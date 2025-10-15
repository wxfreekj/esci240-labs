"""
Canvas API Configuration Loader
Loads configuration from .env file using python-dotenv
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from the canvas-api directory
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)


def get_required_env(key, error_msg=None):
    """
    Get a required environment variable or raise an error
    """
    value = os.getenv(key)
    if not value or value.startswith("your_"):
        msg = error_msg or f"Missing required environment variable: {key}"
        raise ValueError(msg)
    return value


def get_optional_env(key, default=None):
    """
    Get an optional environment variable with a default value
    """
    return os.getenv(key, default)


# Load Canvas API configuration
try:
    CANVAS_API_TOKEN = get_required_env(
        "CANVAS_API_TOKEN",
        "CANVAS_API_TOKEN not set in .env file. See .env.example for setup instructions.",
    )

    CANVAS_DOMAIN = get_required_env(
        "CANVAS_DOMAIN",
        "CANVAS_DOMAIN not set in .env file (e.g., canvas.instructure.com)",
    )

    COURSE_ID = get_required_env(
        "CANVAS_COURSE_ID",
        "CANVAS_COURSE_ID not set in .env file. Find it in your Canvas course URL.",
    )

    # Optional: Output directories
    OUTPUT_BASE_DIR = Path(get_optional_env("OUTPUT_BASE_DIR", "./submissions"))
    ASSIGNMENTS_OUTPUT_FILE = Path(
        get_optional_env("ASSIGNMENTS_OUTPUT_FILE", "./output/assignments_list.json")
    )

    # Ensure output directories exist
    OUTPUT_BASE_DIR.mkdir(parents=True, exist_ok=True)
    ASSIGNMENTS_OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Lab assignment IDs (optional - can be set as needed)
    LAB_ASSIGNMENT_IDS = {
        1: os.getenv("LAB01_ASSIGNMENT_ID"),
        2: os.getenv("LAB02_ASSIGNMENT_ID"),
        3: os.getenv("LAB03_ASSIGNMENT_ID"),
        4: os.getenv("LAB04_ASSIGNMENT_ID"),
        5: os.getenv("LAB05_ASSIGNMENT_ID"),
        6: os.getenv("LAB06_ASSIGNMENT_ID"),
        7: os.getenv("LAB07_ASSIGNMENT_ID"),
        8: os.getenv("LAB08_ASSIGNMENT_ID"),
        9: os.getenv("LAB09_ASSIGNMENT_ID"),
        10: os.getenv("LAB10_ASSIGNMENT_ID"),
    }

    # Remove None values
    LAB_ASSIGNMENT_IDS = {k: v for k, v in LAB_ASSIGNMENT_IDS.items() if v}

except ValueError as e:
    print(f"\n❌ Configuration Error: {e}")
    print("\n📝 Setup Instructions:")
    print("1. Copy .env.example to .env:")
    print("   cp .env.example .env")
    print("\n2. Edit .env and fill in your Canvas credentials")
    print("\n3. Run list_assignments.py to find assignment IDs")
    print()
    raise

# Export configuration
__all__ = [
    "CANVAS_API_TOKEN",
    "CANVAS_DOMAIN",
    "COURSE_ID",
    "OUTPUT_BASE_DIR",
    "ASSIGNMENTS_OUTPUT_FILE",
    "LAB_ASSIGNMENT_IDS",
]
