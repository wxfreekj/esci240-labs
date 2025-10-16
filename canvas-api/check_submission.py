"""
Canvas API - Check Specific Submission
Checks if a specific student has submitted to a specific assignment
"""

import requests
import json
from datetime import datetime

# Load configuration from .env file
try:
    from config import (
        CANVAS_API_TOKEN,
        CANVAS_DOMAIN,
        COURSE_ID,
    )
except ImportError as e:
    print("\n❌ Configuration Error!")
    print("\n📝 Setup Instructions:")
    print("1. Copy .env.example to .env:")
    print("   cp .env.example .env")
    print("\n2. Edit .env and fill in your Canvas credentials")
    print("\n3. Install python-dotenv:")
    print("   pip install python-dotenv")
    print()
    raise


class CanvasAPI:
    def __init__(self, domain, token):
        self.domain = domain
        self.token = token
        self.headers = {"Authorization": f"Bearer {token}"}
        self.base_url = f"https://{domain}/api/v1"

    def get_submission(self, course_id, assignment_id, student_id):
        """Get a specific submission for a student"""
        url = f"{self.base_url}/courses/{course_id}/assignments/{assignment_id}/submissions/{student_id}"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                return None
            raise


def format_date(date_str):
    """Format ISO date string to readable format"""
    if not date_str:
        return "N/A"
    try:
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d %I:%M %p")
    except:
        return date_str


def check_submission(assignment_id, student_id):
    """Check for a specific submission"""

    print("=" * 80)
    print("Canvas Submission Check")
    print("=" * 80)
    print(f"Course ID: {COURSE_ID}")
    print(f"Assignment ID: {assignment_id}")
    print(f"Student Canvas ID: {student_id}")
    print()

    # Initialize Canvas API
    api = CanvasAPI(CANVAS_DOMAIN, CANVAS_API_TOKEN)

    print("🔍 Checking for submission...")
    submission = api.get_submission(COURSE_ID, assignment_id, student_id)

    if submission is None:
        print("\n❌ No submission found!")
        print("\nPossible reasons:")
        print("  • Student is not enrolled in the course")
        print("  • Assignment ID is incorrect")
        print("  • Student has not submitted yet")
        return None

    print("\n✅ Submission found!")
    print("-" * 80)

    # Basic submission info
    print(f"\n📋 Submission Details:")
    print(f"   Workflow State: {submission.get('workflow_state', 'N/A')}")
    print(f"   Submitted: {'Yes' if submission.get('submitted_at') else 'No'}")

    if submission.get("submitted_at"):
        print(f"   Submitted At: {format_date(submission.get('submitted_at'))}")

    if submission.get("graded_at"):
        print(f"   Graded At: {format_date(submission.get('graded_at'))}")

    print(f"   Late: {'Yes' if submission.get('late') else 'No'}")
    print(f"   Missing: {'Yes' if submission.get('missing') else 'No'}")

    # Score info
    if submission.get("score") is not None:
        print(f"\n📊 Grading:")
        print(f"   Score: {submission.get('score')}")
        print(f"   Grade: {submission.get('grade', 'N/A')}")

    # Submission type and content
    print(f"\n📝 Submission Type: {submission.get('submission_type', 'N/A')}")

    if submission.get("attempt"):
        print(f"   Attempt: {submission.get('attempt')}")

    # Attachments
    attachments = submission.get("attachments", [])
    if attachments:
        print(f"\n📎 Attachments ({len(attachments)}):")
        for i, attachment in enumerate(attachments, 1):
            print(f"   {i}. {attachment.get('filename', 'Unknown')}")
            print(f"      Size: {attachment.get('size', 0):,} bytes")
            print(f"      URL: {attachment.get('url', 'N/A')}")

    # URL submission
    if submission.get("url"):
        print(f"\n🔗 URL: {submission.get('url')}")

    # Body/text submission
    if submission.get("body"):
        print(f"\n📄 Text Submission:")
        body = submission.get("body", "")
        if len(body) > 200:
            print(f"   {body[:200]}...")
            print(f"   (Truncated - {len(body)} characters total)")
        else:
            print(f"   {body}")

    print("\n" + "=" * 80)
    print("📊 Raw JSON Data")
    print("=" * 80)
    print(json.dumps(submission, indent=2))

    return submission


if __name__ == "__main__":
    # Configuration
    ASSIGNMENT_ID = 103762  # Assignment to check
    STUDENT_ID = 6299  # Student Canvas ID to check

    print("\n" + "=" * 80)
    print("Checking for specific submission...")
    print("=" * 80)

    submission = check_submission(ASSIGNMENT_ID, STUDENT_ID)

    print("\n✅ Check complete!")
