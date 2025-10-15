"""
Canvas API - List All Assignments
Helper script to find assignment IDs for your course
"""

import requests
import json

# ============================================================================
# CONFIGURATION - Update these values
# ============================================================================

CANVAS_API_TOKEN = "YOUR_CANVAS_API_TOKEN_HERE"
CANVAS_DOMAIN = "canvas.instructure.com"
COURSE_ID = "YOUR_COURSE_ID_HERE"

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
    print("\n💡 Copy the assignment ID and paste it into download_lab01_submissions.py")

    # Save to JSON file
    output_file = "assignments_list.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(assignments, f, indent=2)
    print(f"\n✅ Full assignment list saved to: {output_file}")


def main():
    if CANVAS_API_TOKEN == "YOUR_CANVAS_API_TOKEN_HERE":
        print("❌ Error: Please set your CANVAS_API_TOKEN")
        return

    if COURSE_ID == "YOUR_COURSE_ID_HERE":
        print("❌ Error: Please set your COURSE_ID")
        return

    try:
        list_assignments(CANVAS_DOMAIN, CANVAS_API_TOKEN, COURSE_ID)
    except requests.exceptions.RequestException as e:
        print(f"\n❌ API Error: {e}")
        if hasattr(e, "response") and e.response is not None:
            print(f"   Status Code: {e.response.status_code}")
            print(f"   Response: {e.response.text[:200]}")


if __name__ == "__main__":
    main()
