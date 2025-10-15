"""
Grader for ESCI 240 Lab 01
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from shared.grader_base import LabGrader


class Lab01Grader(LabGrader):
    """Grader for Lab 01 assignments"""
    
    def __init__(self):
        super().__init__(lab_number=1)
    
    def grade_submission(self, submission_file: str) -> dict:
        """Grade Lab 01 submission"""
        try:
            with open(submission_file, 'r') as f:
                content = f.read()
            
            # Example grading logic - customize for your lab
            score = 0
            feedback = []
            
            if len(content) > 50:
                score += 50
                feedback.append("✓ Adequate length")
            else:
                feedback.append("✗ Response too short")
            
            if "example" in content.lower():  # Replace with actual criteria
                score += 50
                feedback.append("✓ Included key concept")
            else:
                feedback.append("✗ Missing key concept")
            
            return {
                'score': score,
                'feedback': '\n'.join(feedback),
                'passed': score >= 70
            }
            
        except Exception as e:
            return {
                'score': 0,
                'feedback': f'Error grading submission: {str(e)}',
                'passed': False
            }


if __name__ == '__main__':
    grader = Lab01Grader()
    grader.run()