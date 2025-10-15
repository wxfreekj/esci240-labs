"""
Canvas API Configuration Template

1. Copy this file to 'config.py': cp config.template.py config.py
2. Edit config.py with your actual values
3. config.py is in .gitignore and won't be committed to Git

This keeps your API token secure!
"""

# Your Canvas API access token
# Get from: Canvas > Account > Settings > New Access Token
CANVAS_API_TOKEN = "YOUR_CANVAS_API_TOKEN_HERE"

# Your Canvas domain (without https://)
# Examples:
#   - "canvas.instructure.com"
#   - "yourschool.instructure.com"
#   - "mycollege.canvas.com"
CANVAS_DOMAIN = "canvas.instructure.com"

# Your ESCI 240 course ID
# Find in course URL: https://canvas.../courses/COURSE_ID
COURSE_ID = "YOUR_COURSE_ID_HERE"

# Assignment IDs for each lab
# Run list_assignments.py to find these
LAB_ASSIGNMENT_IDS = {
    1: "YOUR_LAB01_ASSIGNMENT_ID",
    2: "YOUR_LAB02_ASSIGNMENT_ID",
    3: "YOUR_LAB03_ASSIGNMENT_ID",
    4: "YOUR_LAB04_ASSIGNMENT_ID",
    5: "YOUR_LAB05_ASSIGNMENT_ID",
    6: "YOUR_LAB06_ASSIGNMENT_ID",
    7: "YOUR_LAB07_ASSIGNMENT_ID",
    8: "YOUR_LAB08_ASSIGNMENT_ID",
    9: "YOUR_LAB09_ASSIGNMENT_ID",
    10: "YOUR_LAB10_ASSIGNMENT_ID",
}

# Base directory for downloaded submissions
OUTPUT_BASE_DIR = "./downloads"
