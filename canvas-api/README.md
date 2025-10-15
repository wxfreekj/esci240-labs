# Canvas API - Submission Downloader

Scripts to download student submissions from Canvas LMS for ESCI 240 labs.

## 📋 Prerequisites

- Python 3.7 or higher
- Canvas LMS access with instructor/TA permissions
- Canvas API access token

## 🔧 Setup

### 1. Install Required Packages

```bash
pip install requests python-dotenv
```

Or install from the main requirements file:

```bash
pip install -r ../requirements.txt
```

### 2. Create Your Configuration File

Copy the example environment file:

```bash
cd canvas-api
cp .env.example .env
```

### 3. Get Your Canvas API Token

1. Log in to Canvas
2. Click on **Account** (left menu)
3. Click on **Settings**
4. Scroll down to **Approved Integrations**
5. Click **+ New Access Token**
6. Enter a purpose (e.g., "Lab Submission Downloader")
7. Set expiration date (optional)
8. Click **Generate Token**
9. **Copy the token immediately** (you won't see it again!)

### 4. Edit Your .env File

Open `.env` in a text editor and fill in:

```bash
# Your Canvas API token from step 3
CANVAS_API_TOKEN=paste_your_token_here

# Your Canvas domain (e.g., canvas.instructure.com)
CANVAS_DOMAIN=canvas.instructure.com

# Your course ID (see next step)
CANVAS_COURSE_ID=123456
```

### 5. Find Your Course ID

1. Go to your ESCI 240 course in Canvas
2. Look at the URL in your browser:
   ```
   https://yourschool.instructure.com/courses/123456
                                              ^^^^^^
                                            This is your Course ID
   ```
3. Copy the number after `courses/` and add it to `.env`

### 6. Find Assignment IDs

Run the helper script to list all assignments:

```bash
python list_assignments.py
```

This will display all assignments with their IDs. Look for "Lab 1", "Lab 2", etc. and copy their IDs.

Add the assignment IDs to your `.env` file:

```bash
LAB01_ASSIGNMENT_ID=789012
LAB02_ASSIGNMENT_ID=789013
LAB03_ASSIGNMENT_ID=789014
# ... etc for all 10 labs
```

## 📥 Download Lab 1 Submissions

### 1. Verify Configuration

Make sure your `.env` file has:
- `CANVAS_API_TOKEN`
- `CANVAS_DOMAIN`
- `CANVAS_COURSE_ID`
- `LAB01_ASSIGNMENT_ID`

### 2. Run the Download

```bash
python download_lab01_submissions.py
```

### 3. Check the Output

Submissions will be downloaded to:

```
./lab01_submissions/
├── John_Doe_12345/
│   └── Lab01_NatureOfScience.txt
├── Jane_Smith_67890/
│   └── Lab01_NatureOfScience.txt
└── submissions_metadata.json
```

Each student gets their own folder named: `FirstName_LastName_StudentID`

## 📊 Output Structure

### Student Folders

- Named: `FirstName_LastName_StudentID`
- Contains all submitted files
- Preserves original filenames

### Metadata File

`submissions_metadata.json` contains:

- Assignment details
- Download timestamp
- List of all submissions with:
  - Student name and ID
  - Submission timestamp
  - Score/grade
  - List of downloaded files

## 🔍 Troubleshooting

### "Unauthorized" Error

- Check that your API token is correct
- Verify you have instructor/TA access to the course
- Make sure the token hasn't expired

### "Not Found" Error

- Verify the Course ID is correct
- Verify the Assignment ID is correct
- Check that the assignment exists and is published

### "No files attached"

- Some students may have submitted text instead of files
- Text submissions are saved as HTML files
- Check the student's folder for `text_submission.html`

### Rate Limiting

- Canvas API has rate limits
- The script includes pagination to handle large classes
- If you hit limits, wait a few minutes and try again

## 🚀 Next Steps

### Create Scripts for Other Labs

You can duplicate `download_lab01_submissions.py` and modify it for other labs:

```bash
cp download_lab01_submissions.py download_lab02_submissions.py
```

Then edit and change:

- `LAB01_ASSIGNMENT_ID` → `LAB02_ASSIGNMENT_ID`
- `OUTPUT_DIR = Path("./lab01_submissions")` → `Path("./lab02_submissions")`

### Batch Download All Labs

Create a script that downloads all 10 labs at once (coming soon).

## 📚 Canvas API Documentation

- [Canvas LMS REST API Documentation](https://canvas.instructure.com/doc/api/)
- [Submissions API](https://canvas.instructure.com/doc/api/submissions.html)
- [Assignments API](https://canvas.instructure.com/doc/api/assignments.html)

## ⚠️ Security Notes

- **Never commit your API token to Git!**
- Add `canvas-api/.env` to `.gitignore` if you use environment variables
- Keep your token secure like a password
- Revoke tokens when no longer needed

## 💡 Tips

1. **Test with one lab first** before downloading all labs
2. **Back up submissions** regularly
3. **Use the metadata file** to track who submitted what
4. **Check file sizes** - large files may take longer to download
5. **Organize downloads** by lab number and date

## 📝 Example Workflow

```bash
# 1. List all assignments to find IDs
python list_assignments.py

# 2. Download Lab 1 submissions
python download_lab01_submissions.py

# 3. Check the downloads
ls lab01_submissions/

# 4. Review metadata
cat lab01_submissions/submissions_metadata.json | python -m json.tool
```

## 🆘 Need Help?

- Check Canvas API documentation
- Review the metadata JSON file for debugging
- Check Canvas submission page to verify what students uploaded
- Contact Canvas support for API access issues
