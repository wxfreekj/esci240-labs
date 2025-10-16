"""
AI-Powered Grader for ESCI 240 Lab 01 - The Nature of Science
Uses OpenAI API to grade subjective responses
"""

import sys
import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any
from dotenv import load_dotenv

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from graders.ai_grader import AIGrader, GradingCriteria, load_ai_grader_from_env

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))


class Lab01AIGrader:
    """AI-powered grader for Lab 1"""

    def __init__(self):
        # Get paths for reference materials
        script_dir = Path(__file__).parent
        grading_instructions_path = script_dir / "grading_instructions.md"
        reference_material_path = script_dir / "lab01_reference.md"

        # Load AI grader with reference materials
        self.ai_grader = load_ai_grader_from_env(
            grading_instructions_path=(
                str(grading_instructions_path)
                if grading_instructions_path.exists()
                else None
            ),
            reference_material_path=(
                str(reference_material_path)
                if reference_material_path.exists()
                else None
            ),
        )

        self.lab_number = 1
        self.total_points = 30

        # Define grading criteria for each question
        self.question_criteria = self._define_criteria()

        # Log loaded materials
        if grading_instructions_path.exists():
            print(f"✓ Loaded grading instructions from: {grading_instructions_path}")
        if reference_material_path.exists():
            print(f"✓ Loaded reference material from: {reference_material_path}")

    def _define_criteria(self) -> Dict[str, List[GradingCriteria]]:
        """Define grading rubric for each question"""

        return {
            "q1a": [
                GradingCriteria(
                    name="Identifies naturalism",
                    description="Correctly identifies that science studies natural/observable phenomena, not supernatural",
                    points=3,
                )
            ],
            "q1b": [
                GradingCriteria(
                    name="Explains uniformity",
                    description="Explains that natural laws/rules are consistent throughout the universe",
                    points=3,
                )
            ],
            "q2": [
                GradingCriteria(
                    name="Rejects fixed steps",
                    description="Correctly states there is no single fixed scientific method",
                    points=2,
                ),
                GradingCriteria(
                    name="Explains variability",
                    description="Explains that scientific approaches vary by field/question",
                    points=1,
                ),
            ],
            "q3": [
                GradingCriteria(
                    name="Testing past events",
                    description="Explains how scientists make predictions about evidence that should still exist (fossils, rocks, etc.)",
                    points=2,
                ),
                GradingCriteria(
                    name="Clear explanation",
                    description="Clearly explains the concept of indirect evidence",
                    points=1,
                ),
            ],
            "q4a": [
                GradingCriteria(
                    name="Identifies bias sources",
                    description="Identifies ways bias can enter science (interpretation, data selection, personal characteristics)",
                    points=3,
                )
            ],
            "q4b": [
                GradingCriteria(
                    name="Describes safeguards",
                    description="Describes strategies to minimize bias (multiple investigators, peer review, etc.)",
                    points=3,
                )
            ],
            "q5a": [
                GradingCriteria(
                    name="Rejects authority",
                    description="Explains that scientific truth is not determined by authority/famous scientists",
                    points=3,
                )
            ],
            "q5b": [
                GradingCriteria(
                    name="Evidence-based acceptance",
                    description="Explains that ideas are accepted based on evidence and explanatory power, not authority",
                    points=3,
                )
            ],
            "q6a": [
                GradingCriteria(
                    name="Identifies ethical challenge",
                    description="Identifies a valid ethical challenge in science (harm, consent, fairness, etc.)",
                    points=3,
                )
            ],
            "q6b": [
                GradingCriteria(
                    name="Explains second challenge",
                    description="Identifies and explains a second distinct ethical challenge",
                    points=3,
                )
            ],
        }

    def parse_submission(self, submission_file: Path) -> Dict[str, str]:
        """Parse the structured submission file"""
        with open(submission_file, "r", encoding="utf-8") as f:
            content = f.read()

        answers = {}

        # Extract metadata
        lab_match = re.search(r"LAB:\s*(\d+)", content)
        if lab_match and int(lab_match.group(1)) != 1:
            raise ValueError(f"Wrong lab number: {lab_match.group(1)}")

        # Parse each question
        for q_num in range(1, 7):
            pattern = rf"\[QUESTION_{q_num}\](.*?)\[/QUESTION_{q_num}\]"
            match = re.search(pattern, content, re.DOTALL)

            if match:
                q_content = match.group(1)

                # Extract prompt for context
                prompt_match = re.search(
                    r"PROMPT:\s*(.*?)(?=\n\n|\[)", q_content, re.DOTALL
                )
                prompt = prompt_match.group(1).strip() if prompt_match else ""

                # Check if split type (has PART_A and PART_B)
                if "TYPE: split" in q_content:
                    part_a = re.search(
                        r"\[PART_A\](.*?)\[/PART_A\]", q_content, re.DOTALL
                    )
                    part_b = re.search(
                        r"\[PART_B\](.*?)\[/PART_B\]", q_content, re.DOTALL
                    )

                    answers[f"q{q_num}a"] = {
                        "response": part_a.group(1).strip() if part_a else "",
                        "prompt": prompt,
                    }
                    answers[f"q{q_num}b"] = {
                        "response": part_b.group(1).strip() if part_b else "",
                        "prompt": prompt,
                    }
                else:
                    # Essay type
                    answer = re.search(
                        r"\[ANSWER\](.*?)\[/ANSWER\]", q_content, re.DOTALL
                    )
                    answers[f"q{q_num}"] = {
                        "response": answer.group(1).strip() if answer else "",
                        "prompt": prompt,
                    }

        return answers

    def grade_submission(self, submission_file: Path) -> Dict[str, Any]:
        """
        Grade a Lab 1 submission using AI

        Returns:
            Dictionary with scoring results and feedback
        """

        try:
            # Parse submission
            answers = self.parse_submission(submission_file)

            # Grade each question
            question_results = {}
            total_earned = 0
            flagged_questions = []

            for q_id, answer_data in answers.items():
                if q_id not in self.question_criteria:
                    print(f"Warning: No criteria defined for {q_id}")
                    continue

                # Get the response and prompt
                response = answer_data["response"]
                prompt = answer_data["prompt"]

                # Skip empty responses
                if not response or len(response.strip()) < 10:
                    criteria = self.question_criteria[q_id]
                    points_possible = sum(c.points for c in criteria)
                    question_results[q_id] = {
                        "points_earned": 0,
                        "points_possible": points_possible,
                        "percentage": 0.0,
                        "feedback": "No response provided",
                        "flagged": True,
                        "review_reason": "Empty response",
                    }
                    flagged_questions.append(q_id)
                    continue

                # Grade with AI
                result = self.ai_grader.grade_response(
                    question_prompt=prompt,
                    student_response=response,
                    criteria=self.question_criteria[q_id],
                    context="This is for an introductory meteorology course (ESCI 240). The reading is from Science for All Americans by AAAS.",
                )

                question_results[q_id] = {
                    "points_earned": result.points_earned,
                    "points_possible": result.points_possible,
                    "percentage": result.percentage,
                    "feedback": result.feedback,
                    "confidence": result.confidence,
                    "flagged": result.flagged_for_review,
                    "review_reason": result.review_reason,
                    "criteria_scores": result.criteria_scores,
                }

                total_earned += result.points_earned

                if result.flagged_for_review:
                    flagged_questions.append(q_id)

            # Calculate overall statistics
            percentage = (
                (total_earned / self.total_points * 100) if self.total_points > 0 else 0
            )

            # Determine if entire submission needs review
            needs_review = len(flagged_questions) > 0

            return {
                "total_points_earned": total_earned,
                "total_points_possible": self.total_points,
                "percentage": percentage,
                "letter_grade": self._calculate_letter_grade(percentage),
                "question_results": question_results,
                "flagged_for_review": needs_review,
                "flagged_questions": flagged_questions,
                "grading_method": "AI (OpenAI API)",
                "status": "needs_review" if needs_review else "graded",
            }

        except Exception as e:
            return {
                "error": str(e),
                "total_points_earned": 0,
                "total_points_possible": self.total_points,
                "percentage": 0.0,
                "status": "error",
                "flagged_for_review": True,
                "review_reason": f"Grading error: {str(e)}",
            }

    def _calculate_letter_grade(self, percentage: float) -> str:
        """Convert percentage to letter grade"""
        if percentage >= 93:
            return "A"
        elif percentage >= 90:
            return "A-"
        elif percentage >= 87:
            return "B+"
        elif percentage >= 83:
            return "B"
        elif percentage >= 80:
            return "B-"
        elif percentage >= 77:
            return "C+"
        elif percentage >= 73:
            return "C"
        elif percentage >= 70:
            return "C-"
        elif percentage >= 67:
            return "D+"
        elif percentage >= 63:
            return "D"
        elif percentage >= 60:
            return "D-"
        else:
            return "F"

    def grade_all_submissions(self, submissions_dir: Path) -> Dict[str, Any]:
        """
        Grade all submissions in a directory

        Args:
            submissions_dir: Path to lab01/raw/ directory with student folders

        Returns:
            Dictionary with all grading results
        """

        results = {
            "lab_number": self.lab_number,
            "graded_at": None,
            "total_submissions": 0,
            "student_grades": {},
        }

        # Find all student submission folders
        for student_folder in submissions_dir.iterdir():
            if not student_folder.is_dir():
                continue

            # Find the submission file
            submission_file = None
            for file in student_folder.iterdir():
                if file.suffix == ".txt" and "Lab01" in file.name:
                    submission_file = file
                    break

            if not submission_file:
                print(f"Warning: No submission file found in {student_folder.name}")
                continue

            print(f"Grading {student_folder.name}...")

            # Grade the submission
            grade_result = self.grade_submission(submission_file)

            results["student_grades"][student_folder.name] = grade_result
            results["total_submissions"] += 1

            # Print summary
            if "error" in grade_result:
                print(f"  ERROR: {grade_result['error']}")
            else:
                print(
                    f"  Score: {grade_result['total_points_earned']}/{grade_result['total_points_possible']} ({grade_result['percentage']:.1f}%) - {grade_result['letter_grade']}"
                )
                if grade_result["flagged_for_review"]:
                    print(
                        f"  ⚠️  FLAGGED FOR REVIEW: {', '.join(grade_result['flagged_questions'])}"
                    )

        # Add timestamp
        from datetime import datetime

        results["graded_at"] = datetime.now().isoformat()

        return results


# CLI interface
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Grade Lab 1 submissions using AI")
    parser.add_argument(
        "--submissions-dir",
        type=Path,
        default=Path(__file__).parent.parent / "submissions" / "lab01" / "raw",
        help="Path to submissions directory",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).parent.parent
        / "submissions"
        / "lab01"
        / "graded"
        / "grades.json",
        help="Output file for grades",
    )
    parser.add_argument(
        "--student", type=str, help="Grade only this student (folder name)"
    )

    args = parser.parse_args()

    # Create grader
    grader = Lab01AIGrader()

    # Grade submissions
    if args.student:
        # Grade single student
        student_folder = args.submissions_dir / args.student
        if not student_folder.exists():
            print(f"Error: Student folder not found: {student_folder}")
            sys.exit(1)

        submission_file = None
        for file in student_folder.iterdir():
            if file.suffix == ".txt" and "Lab01" in file.name:
                submission_file = file
                break

        if not submission_file:
            print(f"Error: No submission file found in {student_folder}")
            sys.exit(1)

        print(f"Grading {args.student}...")
        result = grader.grade_submission(submission_file)

        print(json.dumps(result, indent=2))

        # Save individual result
        output_dir = args.output.parent / args.student
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / f"{args.student}_grades.json"
        with open(output_file, "w") as f:
            json.dump(result, f, indent=2)
        print(f"\nResults saved to: {output_file}")
    else:
        # Grade all submissions
        print(f"Grading all submissions in {args.submissions_dir}")
        results = grader.grade_all_submissions(args.submissions_dir)

        # Save results
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)

        print(f"Results saved to: {args.output}")

        print(f"\n✅ Grading complete!")
        print(f"   Total submissions: {results['total_submissions']}")
        print(f"   Results saved to: {args.output}")

        # Summary statistics
        flagged_count = sum(
            1 for g in results["student_grades"].values() if g.get("flagged_for_review")
        )
        if flagged_count > 0:
            print(f"   ⚠️  {flagged_count} submissions flagged for human review")
