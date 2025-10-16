# ESCI 240 Labs - Directory Cleanup & Integration Plan

## Current State Analysis

### What You Have:

1. **`grading-system/`** - Existing grading infrastructure

   - `lab01/grader.py` - Working Lab 1 grader with keyword matching
   - `shared/grader_base.py` - Base class for all lab graders
   - `lab02/` through `lab10/` - Empty directories (ready for future graders)

2. **`canvas-api/`** - NEW Canvas API integration

   - Download scripts (list_students, download_lab01_submissions)
   - Configuration system (.env, config.py)
   - Workflow documentation (GRADING_WORKFLOW.md)

3. **Duplicate/Messy Directories:**
   - `output/` in root (student data - WRONG LOCATION)
   - `canvas-api/output/` (correct location)
   - `downloads/` in root (empty)
   - `canvas-api/downloads/` (empty)

## Recommended Integration

### Option A: Merge into Single System (RECOMMENDED)

Move grading logic into canvas-api structure:

```
canvas-api/
├── downloads/                      # Scripts to download from Canvas
│   ├── list_students.py
│   ├── list_assignments.py
│   └── download_submissions.py    # Generic downloader
│
├── graders/                        # Lab-specific grading logic (MOVE FROM grading-system/)
│   ├── __init__.py
│   ├── base_grader.py             # Moved from grading-system/shared/grader_base.py
│   ├── lab01_grader.py            # Moved from grading-system/lab01/grader.py
│   ├── lab02_grader.py
│   └── ...
│
├── uploads/                        # Scripts to upload grades to Canvas
│   ├── upload_grades.py
│   └── bulk_upload.py
│
├── submissions/                    # Downloaded submissions (gitignored)
│   ├── lab01/
│   │   ├── raw/                   # Original downloads
│   │   ├── graded/                # Grading results
│   │   └── uploaded/              # Upload confirmation
│   └── ...
│
├── output/                         # API metadata (gitignored)
│   ├── students_list.json
│   ├── students_list.csv
│   └── assignments_list.json
│
├── config.py                       # Configuration loader
├── .env                           # Credentials (gitignored)
├── .env.example                   # Template
├── README.md                      # Main documentation
└── GRADING_WORKFLOW.md            # Workflow guide
```

**Benefits:**

- Everything Canvas-related in one place
- Clear separation: downloads → grade → upload
- Existing Lab 1 grader can be integrated immediately

### Option B: Keep Separate (Current Structure)

Keep grading-system/ separate but integrate:

```
grading-system/              # Grading logic ONLY
└── (keep as-is)

canvas-api/                  # Canvas integration ONLY
├── downloads/
├── uploads/
├── submissions/
└── output/
```

**Integration via imports:**

```python
# In canvas-api/grade_lab.py
import sys
sys.path.append('../grading-system')
from lab01.grader import Lab01Grader
```

**Drawbacks:**

- More complex imports
- Two separate "systems" to maintain
- Confusing where things go

## Cleanup Actions

### 1. Fix Duplicate Directories

```powershell
# Move student data to correct location
Move-Item output/* canvas-api/output/
Remove-Item output/

# Remove empty directories
Remove-Item downloads/
Remove-Item canvas-api/downloads/
```

### 2. Integrate Grading System (Option A)

```powershell
# Create new structure
New-Item -ItemType Directory canvas-api/graders
New-Item -ItemType Directory canvas-api/downloads
New-Item -ItemType Directory canvas-api/uploads

# Move grading code
Move-Item grading-system/shared/grader_base.py canvas-api/graders/base_grader.py
Move-Item grading-system/lab01/grader.py canvas-api/graders/lab01_grader.py

# Move download scripts
Move-Item canvas-api/list_students.py canvas-api/downloads/
Move-Item canvas-api/list_assignments.py canvas-api/downloads/
Move-Item canvas-api/download_lab01_submissions.py canvas-api/downloads/

# Keep utility scripts in root
# - config.py (stays in canvas-api/)
# - check_submission.py (stays in canvas-api/)
```

### 3. Update Imports

After moving files, update import statements:

```python
# In canvas-api/graders/lab01_grader.py
from .base_grader import LabGrader  # Updated import
```

### 4. Remove Old Structure

```powershell
# After confirming everything works
Remove-Item grading-system/ -Recurse
```

## File Relocation Summary

### Move to `canvas-api/downloads/`:

- ✅ list_students.py
- ✅ list_assignments.py
- ✅ download_lab01_submissions.py

### Move to `canvas-api/graders/`:

- ✅ grading-system/shared/grader_base.py → base_grader.py
- ✅ grading-system/lab01/grader.py → lab01_grader.py

### Create in `canvas-api/uploads/`:

- ⏳ upload_grades.py (new)
- ⏳ bulk_upload.py (new)

### Keep in `canvas-api/` root:

- ✅ config.py
- ✅ check_submission.py
- ✅ README.md
- ✅ GRADING_WORKFLOW.md
- ✅ .env, .env.example, .gitignore

### Delete:

- ❌ output/ (root level - move contents first)
- ❌ downloads/ (root level - empty)
- ❌ canvas-api/downloads/ (empty - will recreate as subdirectory)
- ❌ grading-system/ (after moving contents)

## Updated Workflow

After cleanup:

```bash
# 1. Download submissions
cd canvas-api/downloads
python download_submissions.py --lab 1

# 2. Grade submissions
cd ../graders
python grade_lab.py --lab 1

# 3. Upload grades
cd ../uploads
python upload_grades.py --lab 1
```

Or use a master script:

```bash
# All-in-one
cd canvas-api
python run_grading_workflow.py --lab 1
```

## Next Steps

1. **Decide:** Option A (merge) or Option B (keep separate)
2. **Backup:** Commit current state before restructuring
3. **Execute:** Run cleanup script
4. **Test:** Verify Lab 1 grader still works
5. **Document:** Update README with new structure

## My Recommendation

**Use Option A (Merge)**:

- Simpler mental model
- One place for all Canvas operations
- Easier to maintain
- Better organization for future labs

The `grading-system/` folder was a good start but it makes more sense to have everything Canvas-related together in `canvas-api/`.
