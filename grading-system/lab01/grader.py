"""
Grader for ESCI 240 Lab 01 - The Nature of Science
"""

import sys
import os
import re

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from shared.grader_base import LabGrader


class Lab01Grader(LabGrader):
    """Grader for Lab 01 assignments"""

    def __init__(self):
        super().__init__(lab_number=1)

        # Keywords to look for in answers (customize based on reading)
        self.q1_keywords = [
            "testable",
            "natural",
            "evidence",
            "observable",
            "consistent",
        ]
        self.q2_keywords = ["observation", "hypothesis", "experiment", "conclusion"]
        self.q3_keywords = ["evidence", "fossil", "record", "indirect", "inference"]
        self.q4_keywords = ["peer review", "replication", "double-blind", "objective"]
        self.q5_keywords = ["evidence", "test", "challenge", "verify", "replicate"]
        self.q6_keywords = ["conflict of interest", "bias", "ethics", "integrity"]

    def parse_submission(self, submission_file: str) -> dict:
        """Parse the structured submission file"""
        with open(submission_file, "r", encoding="utf-8") as f:
            content = f.read()

        answers = {}

        # Extract metadata
        lab_match = re.search(r"LAB:\s*(\d+)", content)
        if lab_match and int(lab_match.group(1)) != 1:
            raise ValueError("Wrong lab number!")

        # Parse each question
        for q_num in range(1, 7):
            pattern = rf"\[QUESTION_{q_num}\](.*?)\[/QUESTION_{q_num}\]"
            match = re.search(pattern, content, re.DOTALL)

            if match:
                q_content = match.group(1)

                # Check if split type (has PART_A and PART_B)
                if "TYPE: split" in q_content:
                    part_a = re.search(
                        r"\[PART_A\](.*?)\[/PART_A\]", q_content, re.DOTALL
                    )
                    part_b = re.search(
                        r"\[PART_B\](.*?)\[/PART_B\]", q_content, re.DOTALL
                    )
                    answers[f"q{q_num}a"] = part_a.group(1).strip() if part_a else ""
                    answers[f"q{q_num}b"] = part_b.group(1).strip() if part_b else ""
                else:
                    # Essay type
                    answer = re.search(
                        r"\[ANSWER\](.*?)\[/ANSWER\]", q_content, re.DOTALL
                    )
                    answers[f"q{q_num}"] = answer.group(1).strip() if answer else ""

        return answers

    def grade_answer(self, answer: str, keywords: list, min_length: int = 20) -> tuple:
        """Grade a single answer based on keywords and length"""
        answer_lower = answer.lower()

        # Check length
        if len(answer) < min_length:
            return 0, f"Answer too short ({len(answer)} chars, need {min_length})"

        # Count keyword matches
        matches = sum(1 for keyword in keywords if keyword.lower() in answer_lower)

        # Scoring based on keyword matches
        if matches >= 2:
            return 1.0, f"Excellent ({matches} key concepts found)"
        elif matches == 1:
            return 0.7, f"Good ({matches} key concept found)"
        else:
            return 0.5, "Needs improvement (missing key concepts)"

    def grade_submission(self, submission_file: str) -> dict:
        """Grade Lab 01 submission"""
        try:
            answers = self.parse_submission(submission_file)

            total_score = 0
            max_score = 20
            feedback = []

            # Question 1: Assumptions (3 pts total, 1.5 each)
            if "q1a" in answers and "q1b" in answers:
                score_a, fb_a = self.grade_answer(answers["q1a"], self.q1_keywords, 15)
                score_b, fb_b = self.grade_answer(answers["q1b"], self.q1_keywords, 15)
                q1_score = (score_a + score_b) * 1.5
                total_score += q1_score
                feedback.append(
                    f"Q1 ({q1_score:.1f}/3.0): Part A: {fb_a}, Part B: {fb_b}"
                )

            # Question 2: Scientific Method (3 pts)
            if "q2" in answers:
                score, fb = self.grade_answer(answers["q2"], self.q2_keywords, 30)
                q2_score = score * 3
                total_score += q2_score
                feedback.append(f"Q2 ({q2_score:.1f}/3.0): {fb}")

            # Question 3: Testing Past Events (4 pts)
            if "q3" in answers:
                score, fb = self.grade_answer(answers["q3"], self.q3_keywords, 40)
                q3_score = score * 4
                total_score += q3_score
                feedback.append(f"Q3 ({q3_score:.1f}/4.0): {fb}")

            # Question 4: Minimizing Bias (3 pts total, 1.5 each)
            if "q4a" in answers and "q4b" in answers:
                score_a, fb_a = self.grade_answer(answers["q4a"], self.q4_keywords, 15)
                score_b, fb_b = self.grade_answer(answers["q4b"], self.q4_keywords, 15)
                q4_score = (score_a + score_b) * 1.5
                total_score += q4_score
                feedback.append(
                    f"Q4 ({q4_score:.1f}/3.0): Part A: {fb_a}, Part B: {fb_b}"
                )

            # Question 5: Science and Authority (4 pts total, 2 each)
            if "q5a" in answers and "q5b" in answers:
                score_a, fb_a = self.grade_answer(answers["q5a"], self.q5_keywords, 20)
                score_b, fb_b = self.grade_answer(answers["q5b"], self.q5_keywords, 20)
                q5_score = (score_a + score_b) * 2
                total_score += q5_score
                feedback.append(
                    f"Q5 ({q5_score:.1f}/4.0): Part A: {fb_a}, Part B: {fb_b}"
                )

            # Question 6: Ethical Challenges (3 pts total, 1.5 each)
            if "q6a" in answers and "q6b" in answers:
                score_a, fb_a = self.grade_answer(answers["q6a"], self.q6_keywords, 15)
                score_b, fb_b = self.grade_answer(answers["q6b"], self.q6_keywords, 15)
                q6_score = (score_a + score_b) * 1.5
                total_score += q6_score
                feedback.append(
                    f"Q6 ({q6_score:.1f}/3.0): Part A: {fb_a}, Part B: {fb_b}"
                )

            percentage = (total_score / max_score) * 100

            return {
                "score": total_score,
                "max_score": max_score,
                "percentage": percentage,
                "feedback": "\n".join(feedback),
                "passed": percentage >= 70,
            }

        except Exception as e:
            return {
                "score": 0,
                "max_score": 20,
                "percentage": 0,
                "feedback": f"Error grading submission: {str(e)}",
                "passed": False,
            }


if __name__ == "__main__":
    grader = Lab01Grader()

    # Test with a sample file if provided
    if len(sys.argv) > 1:
        result = grader.grade_submission(sys.argv[1])
        print(
            f"\nGrade: {result['score']}/{result['max_score']} ({result['percentage']:.1f}%)"
        )
        print(f"Passed: {result['passed']}")
        print(f"\nFeedback:\n{result['feedback']}")
    else:
        grader.run()
