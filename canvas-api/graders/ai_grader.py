"""
AI Grading Engine for ESCI 240 Labs
Uses OpenAI API (ChatGPT) to grade subjective responses
"""

import os
import json
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
import openai


@dataclass
class GradingCriteria:
    """Criteria for grading a single question"""

    name: str
    description: str
    points: int


@dataclass
class GradingResult:
    """Result from AI grading"""

    points_earned: int
    points_possible: int
    percentage: float
    feedback: str
    criteria_scores: Dict[str, int]  # criterion name -> points earned
    confidence: float  # AI's confidence in the grade (0-1)
    flagged_for_review: bool
    review_reason: Optional[str] = None


class AIGrader:
    """AI-powered grading using OpenAI API"""

    def __init__(
        self,
        api_key: str,
        model: str = "gpt-4o-mini",
        temperature: float = 0.3,
        auto_approve_threshold: float = 90.0,
        grading_instructions_path: Optional[str] = None,
        reference_material_path: Optional[str] = None,
    ):
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.auto_approve_threshold = auto_approve_threshold

        # Load grading instructions if provided
        self.grading_instructions = None
        if grading_instructions_path and os.path.exists(grading_instructions_path):
            with open(grading_instructions_path, "r", encoding="utf-8") as f:
                self.grading_instructions = f.read()

        # Load reference material if provided
        self.reference_material = None
        if reference_material_path and os.path.exists(reference_material_path):
            with open(reference_material_path, "r", encoding="utf-8") as f:
                self.reference_material = f.read()

    def grade_response(
        self,
        question_prompt: str,
        student_response: str,
        criteria: List[GradingCriteria],
        reference_answer: Optional[str] = None,
        context: Optional[str] = None,
    ) -> GradingResult:
        """
        Grade a single student response using AI

        Args:
            question_prompt: The question asked
            student_response: Student's answer
            criteria: List of grading criteria
            reference_answer: Optional model/example answer
            context: Optional additional context (readings, lecture notes)

        Returns:
            GradingResult with score and feedback
        """

        # Build the grading prompt
        system_prompt = self._build_system_prompt()
        user_prompt = self._build_grading_prompt(
            question_prompt, student_response, criteria, reference_answer, context
        )

        # Call OpenAI API
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=self.temperature,
                response_format={"type": "json_object"},
            )

            # Parse the response
            result_json = json.loads(response.choices[0].message.content)

            return self._parse_grading_result(result_json, criteria)

        except Exception as e:
            # If AI grading fails, flag for human review
            total_points = sum(c.points for c in criteria)
            return GradingResult(
                points_earned=0,
                points_possible=total_points,
                percentage=0.0,
                feedback=f"AI grading failed: {str(e)}",
                criteria_scores={},
                confidence=0.0,
                flagged_for_review=True,
                review_reason=f"AI grading error: {str(e)}",
            )

    def _build_system_prompt(self) -> str:
        """Build the system prompt for the AI grader"""
        base_prompt = """You are an expert college-level Earth Science instructor grading student responses for ESCI 240 (Introduction to Meteorology and Climate).

Your role is to:
1. Evaluate student responses based on the provided grading criteria and reference material
2. Assign points for each criterion based on how well the student addressed it
3. Provide constructive, specific feedback
4. Be fair but rigorous in your assessment
5. Recognize correct concepts even if wording is imperfect
6. Flag responses that seem plagiarized, AI-generated, or require human review

Grading philosophy:
- Award full points if the student demonstrates understanding of key concepts
- Award partial credit for partially correct or incomplete answers
- Be generous with points if the student shows effort and understanding
- Don't penalize for minor grammar/spelling errors unless they obscure meaning
- Consider the level of the course (introductory undergraduate)
- Use the provided reference material and grading instructions as your guide

You must respond with valid JSON in this exact format:
{
  "criteria_scores": {
    "criterion_name": points_earned,
    ...
  },
  "total_points_earned": number,
  "confidence": 0-1 float,
  "feedback": "detailed feedback string",
  "concerns": ["list of any concerns for human review"],
  "strength_summary": "what the student did well",
  "improvement_summary": "what could be improved"
}"""

        # Append grading instructions if available
        if self.grading_instructions:
            base_prompt += f"\n\nGRADING INSTRUCTIONS:\n{self.grading_instructions}"

        return base_prompt

    def _build_grading_prompt(
        self,
        question: str,
        response: str,
        criteria: List[GradingCriteria],
        reference_answer: Optional[str],
        context: Optional[str],
    ) -> str:
        """Build the user prompt with question and grading criteria"""

        prompt = f"""Grade the following student response.

QUESTION:
{question}

STUDENT RESPONSE:
{response}

GRADING CRITERIA:
Total Points: {sum(c.points for c in criteria)}

"""

        for criterion in criteria:
            prompt += f"- {criterion.name} ({criterion.points} points): {criterion.description}\n"

        # Add reference material if available
        if self.reference_material:
            prompt += f"\nREFERENCE MATERIAL (from lab assignment and required reading):\n{self.reference_material}\n"

        if reference_answer:
            prompt += f"\nREFERENCE ANSWER (for comparison):\n{reference_answer}\n"

        if context:
            prompt += f"\nADDITIONAL CONTEXT:\n{context}\n"

        prompt += """

Evaluate the response and provide:
1. Points earned for each criterion (use the reference material to validate accuracy)
2. Your confidence in this grade (0-1, where 1 is very confident)
3. Specific, constructive feedback (reference the source material when helpful)
4. Any concerns that warrant human review
5. Summary of strengths and areas for improvement

Remember: Be fair and generous with partial credit. The goal is education, not punishment. Use the reference material to ensure accuracy and consistency in grading."""

        return prompt

    def _parse_grading_result(
        self, result_json: Dict[str, Any], criteria: List[GradingCriteria]
    ) -> GradingResult:
        """Parse the AI's JSON response into a GradingResult"""

        points_earned = result_json.get("total_points_earned", 0)
        total_points = sum(c.points for c in criteria)
        percentage = (points_earned / total_points * 100) if total_points > 0 else 0

        confidence = result_json.get("confidence", 0.5)
        concerns = result_json.get("concerns", [])

        # Build comprehensive feedback
        feedback_parts = []
        if result_json.get("strength_summary"):
            feedback_parts.append(f"✓ Strengths: {result_json['strength_summary']}")
        if result_json.get("improvement_summary"):
            feedback_parts.append(
                f"→ Areas for improvement: {result_json['improvement_summary']}"
            )
        if result_json.get("feedback"):
            feedback_parts.append(f"\nDetailed feedback: {result_json['feedback']}")

        feedback = "\n\n".join(feedback_parts)

        # Determine if should be flagged for review
        flagged = False
        review_reason = None

        if concerns:
            flagged = True
            review_reason = f"AI flagged concerns: {'; '.join(concerns)}"
        elif confidence < 0.7:
            flagged = True
            review_reason = f"Low AI confidence ({confidence:.0%})"
        elif percentage < self.auto_approve_threshold and percentage > 0:
            flagged = True
            review_reason = f"Score below auto-approve threshold ({percentage:.1f}% < {self.auto_approve_threshold}%)"

        return GradingResult(
            points_earned=points_earned,
            points_possible=total_points,
            percentage=percentage,
            feedback=feedback,
            criteria_scores=result_json.get("criteria_scores", {}),
            confidence=confidence,
            flagged_for_review=flagged,
            review_reason=review_reason,
        )

    def grade_multi_part_question(
        self,
        question_prompt: str,
        parts: Dict[str, str],  # part_id -> student_response
        criteria_per_part: Dict[str, List[GradingCriteria]],
        reference_answers: Optional[Dict[str, str]] = None,
        context: Optional[str] = None,
    ) -> Dict[str, GradingResult]:
        """
        Grade a multi-part question

        Returns:
            Dictionary mapping part_id to GradingResult
        """
        results = {}

        for part_id, response in parts.items():
            criteria = criteria_per_part.get(part_id, [])
            ref_answer = reference_answers.get(part_id) if reference_answers else None

            results[part_id] = self.grade_response(
                f"{question_prompt} - Part {part_id.upper()}",
                response,
                criteria,
                ref_answer,
                context,
            )

        return results


def load_ai_grader_from_env(
    grading_instructions_path: Optional[str] = None,
    reference_material_path: Optional[str] = None,
) -> AIGrader:
    """Load AI grader with settings from environment variables"""

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set in .env file")

    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    temperature = float(os.getenv("AI_GRADING_TEMPERATURE", "0.3"))
    threshold = float(os.getenv("AI_AUTO_APPROVE_THRESHOLD", "90"))

    return AIGrader(
        api_key=api_key,
        model=model,
        temperature=temperature,
        auto_approve_threshold=threshold,
        grading_instructions_path=grading_instructions_path,
        reference_material_path=reference_material_path,
    )


# Example usage
if __name__ == "__main__":
    # This is an example of how to use the AI grader

    from dotenv import load_dotenv

    load_dotenv()

    grader = load_ai_grader_from_env()

    # Example: Grade a response about assumptions in science
    criteria = [
        GradingCriteria(
            name="Identifies naturalism",
            description="Correctly identifies that science studies natural phenomena",
            points=3,
        ),
        GradingCriteria(
            name="Explains uniformity",
            description="Explains that natural laws are consistent across universe",
            points=3,
        ),
    ]

    result = grader.grade_response(
        question_prompt="List two assumptions in science.",
        student_response="""Science can't answer every kind of question (like questions about ultimate purpose or the supernatural). Science also assumes that the universe is, as its name implies, a vast single system in which the basic rules are everywhere the same.""",
        criteria=criteria,
        reference_answer="1. Naturalism - science studies only natural phenomena; 2. Uniformity - natural laws are consistent throughout the universe",
    )

    print(
        f"Points: {result.points_earned}/{result.points_possible} ({result.percentage:.1f}%)"
    )
    print(f"Confidence: {result.confidence:.0%}")
    print(f"Flagged: {result.flagged_for_review}")
    if result.flagged_for_review:
        print(f"Reason: {result.review_reason}")
    print(f"\nFeedback:\n{result.feedback}")
