"""
Canvas API - List All Assignments
Helper script to find assignment IDs for your course
"""

import requests
import json

# Load configuration from .env file
try:
    from config import (
        CANVAS_API_TOKEN,
        CANVAS_DOMAIN,
        COURSE_ID,
        ASSIGNMENTS_OUTPUT_FILE,
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

# ============================================================================


def list_assignments(domain, token, course_id):
    """
    List all assignments in the course
    """
    base_url = f"https://{domain}/api/v1"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    print("=" * 80)
    print("Canvas Course Assignments")
    print("=" * 80)
    print(f"Course ID: {course_id}\n")

    # Get all assignments
    url = f"{base_url}/courses/{course_id}/assignments"
    params = {"per_page": 100}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    assignments = response.json()

    # Group by lab number
    labs = {}
    other = []

    for assignment in assignments:
        name = assignment["name"]
        if "Lab" in name or "lab" in name:
            # Try to extract lab number
            import re

            match = re.search(r"[Ll]ab\s*(\d+)", name)
            if match:
                lab_num = int(match.group(1))
                labs[lab_num] = assignment
            else:
                other.append(assignment)
        else:
            other.append(assignment)

    # Print lab assignments in order
    if labs:
        print("📚 Lab Assignments:")
        print("-" * 80)
        for lab_num in sorted(labs.keys()):
            assignment = labs[lab_num]
            print(f"\n   Lab {lab_num:02d}: {assignment['name']}")
            print(f"   ID: {assignment['id']}")
            print(f"   Points: {assignment.get('points_possible', 'N/A')}")
            print(f"   Due: {assignment.get('due_at', 'No due date')}")

    # Print other assignments
    if other:
        print("\n\n📋 Other Assignments:")
        print("-" * 80)
        for assignment in other:
            print(f"\n   {assignment['name']}")
            print(f"   ID: {assignment['id']}")
            print(f"   Points: {assignment.get('points_possible', 'N/A')}")

    print("\n" + "=" * 80)
    print("\n💡 Copy the assignment ID and add it to your .env file")

    # Save to JSON file in output directory
    with open(ASSIGNMENTS_OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(assignments, f, indent=2)
    print(f"\n✅ Full assignment list saved to: {ASSIGNMENTS_OUTPUT_FILE}")


def main():
    # Configuration is loaded from .env via config.py
    # No additional validation needed here since config.py handles it

    try:
        list_assignments(CANVAS_DOMAIN, CANVAS_API_TOKEN, COURSE_ID)
    except requests.exceptions.RequestException as e:
        print(f"\n❌ API Error: {e}")
        if hasattr(e, "response") and e.response is not None:
            print(f"   Status Code: {e.response.status_code}")
            print(f"   Response: {e.response.text[:200]}")


if __name__ == "__main__":
    main()
