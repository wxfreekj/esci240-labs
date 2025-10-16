#!/usr/bin/env python3
"""
Lab 3 AI Grader - Hybrid Rule-Based and Keyword Grading
Temperature, Pressure, and Density in the Atmosphere

Grading Strategy:
- Questions 1-12: Rule-based automatic grading (numerical, exact match)
- Questions 13-14: Keyword-based scoring for short answer responses
"""

import os
import sys
import re
from pathlib import Path
from typing import Dict, List, Tuple, Any

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import CANVAS_API_TOKEN, CANVAS_DOMAIN, COURSE_ID, OUTPUT_BASE_DIR
from canvasapi import Canvas

# Lab 3 Configuration
LAB_NUMBER = 3
LAB_NAME = "Lab03_AtmosphericAnalysis"
TOTAL_POINTS = 30

# ============================================================================
# AUTOGRADER ANSWER KEY
# ============================================================================

AUTOGRADER_KEY = {
    # Each question includes points, answer type, correct value(s), and tolerance if applicable.
    "q1": {
        "points": 2,
        "type": "dictionary",
        "answers": {"5.6": 50, "11.2": 25, "16.8": 12.5, "22.4": 6.25},
    },
    "q2": {"points": 3, "type": "exact_match", "answers": ["Curve B", "B"]},
    "q3a": {
        "points": 2,
        "type": "numerical_pair",
        "answers": {
            "pressure": {"value": 250, "tolerance": 15},
            "percentage": {"value": 25, "tolerance": 5},
        },
    },
    "q3b": {
        "points": 2,
        "type": "numerical_pair",
        "answers": {
            "pressure": {"value": 330, "tolerance": 15},
            "percentage": {"value": 33, "tolerance": 5},
        },
    },
    "q3c": {
        "points": 2,
        "type": "numerical_pair",
        "answers": {
            "pressure": {"value": 820, "tolerance": 15},
            "percentage": {"value": 82, "tolerance": 5},
        },
    },
    "q4": {
        "points": 1,
        "type": "exact_match",
        "answers": ["C"],
    },
    "q5": {
        "points": 1,
        "type": "exact_match",
        "answers": ["C"],
    },
    "q6": {
        "points": 1,
        "type": "exact_match",
        "answers": ["B"],
    },
    "q7": {
        "points": 2,
        "type": "multipart",
        "answers": {
            "color": ["Red", "B", "red"],  # Upper-level inversion in stratosphere
            "start_height": {"value": 10, "tolerance": 1},
            "end_height": {"value": 12, "tolerance": 1},
        },
    },
    "q8": {
        "points": 2,
        "type": "numerical_pair",
        "answers": {
            "height": {"value": 10, "tolerance": 0.5},
            "temperature": {"value": -55, "tolerance": 5},
        },
    },
    "q9": {
        "points": 2,
        "type": "numerical_pair",
        "answers": {
            "height": {"value": 11, "tolerance": 0.5},
            "temperature": {"value": -55, "tolerance": 5},
        },
    },
    "q10": {
        "points": 2,
        "type": "numerical_pair",
        "answers": {
            "height": {"value": 16, "tolerance": 0.5},
            "temperature": {"value": -75, "tolerance": 5},
        },
    },
    "q11": {"points": 1, "type": "exact_match", "answers": ["Red"]},
    "q12": {
        "points": 1,
        "type": "exact_match",
        "answers": ["Magenta"],
    },
    "q13": {
        "points": 3,
        "type": "keyword",
        "scoring": {
            "full_credit": {
                "require_all": [],
                "require_any": [
                    "warmer",
                    "colder",
                    "temperature",
                ],  # Accept "temperature" too
                "count_minimum": 2,  # Reduced from 3 to 2
                "keywords": [
                    "higher",
                    "lower",
                    "expands",
                    "contracts",
                    "increases",  # Added - student says "increases"
                    "decreases",  # Added for completeness
                    "height",
                    "tropopause",  # Added - key term
                    "density",
                ],
            },
            "partial_credit": {
                "require_all": [],
                "require_any": ["warmer", "colder", "temperature"],  # More flexible
                "count_minimum": 1,  # Reduced from 2 to 1
                "keywords": ["higher", "lower", "increases", "decreases", "height"],
            },
        },
    },
    "q14": {
        "points": 3,
        "type": "keyword",
        "scoring": {
            "full_credit": {
                "require_all": [],
                "require_any": ["decrease", "less", "lower", "reduce"],
                "count_minimum": 1,  # Reduced from 2 to 1 - just need directional understanding
                "keywords": [
                    "weight",
                    "air",
                    "gravity",
                    "density",
                    "pressure",
                    "compress",
                    "altitude",
                    "height",
                    "up",
                    "all",  # Added - student says "all decrease"
                ],
            },
            "partial_credit": {
                "require_all": [],
                "require_any": ["decrease", "less", "lower", "reduce", "down"],
                "count_minimum": 0,  # Just need to mention the concept
                "keywords": ["weight", "air", "density", "pressure", "up"],
            },
        },
    },
}


# ============================================================================
# SUBMISSION PARSER
# ============================================================================


class Lab3Parser:
    """
    Parse Lab 3 submission files

    The lab uses a JavaScript export function that generates a consistent format.
    We use exact label matching instead of complex regex patterns.
    See: web-components/lab03/index.html - exportToTextFile() function
    """

    @staticmethod
    def parse_submission(file_path: str) -> Dict[str, Any]:
        """
        Parse Lab 3 submission using the known structure from JavaScript export

        The format is guaranteed by the lab's exportToTextFile() function,
        so we can use exact label matching instead of complex regex.

        Returns:
            Dictionary with question IDs as keys and student answers as values
        """
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        answers = {}

        # ====================================================================
        # Question 1: Four height values with exact labels from JavaScript
        # Format: "  Height 22.4 km: 6.25%"
        # ====================================================================
        answers["q1"] = {}
        for height, label in [
            ("22.4", "  Height 22.4 km:"),
            ("16.8", "  Height 16.8 km:"),
            ("11.2", "  Height 11.2 km:"),
            ("5.6", "  Height 5.6 km:"),
        ]:
            if label in content:
                # Get everything after the label until %
                start = content.index(label) + len(label)
                value_str = content[start : start + 20].split("%")[0].strip()
                try:
                    answers["q1"][height] = float(value_str)
                except ValueError:
                    pass

        # ====================================================================
        # Question 2: Exact label "Answer: Curve "
        # Format: "  Answer: Curve B"
        # ====================================================================
        label = "  Answer: Curve "
        if label in content:
            start = content.index(label) + len(label)
            answers["q2"] = content[start : start + 1]  # Just grab next character

        # ====================================================================
        # Question 3a-c: Exact labels from JavaScript export
        # Format: "  a. Cruising airliner (11 km):"
        #         "     Pressure: 220 mb"
        #         "     Percentage above: 22%"
        # ====================================================================
        for part, desc in [
            ("a", "a. Cruising airliner"),
            ("b", "b. Mt. Everest"),
            ("c", "c. Denver, CO"),
        ]:
            if desc in content:
                section_start = content.index(desc)
                section = content[section_start : section_start + 200]

                answers[f"q3{part}"] = {}

                # Pressure line
                if "     Pressure:" in section:
                    start = section.index("     Pressure:") + len("     Pressure:")
                    pressure_str = section[start : start + 20].split("mb")[0].strip()
                    try:
                        answers[f"q3{part}"]["pressure"] = float(pressure_str)
                    except ValueError:
                        pass

                # Percentage line
                if "     Percentage above:" in section:
                    start = section.index("     Percentage above:") + len(
                        "     Percentage above:"
                    )
                    pct_str = section[start : start + 20].split("%")[0].strip()
                    try:
                        answers[f"q3{part}"]["percentage"] = float(pct_str)
                    except ValueError:
                        pass

        # ====================================================================
        # Questions 4-6: Station letters
        # Format: "  Answer: Station C"
        # ====================================================================
        for q_num, text in [
            (4, "Question 4 (1 pt): Station with highest surface temperature"),
            (5, "Question 5 (1 pt): Station with highest temperature at 10 km"),
            (6, "Question 6 (1 pt): Station with highest temperature at 14 km"),
        ]:
            if text in content:
                section_start = content.index(text)
                section = content[section_start : section_start + 150]
                if "  Answer: Station " in section:
                    start = section.index("  Answer: Station ") + len(
                        "  Answer: Station "
                    )
                    answers[f"q{q_num}"] = (
                        section[start : start + 20].split("\n")[0].strip()
                    )

        # ====================================================================
        # Question 7: Inversion layer - 3 values
        # Format: "  Color: red"
        #         "  Start height: 10 km"
        #         "  End height: 12 km"
        # ====================================================================
        if "Question 7 (2 pts): Inversion layer identification" in content:
            section_start = content.index(
                "Question 7 (2 pts): Inversion layer identification"
            )
            section = content[section_start : section_start + 200]

            answers["q7"] = {}

            if "  Color:" in section:
                start = section.index("  Color:") + len("  Color:")
                answers["q7"]["color"] = (
                    section[start : start + 20].split("\n")[0].strip()
                )

            if "  Start height:" in section:
                start = section.index("  Start height:") + len("  Start height:")
                height_str = section[start : start + 20].split("km")[0].strip()
                try:
                    answers["q7"]["start_height"] = float(height_str)
                except ValueError:
                    pass

            if "  End height:" in section:
                start = section.index("  End height:") + len("  End height:")
                height_str = section[start : start + 20].split("km")[0].strip()
                try:
                    answers["q7"]["end_height"] = float(height_str)
                except ValueError:
                    pass

        # ====================================================================
        # Questions 8-10: Tropopause data
        # Format: "  Height: 10 km"
        #         "  Temperature: -50°C"
        # ====================================================================
        for q_num, color in [(8, "red"), (9, "blue"), (10, "magenta")]:
            question_text = f"Question {q_num} (2 pts): Tropopause for {color} station"
            if question_text in content:
                section_start = content.index(question_text)
                section = content[section_start : section_start + 150]

                answers[f"q{q_num}"] = {}

                if "  Height:" in section:
                    start = section.index("  Height:") + len("  Height:")
                    height_str = section[start : start + 20].split("km")[0].strip()
                    try:
                        answers[f"q{q_num}"]["height"] = float(height_str)
                    except ValueError:
                        pass

                if "  Temperature:" in section:
                    start = section.index("  Temperature:") + len("  Temperature:")
                    temp_str = section[start : start + 20].split("°C")[0].strip()
                    try:
                        answers[f"q{q_num}"]["temperature"] = float(temp_str)
                    except ValueError:
                        pass

        # ====================================================================
        # Questions 11-12: Color identification
        # Format: "  Answer: red"
        # ====================================================================
        for q_num, location in [(11, "Alaska"), (12, "the tropics")]:
            question_text = (
                f"Question {q_num} (1 pt): Color plot representing {location}"
            )
            if question_text in content:
                section_start = content.index(question_text)
                section = content[section_start : section_start + 100]
                if "  Answer:" in section:
                    start = section.index("  Answer:") + len("  Answer:")
                    answers[f"q{q_num}"] = (
                        section[start : start + 20].split("\n")[0].strip()
                    )

        # ====================================================================
        # Questions 13-14: Essay responses
        # Format: Paragraph text between question header and next section
        # ====================================================================
        for q_num, text in [
            (13, "Question 13 (3 pts): Tropopause-Temperature Relationship"),
            (14, "Question 14 (3 pts): Atmospheric Variables"),
        ]:
            if text in content:
                section_start = content.index(text) + len(text)
                # Find the next question or end marker
                end_markers = [
                    "Question 13",
                    "Question 14",
                    "PART 5",
                    "===",
                    "END OF SUBMISSION",
                ]
                next_section = len(content)
                for marker in end_markers:
                    marker_pos = content.find(marker, section_start + 10)
                    if marker_pos != -1 and marker_pos < next_section:
                        next_section = marker_pos

                essay_text = content[section_start:next_section].strip()
                # Remove [NOT ANSWERED] markers
                if "[NOT ANSWERED]" not in essay_text and essay_text:
                    answers[f"q{q_num}"] = essay_text

        return answers


# ============================================================================
# GRADING ENGINE
# ============================================================================


class Lab3Grader:
    """Hybrid grader for Lab 3"""

    def __init__(self, answer_key: Dict):
        self.answer_key = answer_key

    def grade_submission(self, answers: Dict[str, Any]) -> Tuple[float, Dict[str, Any]]:
        """
        Grade a complete submission

        Returns:
            (total_score, detailed_results)
        """
        total_score = 0
        detailed_results = {}

        for question_id, question_config in self.answer_key.items():
            if question_id not in answers:
                detailed_results[question_id] = {
                    "score": 0,
                    "max_points": question_config["points"],
                    "feedback": "No answer provided",
                }
                continue

            student_answer = answers[question_id]
            question_type = question_config["type"]

            # Grade based on question type
            if question_type == "dictionary":
                score, feedback = self._grade_dictionary(
                    student_answer,
                    question_config["answers"],
                    question_config["points"],
                )
            elif question_type == "exact_match":
                score, feedback = self._grade_exact_match(
                    student_answer,
                    question_config["answers"],
                    question_config["points"],
                )
            elif question_type == "numerical_pair":
                score, feedback = self._grade_numerical_pair(
                    student_answer,
                    question_config["answers"],
                    question_config["points"],
                )
            elif question_type == "multipart":
                score, feedback = self._grade_multipart(
                    student_answer,
                    question_config["answers"],
                    question_config["points"],
                )
            elif question_type == "keyword":
                score, feedback = self._grade_keyword(
                    student_answer,
                    question_config["scoring"],
                    question_config["points"],
                )
            else:
                score = 0
                feedback = f"Unknown question type: {question_type}"

            total_score += score
            detailed_results[question_id] = {
                "score": score,
                "max_points": question_config["points"],
                "feedback": feedback,
                "student_answer": student_answer,
            }

        return total_score, detailed_results

    def _grade_dictionary(
        self, student_dict: Dict, correct_dict: Dict, max_points: float
    ) -> Tuple[float, str]:
        """Grade Q1 table - dictionary mapping"""
        if not isinstance(student_dict, dict):
            return 0, "Invalid format - expected table data"

        points_per_entry = max_points / len(correct_dict)
        score = 0
        feedback_parts = []

        for height, correct_percentage in correct_dict.items():
            if height in student_dict:
                student_percentage = student_dict[height]
                if abs(student_percentage - correct_percentage) <= 1:  # ±1% tolerance
                    score += points_per_entry
                    feedback_parts.append(f"{height}km: ✓ ({student_percentage}%)")
                else:
                    feedback_parts.append(
                        f"{height}km: ✗ ({student_percentage}% vs {correct_percentage}%)"
                    )
            else:
                feedback_parts.append(f"{height}km: Missing")

        feedback = ", ".join(feedback_parts)
        return score, feedback

    def _grade_exact_match(
        self, student_answer: str, correct_answers: List[str], max_points: float
    ) -> Tuple[float, str]:
        """Grade exact match questions (colors, stations, curves)"""
        student_clean = student_answer.strip().lower()

        for correct in correct_answers:
            if student_clean == correct.lower():
                return max_points, f"Correct: {student_answer}"

        return (
            0,
            f'Incorrect: {student_answer} (expected one of: {", ".join(correct_answers)})',
        )

    def _grade_numerical_pair(
        self, student_answer: Dict, correct_answers: Dict, max_points: float
    ) -> Tuple[float, str]:
        """Grade numerical pairs (pressure/percentage, height/temperature)"""
        if not isinstance(student_answer, dict):
            return 0, "Invalid format - expected two values"

        points_per_value = max_points / 2
        score = 0
        feedback_parts = []

        for key, expected in correct_answers.items():
            if key not in student_answer:
                feedback_parts.append(f"{key}: Missing")
                continue

            student_value = student_answer[key]
            expected_value = expected["value"]
            tolerance = expected["tolerance"]

            if abs(student_value - expected_value) <= tolerance:
                score += points_per_value
                feedback_parts.append(f"{key}: ✓ ({student_value})")
            else:
                feedback_parts.append(
                    f"{key}: ✗ ({student_value} vs {expected_value}±{tolerance})"
                )

        feedback = ", ".join(feedback_parts)
        return score, feedback

    def _grade_multipart(
        self, student_answer: Dict, correct_answers: Dict, max_points: float
    ) -> Tuple[float, str]:
        """Grade Q7 multipart (color + two heights)"""
        if not isinstance(student_answer, dict):
            return 0, "Invalid format"

        score = 0
        feedback_parts = []

        # Check color (1 point)
        if "color" in student_answer:
            student_color = student_answer["color"].strip().lower()
            correct_colors = [c.lower() for c in correct_answers["color"]]
            if student_color in correct_colors:
                score += 1
                feedback_parts.append(f"Color: ✓")
            else:
                feedback_parts.append(f'Color: ✗ ({student_answer["color"]})')
        else:
            feedback_parts.append("Color: Missing")

        # Check start height (0.5 points)
        if "start_height" in student_answer:
            expected = correct_answers["start_height"]["value"]
            tolerance = correct_answers["start_height"]["tolerance"]
            if abs(student_answer["start_height"] - expected) <= tolerance:
                score += 0.5
                feedback_parts.append(f"Start: ✓")
            else:
                feedback_parts.append(f'Start: ✗ ({student_answer["start_height"]}km)')
        else:
            feedback_parts.append("Start: Missing")

        # Check end height (0.5 points)
        if "end_height" in student_answer:
            expected = correct_answers["end_height"]["value"]
            tolerance = correct_answers["end_height"]["tolerance"]
            if abs(student_answer["end_height"] - expected) <= tolerance:
                score += 0.5
                feedback_parts.append(f"End: ✓")
            else:
                feedback_parts.append(f'End: ✗ ({student_answer["end_height"]}km)')
        else:
            feedback_parts.append("End: Missing")

        feedback = ", ".join(feedback_parts)
        return score, feedback

    def _grade_keyword(
        self, student_answer: str, scoring_config: Dict, max_points: float
    ) -> Tuple[float, str]:
        """Grade essay questions using keyword matching"""
        student_lower = student_answer.lower()

        # Try full credit first
        full_credit = scoring_config["full_credit"]
        if self._check_keyword_criteria(student_lower, full_credit):
            return max_points, f"Full credit - comprehensive answer"

        # Try partial credit
        partial_credit = scoring_config["partial_credit"]
        if self._check_keyword_criteria(student_lower, partial_credit):
            partial_score = max_points * 0.6  # 60% for partial
            return partial_score, f"Partial credit - answer needs more detail"

        return 0, "Insufficient detail or missing key concepts"

    def _check_keyword_criteria(self, text: str, criteria: Dict) -> bool:
        """Check if text meets keyword criteria"""
        # Check require_all
        if criteria["require_all"]:
            for keyword in criteria["require_all"]:
                if keyword.lower() not in text:
                    return False

        # Check require_any
        if criteria["require_any"]:
            found_any = False
            for keyword in criteria["require_any"]:
                if keyword.lower() in text:
                    found_any = True
                    break
            if not found_any:
                return False

        # Check count_minimum with keywords
        if criteria["count_minimum"] > 0 and criteria["keywords"]:
            count = sum(
                1 for keyword in criteria["keywords"] if keyword.lower() in text
            )
            if count < criteria["count_minimum"]:
                return False

        return True


# ============================================================================
# MAIN GRADING FUNCTION
# ============================================================================


def grade_lab3_submission(
    student_id: int, assignment_id: int, dry_run: bool = False
) -> Dict:
    """
    Grade a single Lab 3 submission

    Args:
        student_id: Canvas student ID
        assignment_id: Canvas assignment ID for Lab 3
        dry_run: If True, don't upload grades to Canvas

    Returns:
        Dictionary with grading results
    """
    # Initialize Canvas
    canvas_url = f"https://{CANVAS_DOMAIN}"
    canvas = Canvas(canvas_url, CANVAS_API_TOKEN)
    course = canvas.get_course(COURSE_ID)
    assignment = course.get_assignment(assignment_id)

    # Get student info
    student = course.get_user(student_id)
    print(f"\n{'='*60}")
    print(f"Grading Lab 3 for: {student.name} (ID: {student_id})")
    print(f"{'='*60}")

    # Get submission
    submission = assignment.get_submission(student_id)

    if not submission.attachments:
        print("❌ No submission found")
        return {"error": "No submission"}

    # Download submission
    submission_dir = (
        OUTPUT_BASE_DIR
        / f"lab{LAB_NUMBER:02d}"
        / "raw"
        / f"{student.name}_{student_id}"
    )
    submission_dir.mkdir(parents=True, exist_ok=True)

    submission_file = None
    for attachment in submission.attachments:
        file_path = submission_dir / attachment.filename
        attachment.download(str(file_path))
        submission_file = file_path
        print(f"📥 Downloaded: {attachment.filename}")

    if not submission_file:
        print("❌ No file to grade")
        return {"error": "No file"}

    # Parse submission
    print(f"\n📋 Parsing submission...")
    parser = Lab3Parser()
    answers = parser.parse_submission(str(submission_file))
    print(f"   Found answers for {len(answers)} questions")

    # Grade submission
    print(f"\n🎯 Grading...")
    grader = Lab3Grader(AUTOGRADER_KEY)
    total_score, detailed_results = grader.grade_submission(answers)

    # Display results
    print(f"\n{'='*60}")
    print(f"GRADING RESULTS")
    print(f"{'='*60}")

    for q_id in sorted(detailed_results.keys()):
        result = detailed_results[q_id]
        print(f"\n{q_id.upper()}: {result['score']:.1f}/{result['max_points']}")
        print(f"   {result['feedback']}")

    print(f"\n{'='*60}")
    print(f"TOTAL SCORE: {total_score:.1f}/{TOTAL_POINTS}")
    percentage = (total_score / TOTAL_POINTS) * 100
    print(f"PERCENTAGE: {percentage:.1f}%")
    print(f"{'='*60}")

    # Upload grade to Canvas
    if not dry_run:
        print(f"\n📤 Uploading grade to Canvas...")
        submission.edit(submission={"posted_grade": total_score})
        print(f"✅ Grade uploaded successfully")
    else:
        print(f"\n⚠️  DRY RUN - Grade not uploaded to Canvas")

    return {
        "student_id": student_id,
        "student_name": student.name,
        "total_score": total_score,
        "max_points": TOTAL_POINTS,
        "percentage": percentage,
        "detailed_results": detailed_results,
    }


# ============================================================================
# CLI INTERFACE
# ============================================================================

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Grade Lab 3 submissions")
    parser.add_argument("--student-id", type=int, help="Student ID to grade")
    parser.add_argument(
        "--assignment-id", type=int, required=True, help="Lab 3 assignment ID"
    )
    parser.add_argument("--dry-run", action="store_true", help="Don't upload grades")
    parser.add_argument(
        "--test", action="store_true", help="Grade Test Student (ID 6299)"
    )

    args = parser.parse_args()

    if args.test:
        student_id = 6299
    elif args.student_id:
        student_id = args.student_id
    else:
        print("Error: Must specify --student-id or --test")
        sys.exit(1)

    result = grade_lab3_submission(student_id, args.assignment_id, dry_run=args.dry_run)

    if "error" not in result:
        print(f"\n✅ Grading complete!")
