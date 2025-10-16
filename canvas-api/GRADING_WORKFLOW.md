# Canvas API - Grading Workflow & Directory Structure

## Overview

This document describes the recommended organization for downloading submissions, grading them, and uploading scores back to Canvas.

## Complete Workflow

```
1. Download Submissions (Canvas API)
2. Grade Submissions (Automated grading scripts)
3. Review/Adjust Grades (Manual review)
4. Upload Scores (Canvas API)
5. Archive Results (For records)
```

## Recommended Directory Structure

```
canvas-api/
├── submissions/                    # Downloaded submissions (gitignored)
│   ├── lab01/
│   │   ├── raw/                   # Original downloads from Canvas
│   │   │   ├── Test_Student_6299/
│   │   │   │   ├── Lab01_NatureOfScience.txt
│   │   │   │   └── metadata.json
│   │   │   ├── Austin_Aksamit_877/
│   │   │   │   ├── Lab01_NatureOfScience.txt
│   │   │   │   └── metadata.json
│   │   │   └── ...
│   │   ├── graded/                # Grading results
│   │   │   ├── grades.json        # Structured grade data
│   │   │   ├── grades.csv         # Human-readable grades
│   │   │   ├── grading_log.txt    # Grading process log
│   │   │   └── student_reports/   # Individual feedback files
│   │   │       ├── Test_Student_6299_report.txt
│   │   │       ├── Austin_Aksamit_877_report.txt
│   │   │       └── ...
│   │   └── uploaded/              # Upload confirmation
│   │       ├── upload_log.json    # When grades were uploaded
│   │       └── canvas_response.json
│   ├── lab02/
│   │   ├── raw/
│   │   ├── graded/
│   │   └── uploaded/
│   └── ...
│
├── output/                         # API metadata (gitignored)
│   ├── students_list.json
│   ├── students_list.csv
│   └── assignments_list.json
│
├── scripts/                        # Main workflow scripts
│   ├── download_submissions.py    # Generic downloader
│   ├── grade_lab.py              # Grade automation
│   └── upload_grades.py          # Score uploader
│
├── graders/                       # Lab-specific grading logic
│   ├── lab01_grader.py
│   ├── lab02_grader.py
│   └── ...
│
└── archive/                       # Historical records (optional)
    └── 2025-fall/
        └── lab01/
            └── ...
```

## Grading Data Format

### grades.json Structure

```json
{
  "assignment_id": 103762,
  "assignment_name": "Lab 1: Nature of Science",
  "graded_at": "2025-10-15T14:30:00Z",
  "grader_version": "1.0",
  "total_submissions": 31,
  "grades": [
    {
      "student_id": 6299,
      "student_name": "Test Student",
      "canvas_id": 6299,
      "submission_id": 1797215,
      "score": 95.0,
      "max_points": 100.0,
      "percentage": 95.0,
      "status": "graded",
      "feedback": "Excellent work! Minor formatting issues.",
      "grading_details": {
        "question_1": { "points": 20, "max": 20, "feedback": "Perfect" },
        "question_2": { "points": 18, "max": 20, "feedback": "Good reasoning" },
        "formatting": { "points": 7, "max": 10, "feedback": "Missing headers" }
      },
      "flags": [],
      "requires_manual_review": false
    },
    {
      "student_id": 877,
      "student_name": "Austin Aksamit",
      "canvas_id": 877,
      "submission_id": 1797123,
      "score": null,
      "status": "error",
      "error": "File format not recognized",
      "requires_manual_review": true
    }
  ]
}
```

### grades.csv Structure

```csv
Canvas ID,Student Name,Score,Max Points,Percentage,Status,Feedback,Requires Review
6299,Test Student,95.0,100.0,95.0,graded,Excellent work! Minor formatting issues.,FALSE
877,Austin Aksamit,,,0.0,error,File format not recognized,TRUE
```

## Script Organization

### 1. Download Script (`download_submissions.py`)

**Features:**

- Downloads by assignment ID
- Creates `raw/` directory with student folders
- Saves metadata.json for each submission
- Generates download manifest

**Usage:**

```bash
python download_submissions.py --lab 1
python download_submissions.py --assignment-id 103762
```

### 2. Grading Script (`grade_lab.py`)

**Features:**

- Loads submissions from `raw/`
- Calls lab-specific grader (e.g., `graders/lab01_grader.py`)
- Generates grades.json and grades.csv
- Creates individual student reports
- Flags submissions needing manual review

**Usage:**

```bash
python grade_lab.py --lab 1
python grade_lab.py --lab 1 --review-only  # Only grade flagged submissions
```

### 3. Upload Script (`upload_grades.py`)

**Features:**

- Reads grades.json
- Confirms grades before upload
- Uploads scores to Canvas API
- Optionally uploads feedback comments
- Logs all uploads
- Dry-run mode for testing

**Usage:**

```bash
python upload_grades.py --lab 1 --dry-run    # Test without uploading
python upload_grades.py --lab 1              # Actually upload
python upload_grades.py --lab 1 --student-id 6299  # Upload single student
```

## Workflow Example

### Complete Lab 1 Grading Process

```bash
# Step 1: Download all submissions
python download_submissions.py --lab 1

# Step 2: Run automated grading
python grade_lab.py --lab 1

# Step 3: Review flagged submissions manually
# Edit: submissions/lab01/graded/grades.json

# Step 4: Preview grades
python upload_grades.py --lab 1 --dry-run

# Step 5: Upload to Canvas
python upload_grades.py --lab 1

# Step 6: Verify in Canvas
# Check Canvas gradebook to confirm uploads
```

## Benefits of This Structure

### ✅ Separation of Concerns

- **raw/** = Untouched original submissions
- **graded/** = All grading artifacts
- **uploaded/** = Upload confirmation

### ✅ Audit Trail

- Every step is logged
- Can recreate grading decisions
- Upload timestamps preserved

### ✅ Partial Processing

- Can re-grade without re-downloading
- Can upload subset of students
- Can fix individual grades

### ✅ Manual Review Support

- Flags submissions needing attention
- Easy to edit grades.json manually
- Student reports for transparency

### ✅ Automation Ready

- JSON format for programmatic access
- CSV format for Excel/spreadsheet review
- Batch processing support

## Canvas API Endpoints Needed

### For Uploading Grades

```python
# Update submission score
PUT /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}

# Parameters:
{
  "submission": {
    "posted_grade": "95"  # Can be number or letter grade
  },
  "comment": {
    "text_comment": "Excellent work! Minor formatting issues."
  }
}
```

### For Bulk Uploads

```python
# Update multiple submissions at once
POST /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/update_grades

# Parameters:
{
  "grade_data": {
    "6299": {"posted_grade": "95"},
    "877": {"posted_grade": "88"}
  }
}
```

## Security Considerations

### ⚠️ All student data directories are gitignored

```gitignore
# .gitignore
submissions/
output/
archive/
```

### ⚠️ Never commit

- Student submissions
- Grade data
- Student PII (names, IDs, emails)
- Canvas API responses with student data

### ✅ Safe to commit

- Grading scripts
- Configuration templates
- Documentation
- Anonymized test data

## Future Enhancements

1. **Grading UI** - Web interface for manual review
2. **Grade Analytics** - Class statistics, distributions
3. **Partial Credit** - Granular rubric scoring
4. **Plagiarism Detection** - Similarity checking
5. **Late Submission Handling** - Automatic penalties
6. **Grade Curves** - Adjust scores based on distribution
7. **Student Notifications** - Email feedback automatically

## Questions to Consider

1. **Should we download ALL labs at once or one at a time?**

   - Recommendation: One at a time for better organization

2. **Should grading be fully automated or semi-automated?**

   - Recommendation: Automated with manual review flags

3. **Should we upload feedback comments to Canvas?**

   - Recommendation: Yes, students appreciate detailed feedback

4. **How to handle late submissions?**

   - Recommendation: Flag in grading, apply policy in upload script

5. **Should we keep multiple grading attempts?**
   - Recommendation: Yes, version grades.json with timestamps
