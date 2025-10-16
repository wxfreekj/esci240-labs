#!/usr/bin/env python3
"""
Batch Grade All Lab 3 Submissions and Upload to Canvas

This script:
1. Fetches all submissions for Lab 3
2. Grades each submission using the hybrid grader
3. Uploads scores back to Canvas gradebook
4. Generates a summary report
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import json

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import CANVAS_API_TOKEN, CANVAS_DOMAIN, COURSE_ID
from canvasapi import Canvas
from grade_lab03_ai import grade_lab3_submission, TOTAL_POINTS


def batch_grade_lab3(
    assignment_id: int, dry_run: bool = False, skip_errors: bool = True
):
    """
    Grade all submissions for Lab 3

    Args:
        assignment_id: Canvas assignment ID for Lab 3
        dry_run: If True, don't upload grades to Canvas
        skip_errors: If True, continue grading even if individual submissions fail

    Returns:
        Summary statistics dictionary
    """
    print("=" * 70)
    print("LAB 3 BATCH GRADING - ATMOSPHERIC ANALYSIS")
    print("=" * 70)
    print(f"Assignment ID: {assignment_id}")
    print(f"Dry Run: {dry_run}")
    print(f"Skip Errors: {skip_errors}")
    print()

    # Initialize Canvas
    canvas_url = f"https://{CANVAS_DOMAIN}"
    canvas = Canvas(canvas_url, CANVAS_API_TOKEN)
    course = canvas.get_course(COURSE_ID)
    assignment = course.get_assignment(assignment_id)

    print(f"📚 Course: {course.name}")
    print(f"📝 Assignment: {assignment.name}")
    print(f"📊 Points Possible: {assignment.points_possible}")
    print()

    # Get all submissions
    submissions = assignment.get_submissions()

    # Statistics
    stats = {
        "total_submissions": 0,
        "graded": 0,
        "errors": 0,
        "skipped": 0,
        "scores": [],
        "results": [],
        "timestamp": datetime.now().isoformat(),
    }

    print("🔍 Processing submissions...\n")

    for submission in submissions:
        student_id = submission.user_id

        # Skip if no submission
        if submission.workflow_state in ["unsubmitted", "graded"]:
            print(f"⏭️  Skipping student {student_id} - {submission.workflow_state}")
            stats["skipped"] += 1
            continue

        stats["total_submissions"] += 1

        print(f"\n{'='*70}")
        print(f"👤 Student ID: {student_id}")
        print(f"{'='*70}")

        try:
            # Grade the submission
            result = grade_lab3_submission(
                student_id=student_id, assignment_id=assignment_id, dry_run=dry_run
            )

            if "error" in result:
                print(f"❌ Error: {result['error']}")
                stats["errors"] += 1
                if not skip_errors:
                    break
            else:
                stats["graded"] += 1
                stats["scores"].append(result["total_score"])
                stats["results"].append(
                    {
                        "student_id": result["student_id"],
                        "student_name": result["student_name"],
                        "score": result["total_score"],
                        "percentage": result["percentage"],
                    }
                )
                print(
                    f"✅ Successfully graded: {result['total_score']}/{TOTAL_POINTS} ({result['percentage']:.1f}%)"
                )

        except Exception as e:
            print(f"❌ Exception grading student {student_id}: {str(e)}")
            stats["errors"] += 1
            if not skip_errors:
                raise

    # Print summary
    print("\n" + "=" * 70)
    print("BATCH GRADING SUMMARY")
    print("=" * 70)
    print(f"Total Submissions: {stats['total_submissions']}")
    print(f"Successfully Graded: {stats['graded']}")
    print(f"Errors: {stats['errors']}")
    print(f"Skipped: {stats['skipped']}")

    if stats["scores"]:
        print(f"\nScore Statistics:")
        print(
            f"  Mean: {sum(stats['scores']) / len(stats['scores']):.2f}/{TOTAL_POINTS}"
        )
        print(f"  Min: {min(stats['scores']):.2f}/{TOTAL_POINTS}")
        print(f"  Max: {max(stats['scores']):.2f}/{TOTAL_POINTS}")

        # Score distribution
        score_ranges = {
            "A (90-100%)": 0,
            "B (80-89%)": 0,
            "C (70-79%)": 0,
            "D (60-69%)": 0,
            "F (<60%)": 0,
        }

        for score in stats["scores"]:
            percentage = (score / TOTAL_POINTS) * 100
            if percentage >= 90:
                score_ranges["A (90-100%)"] += 1
            elif percentage >= 80:
                score_ranges["B (80-89%)"] += 1
            elif percentage >= 70:
                score_ranges["C (70-79%)"] += 1
            elif percentage >= 60:
                score_ranges["D (60-69%)"] += 1
            else:
                score_ranges["F (<60%)"] += 1

        print(f"\nGrade Distribution:")
        for grade_range, count in score_ranges.items():
            print(f"  {grade_range}: {count}")

    print("=" * 70)

    if dry_run:
        print("\n⚠️  DRY RUN - No grades were uploaded to Canvas")
    else:
        print(f"\n✅ All grades uploaded to Canvas gradebook!")

    # Save detailed results
    output_dir = Path(__file__).parent / "batch_results"
    output_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = output_dir / f"lab03_batch_results_{timestamp}.json"

    with open(results_file, "w") as f:
        json.dump(stats, f, indent=2)

    print(f"\n📄 Detailed results saved to: {results_file}")

    return stats


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Batch grade all Lab 3 submissions and upload to Canvas"
    )
    parser.add_argument(
        "--assignment-id",
        type=int,
        required=True,
        help="Canvas assignment ID for Lab 3",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Don't upload grades to Canvas (testing only)",
    )
    parser.add_argument(
        "--stop-on-error",
        action="store_true",
        help="Stop grading if an error occurs (default: skip and continue)",
    )

    args = parser.parse_args()

    stats = batch_grade_lab3(
        assignment_id=args.assignment_id,
        dry_run=args.dry_run,
        skip_errors=not args.stop_on_error,
    )

    # Exit with error code if there were errors
    if stats["errors"] > 0:
        sys.exit(1)
