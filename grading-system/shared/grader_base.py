"""
Base class for ESCI 240 lab graders
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any
import os
from dotenv import load_dotenv

load_dotenv('config/.env')


class LabGrader(ABC):
    """Base class for grading lab assignments"""
    
    def __init__(self, lab_number: int):
        self.lab_number = lab_number
        self.canvas_api_url = os.getenv('CANVAS_API_URL')
        self.canvas_api_key = os.getenv('CANVAS_API_KEY')
        self.course_id = os.getenv('COURSE_ID')
    
    @abstractmethod
    def grade_submission(self, submission_file: str) -> Dict[str, Any]:
        """
        Grade a single submission file
        
        Args:
            submission_file: Path to the student's submission
            
        Returns:
            Dictionary with 'score', 'feedback', and 'passed' keys
        """
        pass
    
    def fetch_submissions(self) -> List[Dict]:
        """Fetch submissions from Canvas API"""
        # TODO: Implement Canvas API integration
        print(f"Fetching submissions for Lab {self.lab_number}")
        return []
    
    def post_grade(self, student_id: str, score: float, feedback: str):
        """Post grade and feedback to Canvas"""
        # TODO: Implement Canvas API integration
        print(f"Posting grade for student {student_id}: {score}")
        print(f"Feedback: {feedback}")
    
    def run(self):
        """Main grading workflow"""
        print(f"Starting grading for ESCI 240 Lab {self.lab_number}")
        submissions = self.fetch_submissions()
        
        for submission in submissions:
            result = self.grade_submission(submission['file'])
            self.post_grade(
                submission['student_id'],
                result['score'],
                result['feedback']
            )