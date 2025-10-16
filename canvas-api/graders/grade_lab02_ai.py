"""
AI-Powered Grader for ESCI 240 Lab 02 - Weather Forecasting Tools
Uses OpenAI API to grade URL submissions and analysis responses
"""

import sys
import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from urllib.parse import urlparse
from dotenv import load_dotenv

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from graders.ai_grader import AIGrader, GradingCriteria, load_ai_grader_from_env

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))


class Lab02AIGrader:
    """AI-powered grader for Lab 2 - Weather Forecasting Tools"""

    def __init__(self):
        # Get paths for reference materials
        script_dir = Path(__file__).parent
        grading_instructions_path = script_dir / "grading_instructions.md"
        reference_material_path = script_dir / "lab02_reference.md"

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

        self.lab_number = 2
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
            "q1": [
                GradingCriteria(
                    name="Valid satellite image URL",
                    description="URL shows a satellite image centered on Minnesota (visible or infrared acceptable)",
                    points=2,
                ),
                GradingCriteria(
                    name="Descriptive caption",
                    description="Caption describes satellite type and cloud cover/weather features",
                    points=1,
                ),
            ],
            "q2": [
                GradingCriteria(
                    name="Valid radar image URL",
                    description="URL shows a weather radar image centered on Chicago, Illinois",
                    points=2,
                ),
                GradingCriteria(
                    name="Descriptive caption",
                    description="Caption describes radar and precipitation patterns",
                    points=1,
                ),
            ],
            "q3": [
                GradingCriteria(
                    name="Valid surface observations URL",
                    description="URL shows a surface weather map with observations over Kansas (temperatures, wind barbs, station plots)",
                    points=2,
                ),
                GradingCriteria(
                    name="Descriptive caption",
                    description="Caption describes surface observations and data shown",
                    points=1,
                ),
            ],
            "q4": [
                GradingCriteria(
                    name="Valid NWS forecast URL",
                    description="URL is from weather.gov for Fargo, North Dakota",
                    points=1,
                ),
                GradingCriteria(
                    name="Complete 7-day forecast",
                    description="Caption/text includes the full 7-day forecast from NWS",
                    points=2,
                ),
            ],
            "q5": [
                GradingCriteria(
                    name="Valid SPC Day 2 outlook URL",
                    description="URL shows Storm Prediction Center's Day 2 Convective Outlook map",
                    points=2,
                ),
                GradingCriteria(
                    name="Descriptive caption",
                    description="Caption describes Day 2 outlook and severe weather risk areas",
                    points=1,
                ),
            ],
            "q6": [
                GradingCriteria(
                    name="Valid WPC QPF URL",
                    description="URL shows Weather Prediction Center Quantitative Precipitation Forecast",
                    points=2,
                ),
                GradingCriteria(
                    name="Descriptive caption",
                    description="Caption describes QPF and time period (6-hr, 24-hr, 7-day, etc.)",
                    points=1,
                ),
            ],
            "q7": [
                GradingCriteria(
                    name="Valid ensemble probability map",
                    description="URL shows an ensemble model forecast with probability of snowfall/precipitation",
                    points=2,
                ),
                GradingCriteria(
                    name="Descriptive caption",
                    description="Caption mentions ensemble/probability and what is being forecast",
                    points=1,
                ),
            ],
            "q8": [
                GradingCriteria(
                    name="Valid model precipitation forecast",
                    description="URL shows precipitation forecast from a weather model (GFS, NAM, ECMWF, etc.)",
                    points=2,
                ),
                GradingCriteria(
                    name="Caption identifies model",
                    description="Caption mentions model name and describes precipitation forecast",
                    points=1,
                ),
            ],
            "q9": [
                GradingCriteria(
                    name="Valid 500mb map URL",
                    description="URL shows 500mb heights and winds covering central U.S.",
                    points=2,
                ),
                GradingCriteria(
                    name="Descriptive caption",
                    description="Caption describes 500mb/upper level heights and winds",
                    points=1,
                ),
            ],
            "q10": [
                GradingCriteria(
                    name="Valid visible satellite URL",
                    description="URL shows a daytime visible satellite image over southeastern U.S.",
                    points=2,
                ),
                GradingCriteria(
                    name="Descriptive caption",
                    description="Caption mentions visible satellite and describes SE US or cloud features",
                    points=1,
                ),
            ],
        }

    def parse_submission(self, file_path: Path) -> Dict[str, Dict[str, str]]:
        """
        Parse Lab 2 submission file

        Expected format (from actual student submissions):
        1. Question Title
        --------------------------------------------------
        Link: https://example.com/weather

        Caption:
        Description of the resource

        ===================================================
        """

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        questions = {}

        # Split by question sections (numbered 1-10)
        # Pattern: number followed by period and text, then link and caption
        sections = re.split(r"(?=\n\d+\.)", content)

        for section in sections:
            # Extract question number
            num_match = re.match(r"\n?(\d+)\.", section)
            if not num_match:
                continue

            question_num = num_match.group(1)
            q_id = f"q{question_num}"

            # Extract Link/URL
            url_match = re.search(r"Link:\s*(.+?)(?:\n|$)", section, re.MULTILINE)
            url = url_match.group(1).strip() if url_match else ""

            # Extract Caption (everything after "Caption:" until next section or end)
            caption_match = re.search(
                r"Caption:\s*(.+?)(?=\n===|$)", section, re.DOTALL
            )
            caption = caption_match.group(1).strip() if caption_match else ""

            questions[q_id] = {
                "url": url,
                "caption": caption,
                "answer": caption if question_num == "10" else "",
            }

        return questions

    def validate_url_domain(self, url: str, required_domains: List[str]) -> bool:
        """Check if URL contains one of the required domains"""
        try:
            parsed = urlparse(url.lower().strip())
            domain = parsed.netloc.replace("www.", "")
            return any(req_domain in domain for req_domain in required_domains)
        except:
            return False

    def validate_url_path(self, url: str, required_terms: List[str]) -> bool:
        """Check if URL path contains required terms"""
        try:
            parsed = urlparse(url.lower())
            path = parsed.path.lower()
            return any(term in path for term in required_terms)
        except:
            return False

    def build_question_prompt(
        self, question_id: str, url: str, caption: str, answer: str
    ) -> str:
        """Build a detailed prompt for the AI grader based on question type"""

        prompts = {
            "q1": f"""Question 1: Satellite Image – Minnesota (3 pts)

Student's URL: {url}
Student's Caption: {caption}

Requirements:
- URL should show a satellite image centered on Minnesota
- Visible or infrared satellite acceptable
- Recommended sources: weather.cod.edu, weather.rap.ucar.edu
- Caption should describe satellite type and cloud cover/weather features

Grade the URL and caption together.""",
            "q2": f"""Question 2: Radar Image – Chicago (3 pts)

Student's URL: {url}
Student's Caption: {caption}

Requirements:
- URL should show a weather radar image centered on Chicago, Illinois
- Base reflectivity product preferred
- Recommended sources: weather.cod.edu, weather.rap.ucar.edu
- Caption should describe radar and precipitation patterns

Grade the URL and caption together.""",
            "q3": f"""Question 3: Surface Observations – Kansas (3 pts)

Student's URL: {url}
Student's Caption: {caption}

Requirements:
- URL should show a surface weather map with observations over Kansas
- Should include temperatures, wind barbs, station circles
- Recommended sources: weather.cod.edu, weather.rap.ucar.edu
- Caption should describe surface observations and data shown

Grade the URL and caption together.""",
            "q4": f"""Question 4: 7-Day Forecast – Fargo, ND (3 pts)

Student's URL: {url}
Student's Forecast Text: {caption}

Requirements:
- URL should be from National Weather Service (weather.gov) for Fargo, North Dakota
- Caption/text should include the complete 7-day forecast
- Must include all seven days of forecast text
- Caption should contain actual forecast text, not just description

Grade the URL and forecast text together. This is the one question where a long caption is expected.""",
            "q5": f"""Question 5: SPC Day 2 Outlook (3 pts)

Student's URL: {url}
Student's Caption: {caption}

Requirements:
- URL should show Storm Prediction Center's Day 2 Convective Outlook map
- Domain should be spc.noaa.gov
- Caption should describe Day 2 outlook and severe weather risk areas

Grade the URL and caption together.""",
            "q6": f"""Question 6: WPC QPF Forecast (3 pts)

Student's URL: {url}
Student's Caption: {caption}

Requirements:
- URL should show Weather Prediction Center Quantitative Precipitation Forecast (QPF)
- Domain should be wpc.ncep.noaa.gov
- Any time period acceptable (6-hr, 24-hr, 7-day total)
- Caption should describe precipitation forecast and time period

Grade the URL and caption together.""",
            "q7": f"""Question 7: Ensemble Forecast Probability (3 pts)

Student's URL: {url}
Student's Caption: {caption}

Requirements:
- URL should show ensemble model forecast map with probability of snowfall/precipitation
- Recommended sources: spc.noaa.gov/exper/sref/, weather.cod.edu
- Caption should mention ensemble/probability and what is being forecast

Grade the URL and caption together.""",
            "q8": f"""Question 8: Model Precipitation Forecast (3 pts)

Student's URL: {url}
Student's Caption: {caption}

Requirements:
- URL should show precipitation forecast from a weather model (GFS, NAM, ECMWF, etc.)
- Any region/time period acceptable
- Recommended sources: mag.ncep.noaa.gov, twisterdata.com, weather.cod.edu
- Caption should mention model name and describe precipitation forecast

Grade the URL and caption together.""",
            "q9": f"""Question 9: 500 mb Heights and Winds – Central U.S. (3 pts)

Student's URL: {url}
Student's Caption: {caption}

Requirements:
- URL should show 500 mb heights and winds covering central U.S.
- Should show color contours and wind barbs
- Recommended sources: mag.ncep.noaa.gov, weather.cod.edu, twisterdata.com
- Caption should describe 500mb/upper level heights and winds

Grade the URL and caption together.""",
            "q10": f"""Question 10: Visible Satellite – Southeast U.S. (3 pts)

Student's URL: {url}
Student's Caption: {caption}

Requirements:
- URL should show a daytime visible satellite image over southeastern U.S.
- Must be from a time when sun is up (daytime)
- Recommended sources: weather.cod.edu, weather.rap.ucar.edu
- Caption should mention visible satellite and describe SE US or cloud features

Grade the URL and caption together.""",
        }

        return prompts.get(question_id, "")

    def grade_submission(self, file_path: Path) -> Dict[str, Any]:
        """Grade a complete Lab 2 submission"""

        # Parse submission
        questions = self.parse_submission(file_path)

        # Grade each question
        question_results = {}
        total_points_earned = 0

        for q_id in [f"q{i}" for i in range(1, 11)]:
            if q_id not in questions:
                print(f"Warning: {q_id} not found in submission")
                continue

            q_data = questions[q_id]
            criteria = self.question_criteria[q_id]

            # Build question-specific prompt
            prompt = self.build_question_prompt(
                q_id, q_data["url"], q_data["caption"], q_data["answer"]
            )

            # For Q1-Q9, combine URL and caption as the response
            if q_id != "q10":
                student_response = f"URL: {q_data['url']}\nCaption: {q_data['caption']}"
            else:
                student_response = q_data["answer"]

            # Grade with AI
            result = self.ai_grader.grade_response(
                question_prompt=prompt,
                student_response=student_response,
                criteria=criteria,
            )

            # Store result
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

            total_points_earned += result.points_earned

        # Calculate overall grade
        percentage = total_points_earned / self.total_points * 100
        letter_grade = self._calculate_letter_grade(percentage)

        # Determine if needs review
        flagged_questions = [
            q_id for q_id, result in question_results.items() if result["flagged"]
        ]
        flagged_for_review = len(flagged_questions) > 0

        return {
            "total_points_earned": total_points_earned,
            "total_points_possible": self.total_points,
            "percentage": percentage,
            "letter_grade": letter_grade,
            "question_results": question_results,
            "flagged_for_review": flagged_for_review,
            "flagged_questions": flagged_questions,
            "grading_method": "AI (OpenAI API)",
            "status": "needs_review" if flagged_for_review else "auto_approved",
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

    def grade_all_submissions(self, submissions_dir: Path) -> Dict[str, Dict[str, Any]]:
        """Grade all submissions in a directory"""

        results = {}

        for student_folder in submissions_dir.iterdir():
            if not student_folder.is_dir():
                continue

            # Find submission file
            submission_file = None
            for file in student_folder.iterdir():
                if file.suffix == ".txt" and "Lab02" in file.name:
                    submission_file = file
                    break

            if not submission_file:
                print(f"Warning: No submission file found for {student_folder.name}")
                continue

            print(f"Grading {student_folder.name}...")
            results[student_folder.name] = self.grade_submission(submission_file)

        return results


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Grade Lab 02 submissions with AI")
    parser.add_argument(
        "--submissions-dir",
        type=Path,
        default=Path(__file__).parent.parent / "submissions" / "lab02" / "raw",
        help="Directory containing student submissions",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).parent.parent
        / "submissions"
        / "lab02"
        / "graded"
        / "grades.json",
        help="Output file for grading results",
    )
    parser.add_argument(
        "--student", type=str, help="Grade only this student (folder name)"
    )

    args = parser.parse_args()

    # Create grader
    grader = Lab02AIGrader()

    # Grade submissions
    if args.student:
        # Grade single student
        student_folder = args.submissions_dir / args.student
        if not student_folder.exists():
            print(f"Error: Student folder not found: {student_folder}")
            sys.exit(1)

        submission_file = None
        for file in student_folder.iterdir():
            if file.suffix == ".txt" and "Lab02" in file.name:
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
