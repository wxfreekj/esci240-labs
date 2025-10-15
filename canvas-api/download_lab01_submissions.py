"""
Canvas API - Download Lab 1 Submissions
Downloads all student submissions for Lab 1 from Canvas LMS
"""

import requests
import os
from datetime import datetime
from pathlib import Path
import json

# Load configuration from .env file
try:
    from config import (
        CANVAS_API_TOKEN,
        CANVAS_DOMAIN,
        COURSE_ID,
        LAB_ASSIGNMENT_IDS,
        OUTPUT_BASE_DIR,
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

# Lab 1 specific configuration
LAB_NUMBER = 1
LAB01_ASSIGNMENT_ID = LAB_ASSIGNMENT_IDS.get(LAB_NUMBER)

if not LAB01_ASSIGNMENT_ID:
    print(f"\n⚠️  Warning: LAB0{LAB_NUMBER}_ASSIGNMENT_ID not set in .env file")
    print("\nRun: python list_assignments.py to find assignment IDs")
    LAB01_ASSIGNMENT_ID = None  # Will be validated later

# Output directory for downloaded submissions
OUTPUT_DIR = Path(OUTPUT_BASE_DIR) / f"lab{LAB_NUMBER:02d}_submissions"

# ============================================================================
# Canvas API Functions
# ============================================================================


class CanvasAPI:
    def __init__(self, domain, token):
        self.base_url = f"https://{domain}/api/v1"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def get_paginated(self, endpoint, params=None):
        """
        Handle Canvas API pagination to get all results
        """
        all_items = []
        url = f"{self.base_url}/{endpoint}"

        while url:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()

            items = response.json()
            all_items.extend(items)

            # Check for next page in Link header
            links = response.links
            url = links.get("next", {}).get("url")
            params = None  # Params are included in the next URL

        return all_items

    def get_assignment(self, course_id, assignment_id):
        """
        Get assignment details
        """
        endpoint = f"courses/{course_id}/assignments/{assignment_id}"
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_submissions(self, course_id, assignment_id):
        """
        Get all submissions for an assignment
        """
        endpoint = f"courses/{course_id}/assignments/{assignment_id}/submissions"
        params = {"include[]": ["user", "submission_comments"], "per_page": 100}
        return self.get_paginated(endpoint, params)

    def download_attachment(self, url, output_path):
        """
        Download a file attachment from Canvas
        """
        response = requests.get(url, headers=self.headers, stream=True)
        response.raise_for_status()

        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        return output_path


# ============================================================================
# Submission Download Functions
# ============================================================================


def sanitize_filename(name):
    """
    Remove invalid characters from filenames
    """
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        name = name.replace(char, "_")
    return name


def format_student_name(user):
    """
    Format student name for folder/file naming
    """
    name = user.get("sortable_name", user.get("name", "Unknown"))
    # Convert "Last, First" to "First_Last"
    if ", " in name:
        last, first = name.split(", ", 1)
        name = f"{first}_{last}"
    return sanitize_filename(name.replace(" ", "_"))


def download_lab01_submissions(canvas, course_id, assignment_id, output_dir):
    """
    Download all Lab 1 submissions
    """
    print("=" * 80)
    print("Canvas API - Lab 1 Submission Downloader")
    print("=" * 80)

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n📁 Output directory: {output_dir.absolute()}")

    # Get assignment details
    print(f"\n🔍 Fetching assignment details...")
    assignment = canvas.get_assignment(course_id, assignment_id)
    print(f"   Assignment: {assignment['name']}")
    print(f"   Points: {assignment.get('points_possible', 'N/A')}")

    # Get all submissions
    print(f"\n📥 Fetching submissions...")
    submissions = canvas.get_submissions(course_id, assignment_id)
    print(f"   Found {len(submissions)} total submission records")

    # Filter for submitted assignments
    submitted = [
        s for s in submissions if s.get("workflow_state") in ["submitted", "graded"]
    ]
    print(f"   {len(submitted)} students have submitted")

    # Download each submission
    print(f"\n💾 Downloading submissions...")
    downloaded_count = 0
    skipped_count = 0

    # Create a metadata file
    metadata = {
        "assignment_name": assignment["name"],
        "assignment_id": assignment_id,
        "download_date": datetime.now().isoformat(),
        "submissions": [],
    }

    for submission in submitted:
        user = submission.get("user", {})
        student_name = format_student_name(user)
        student_id = user.get("id", "unknown")

        # Create student folder
        student_dir = output_dir / f"{student_name}_{student_id}"
        student_dir.mkdir(exist_ok=True)

        submission_info = {
            "student_name": user.get("name"),
            "student_id": student_id,
            "submitted_at": submission.get("submitted_at"),
            "score": submission.get("score"),
            "grade": submission.get("grade"),
            "files": [],
        }

        # Download attachments
        attachments = submission.get("attachments", [])
        if attachments:
            for attachment in attachments:
                filename = sanitize_filename(attachment.get("filename", "file.txt"))
                file_path = student_dir / filename

                try:
                    download_url = attachment.get("url")
                    canvas.download_attachment(download_url, file_path)
                    print(f"   ✓ {student_name}: {filename}")

                    submission_info["files"].append(
                        {
                            "filename": filename,
                            "size": attachment.get("size"),
                            "content_type": attachment.get("content-type"),
                        }
                    )

                    downloaded_count += 1
                except Exception as e:
                    print(f"   ✗ {student_name}: Failed to download {filename} - {e}")
        else:
            # Handle text submissions
            if submission.get("submission_type") == "online_text_entry":
                text_content = submission.get("body", "")
                text_file = student_dir / f"{student_name}_text_submission.html"
                text_file.write_text(text_content, encoding="utf-8")
                print(f"   ✓ {student_name}: text_submission.html")

                submission_info["files"].append(
                    {"filename": text_file.name, "type": "text_entry"}
                )

                downloaded_count += 1
            else:
                print(f"   ⊘ {student_name}: No files attached")
                skipped_count += 1

        # Save submission metadata
        metadata["submissions"].append(submission_info)

    # Write metadata file
    metadata_file = output_dir / "submissions_metadata.json"
    with open(metadata_file, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    # Summary
    print("\n" + "=" * 80)
    print("📊 Download Summary")
    print("=" * 80)
    print(f"   Total submissions: {len(submitted)}")
    print(f"   Files downloaded: {downloaded_count}")
    print(f"   Skipped (no files): {skipped_count}")
    print(f"   Output location: {output_dir.absolute()}")
    print(f"   Metadata file: {metadata_file.name}")
    print("\n✅ Download complete!")


# ============================================================================
# Main Execution
# ============================================================================


def main():
    # Validate configuration
    if not LAB01_ASSIGNMENT_ID:
        print("❌ Error: LAB01_ASSIGNMENT_ID not set in .env file")
        print("\nTo find your assignment ID:")
        print("1. Run: python list_assignments.py")
        print("2. Find 'Lab 1' in the output")
        print("3. Copy the assignment ID")
        print("4. Add to .env file: LAB01_ASSIGNMENT_ID=your_id_here")
        return

    try:
        # Initialize Canvas API
        canvas = CanvasAPI(CANVAS_DOMAIN, CANVAS_API_TOKEN)

        # Download submissions
        download_lab01_submissions(canvas, COURSE_ID, LAB01_ASSIGNMENT_ID, OUTPUT_DIR)

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
