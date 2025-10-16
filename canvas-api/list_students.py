"""
Canvas API - List Students
Retrieves all students enrolled in the course
"""

import requests
import json
import csv
from pathlib import Path

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

# Output file path
STUDENTS_OUTPUT_DIR = ASSIGNMENTS_OUTPUT_FILE.parent
STUDENTS_JSON_FILE = STUDENTS_OUTPUT_DIR / "students_list.json"
STUDENTS_CSV_FILE = STUDENTS_OUTPUT_DIR / "students_list.csv"

# ============================================================================


def get_students(domain, token, course_id):
    """
    Get all students enrolled in the course
    """
    base_url = f"https://{domain}/api/v1"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    print("=" * 80)
    print("Canvas Course Students")
    print("=" * 80)
    print(f"Course ID: {course_id}\n")

    # Get all students (active enrollments only)
    students = []
    url = f"{base_url}/courses/{course_id}/users"
    params = {
        "enrollment_type[]": "student",
        "enrollment_state[]": ["active", "invited", "completed"],
        "per_page": 100,
    }

    print("📥 Fetching student list from Canvas...")

    while url:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        page_students = response.json()
        students.extend(page_students)

        # Check for next page in Link header
        links = response.links
        url = links.get("next", {}).get("url")
        params = None  # Params are included in the next URL

    print(f"   Found {len(students)} students\n")

    # Display student list
    print("👥 Enrolled Students:")
    print("-" * 80)

    # Sort by sortable_name (Last, First)
    students_sorted = sorted(students, key=lambda x: x.get("sortable_name", ""))

    for i, student in enumerate(students_sorted, 1):
        name = student.get("name", "Unknown")
        sortable_name = student.get("sortable_name", "Unknown")
        student_id = student.get("id")
        email = student.get("email", "No email")
        sis_id = student.get("sis_user_id", "N/A")

        print(f"\n{i:3d}. {sortable_name}")
        print(f"     Canvas ID: {student_id}")
        print(f"     SIS ID: {sis_id}")
        print(f"     Email: {email}")

    print("\n" + "=" * 80)

    # Save to JSON file
    print(f"\n💾 Saving student list...")
    with open(STUDENTS_JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(students_sorted, f, indent=2)
    print(f"   ✅ JSON saved to: {STUDENTS_JSON_FILE}")

    # Save to CSV file (simplified format)
    csv_data = []
    for student in students_sorted:
        csv_data.append(
            {
                "Canvas ID": student.get("id"),
                "SIS ID": student.get("sis_user_id", ""),
                "Name": student.get("name", ""),
                "Sortable Name": student.get("sortable_name", ""),
                "Email": student.get("email", ""),
                "Login ID": student.get("login_id", ""),
            }
        )

    with open(STUDENTS_CSV_FILE, "w", newline="", encoding="utf-8") as f:
        if csv_data:
            writer = csv.DictWriter(f, fieldnames=csv_data[0].keys())
            writer.writeheader()
            writer.writerows(csv_data)
    print(f"   ✅ CSV saved to: {STUDENTS_CSV_FILE}")

    # Summary
    print("\n" + "=" * 80)
    print("📊 Summary")
    print("=" * 80)
    print(f"   Total students: {len(students)}")
    print(f"   JSON output: {STUDENTS_JSON_FILE.name}")
    print(f"   CSV output: {STUDENTS_CSV_FILE.name}")
    print("\n✅ Complete!")


def main():
    # Configuration is loaded from .env via config.py
    # No additional validation needed here since config.py handles it

    try:
        get_students(CANVAS_DOMAIN, CANVAS_API_TOKEN, COURSE_ID)
    except requests.exceptions.RequestException as e:
        print(f"\n❌ API Error: {e}")
        if hasattr(e, "response") and e.response is not None:
            print(f"   Status Code: {e.response.status_code}")
            print(f"   Response: {e.response.text[:200]}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
