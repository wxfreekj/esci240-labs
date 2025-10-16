# Manual Cleanup Steps for ESCI 240 Labs

## Current Issues:

1. `output/` in root contains student data (should be in canvas-api/output/)
2. `downloads/` directories are empty and should be removed
3. `grading-system/` should be integrated into `canvas-api/`

## Manual Cleanup Commands:

```powershell
# Navigate to project root
cd C:\Users\jayma\source\repos\esci240-labs

# Step 1: Move student data from root output/ to canvas-api/output/
Move-Item output\* canvas-api\output\ -Force
Remove-Item output\

# Step 2: Remove empty downloads directories
Remove-Item downloads\ -Force
Remove-Item canvas-api\downloads\ -Force

# Step 3: Create new structure in canvas-api
New-Item -ItemType Directory -Path canvas-api\downloads
New-Item -ItemType Directory -Path canvas-api\graders
New-Item -ItemType Directory -Path canvas-api\uploads

# Step 4: Move grading system into canvas-api
Move-Item grading-system\shared\grader_base.py canvas-api\graders\base_grader.py -Force
Move-Item grading-system\lab01\grader.py canvas-api\graders\lab01_grader.py -Force

# Step 5: Organize canvas-api scripts
Move-Item canvas-api\list_students.py canvas-api\downloads\ -Force
Move-Item canvas-api\list_assignments.py canvas-api\downloads\ -Force
Move-Item canvas-api\download_lab01_submissions.py canvas-api\downloads\ -Force

# Step 6: Create __init__.py files
Set-Content canvas-api\graders\__init__.py "# ESCI 240 Lab Graders`n"
Set-Content canvas-api\downloads\__init__.py "# Canvas API Download Scripts`n"

# Step 7: Clean up empty grading-system
Remove-Item grading-system\ -Recurse -Force

# Step 8: Check results
git status
```

## Or Run the Automated Script:

```powershell
.\cleanup_and_integrate.ps1
# Type 'yes' when prompted
```

## Result Structure:

```
canvas-api/
├── downloads/
│   ├── __init__.py
│   ├── list_students.py
│   ├── list_assignments.py
│   └── download_lab01_submissions.py
│
├── graders/
│   ├── __init__.py
│   ├── base_grader.py
│   └── lab01_grader.py
│
├── uploads/
│   └── (empty - ready for upload scripts)
│
├── submissions/
│   └── (student data - gitignored)
│
├── output/
│   ├── students_list.json
│   ├── students_list.csv
│   └── assignments_list.json
│
├── config.py
├── check_submission.py
├── README.md
├── GRADING_WORKFLOW.md
├── .env (gitignored)
├── .env.example
└── .gitignore
```
