#!/usr/bin/env python3
"""
Test Grade Upload to Canvas for Lab 3

Tests the complete workflow:
1. Download submission from Canvas
2. Grade using hybrid grader
3. Upload score back to Canvas gradebook
4. Verify the grade was posted
"""

import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import CANVAS_API_TOKEN, CANVAS_DOMAIN, COURSE_ID
from canvasapi import Canvas
from grade_lab03_ai import grade_lab3_submission


def test_grade_upload(assignment_id: int, student_id: int = 6299, dry_run: bool = True):
    """
    Test the complete grading and upload workflow

    Args:
        assignment_id: Canvas assignment ID for Lab 3
        student_id: Student to test (default: Test Student 6299)
        dry_run: If True, don't actually upload to Canvas
    """
    print("=" * 70)
    print("LAB 3 GRADE UPLOAD TEST")
    print("=" * 70)
    print(f"Assignment ID: {assignment_id}")
    print(f"Student ID: {student_id}")
    print(f"Dry Run: {dry_run}")
    print()

    # Initialize Canvas
    canvas_url = f"https://{CANVAS_DOMAIN}"
    canvas = Canvas(canvas_url, CANVAS_API_TOKEN)
    course = canvas.get_course(COURSE_ID)
    assignment = course.get_assignment(assignment_id)
    student = course.get_user(student_id)

    print(f"📚 Course: {course.name}")
    print(f"📝 Assignment: {assignment.name}")
    print(f"👤 Student: {student.name}")
    print()

    # Get current grade before grading
    submission = assignment.get_submission(student_id)
    current_grade = submission.grade
    print(f"📊 Current grade in Canvas: {current_grade}")
    print()

    # Grade the submission
    print("🎯 Grading submission...")
    result = grade_lab3_submission(
        student_id=student_id, assignment_id=assignment_id, dry_run=dry_run
    )

    if "error" in result:
        print(f"❌ Error: {result['error']}")
        return False

    print()
    print("=" * 70)
    print("GRADING COMPLETE")
    print("=" * 70)
    print(f"Student: {result['student_name']}")
    print(f"Score: {result['total_score']}/{result['max_points']}")
    print(f"Percentage: {result['percentage']:.1f}%")
    print()

    # Verify upload (if not dry run)
    if not dry_run:
        # Refresh submission to get updated grade
        submission = assignment.get_submission(student_id)
        new_grade = submission.grade

        print("=" * 70)
        print("CANVAS GRADEBOOK UPDATE VERIFICATION")
        print("=" * 70)
        print(f"Previous grade: {current_grade}")
        print(f"New grade: {new_grade}")
        print(f"Expected grade: {result['total_score']}")
        print()

        # Compare as floats (Canvas may return int or float)
        if float(new_grade) == float(result["total_score"]):
            print("✅ Grade successfully posted to Canvas!")
            return True
        else:
            print("❌ Grade mismatch - upload may have failed")
            return False
    else:
        print("⚠️  DRY RUN - Grade was NOT uploaded to Canvas")
        print(f"   Would have posted: {result['total_score']}/{result['max_points']}")
        return True


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Test Lab 3 grading and Canvas upload")
    parser.add_argument(
        "--assignment-id",
        type=int,
        default=103764,
        help="Canvas assignment ID for Lab 3 (default: 103764)",
    )
    parser.add_argument(
        "--student-id",
        type=int,
        default=6299,
        help="Student ID to test (default: 6299 - Test Student)",
    )
    parser.add_argument(
        "--upload",
        action="store_true",
        help="Actually upload grade to Canvas (default: dry run)",
    )

    args = parser.parse_args()

    success = test_grade_upload(
        assignment_id=args.assignment_id,
        student_id=args.student_id,
        dry_run=not args.upload,
    )

    if success:
        print("\n✅ Test completed successfully!")
        sys.exit(0)
    else:
        print("\n❌ Test failed!")
        sys.exit(1)
