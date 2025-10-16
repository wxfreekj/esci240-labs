#!/usr/bin/env python3
"""
Test grader on local file without downloading from Canvas
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from grade_lab03_ai import Lab3Parser, Lab3Grader, AUTOGRADER_KEY


def test_local_file(file_path):
    """Test grading on a local file"""

    print(f"\n{'='*60}")
    print(f"Testing Local File: {os.path.basename(file_path)}")
    print(f"{'='*60}\n")

    # Parse submission
    parser = Lab3Parser()
    answers = parser.parse_submission(file_path)
    print(f"📋 Parsed {len(answers)} questions\n")

    # Grade submission
    grader = Lab3Grader(AUTOGRADER_KEY)
    total_score, detailed_results = grader.grade_submission(answers)

    # Display results
    print(f"{'='*60}")
    print(f"GRADING RESULTS")
    print(f"{'='*60}\n")

    for q_id in sorted(detailed_results.keys()):
        result = detailed_results[q_id]
        print(f"{q_id.upper()}: {result['score']:.1f}/{result['max_points']}")
        print(f"   {result['feedback']}")
        if "student_answer" in result:
            answer = result["student_answer"]
            if isinstance(answer, str) and len(answer) > 60:
                print(f"   Student: {answer[:60]}...")
            elif isinstance(answer, dict):
                print(f"   Student: {answer}")
        print()

    print(f"{'='*60}")
    print(f"TOTAL SCORE: {total_score:.1f}/30")
    percentage = (total_score / 30) * 100
    print(f"PERCENTAGE: {percentage:.1f}%")
    print(f"{'='*60}\n")

    return total_score, detailed_results


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Test Lab 3 grader on local file")
    parser.add_argument(
        "file",
        nargs="?",
        default=r"submissions\lab03\raw\Test Student_6299\Lab03_AtmosphericAnalysis.txt",
        help="Path to submission file",
    )

    args = parser.parse_args()

    # Resolve relative path
    if not os.path.isabs(args.file):
        args.file = os.path.join(os.path.dirname(__file__), args.file)

    if not os.path.exists(args.file):
        print(f"❌ File not found: {args.file}")
        sys.exit(1)

    test_local_file(args.file)
