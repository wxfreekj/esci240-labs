#!/usr/bin/env python3
"""
Test the Lab 3 grader with sample data
"""
import sys
import os
import re
from typing import Dict, List, Tuple, Any

# Copy the key classes to avoid Canvas import issues during testing

# AUTOGRADER KEY (copied from grade_lab03_ai.py)
AUTOGRADER_KEY = {
    "q1": {
        "points": 2,
        "type": "dictionary",
        "answers": {"5.6": 50, "11.2": 25, "16.8": 12.5, "22.4": 6.25},
    },
    "q2": {"points": 3, "type": "exact_match", "answers": ["Curve B", "B"]},
    "q3a": {
        "points": 2,
        "type": "numerical_pair",
        "answers": {
            "pressure": {"value": 250, "tolerance": 10},
            "percentage": {"value": 25, "tolerance": 1},
        },
    },
    "q3b": {
        "points": 2,
        "type": "numerical_pair",
        "answers": {
            "pressure": {"value": 330, "tolerance": 10},
            "percentage": {"value": 33, "tolerance": 2},
        },
    },
    "q3c": {
        "points": 2,
        "type": "numerical_pair",
        "answers": {
            "pressure": {"value": 820, "tolerance": 15},
            "percentage": {"value": 82, "tolerance": 2},
        },
    },
    "q4": {
        "points": 1,
        "type": "exact_match",
        "answers": ["C", "magenta", "Station C"],
    },
    "q5": {
        "points": 1,
        "type": "exact_match",
        "answers": ["C", "magenta", "Station C"],
    },
    "q6": {
        "points": 1,
        "type": "exact_match",
        "answers": ["A", "B", "blue", "red", "Station A", "Station B"],
    },
    "q7": {
        "points": 2,
        "type": "multipart",
        "answers": {
            "color": ["Blue", "A"],
            "start_height": {"value": 11, "tolerance": 0.5},
            "end_height": {"value": 20, "tolerance": 1.0},
        },
    },
    "q8": {
        "points": 2,
        "type": "numerical_pair",
        "answers": {
            "height": {"value": 11, "tolerance": 0.5},
            "temperature": {"value": -55, "tolerance": 3},
        },
    },
    "q9": {
        "points": 2,
        "type": "numerical_pair",
        "answers": {
            "height": {"value": 9, "tolerance": 0.5},
            "temperature": {"value": -55, "tolerance": 3},
        },
    },
    "q10": {
        "points": 2,
        "type": "numerical_pair",
        "answers": {
            "height": {"value": 16, "tolerance": 0.5},
            "temperature": {"value": -75, "tolerance": 3},
        },
    },
    "q11": {"points": 1, "type": "exact_match", "answers": ["Blue", "A", "Station A"]},
    "q12": {
        "points": 1,
        "type": "exact_match",
        "answers": ["Magenta", "C", "Station C", "purple"],
    },
    "q13": {
        "points": 3,
        "type": "keyword",
        "scoring": {
            "full_credit": {
                "require_all": [],
                "require_any": ["warmer", "colder"],
                "count_minimum": 3,
                "keywords": [
                    "higher",
                    "lower",
                    "expands",
                    "contracts",
                    "temperature",
                    "height",
                ],
            },
            "partial_credit": {
                "require_all": [],
                "require_any": ["warmer", "colder"],
                "count_minimum": 2,
                "keywords": ["higher", "lower"],
            },
        },
    },
    "q14": {
        "points": 3,
        "type": "keyword",
        "scoring": {
            "full_credit": {
                "require_all": ["weight", "less air"],
                "require_any": ["gravity", "density", "compress"],
                "count_minimum": 0,
                "keywords": [],
            },
            "partial_credit": {
                "require_all": [],
                "require_any": ["weight", "less air"],
                "count_minimum": 0,
                "keywords": [],
            },
        },
    },
}

# Import the classes from the grader
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from grade_lab03_ai import Lab3Parser, Lab3Grader

# Sample submission data for testing
SAMPLE_SUBMISSION = """
Lab 3: Temperature, Pressure, and Density

Question 1: Complete the table showing percentage of atmosphere above each height

Height (km) | Percentage Above
5.6         | 50%
11.2        | 25%
16.8        | 12.5%
22.4        | 6.25%

Question 2: Which curve represents exponential decrease?
Answer: Curve B

Question 3a: Cruising airliner at 11 km
Pressure: 250 mb
Percentage: 25%

Question 3b: Mt. Everest at 8.85 km
Pressure: 330 mb
Percentage: 33%

Question 3c: Denver at 1.6 km
Pressure: 820 mb
Percentage: 82%

Question 4: Highest surface temperature
Answer: Station C (Magenta)

Question 5: Highest temperature at 10 km
Answer: C

Question 6: Highest temperature at 14 km
Answer: Blue

Question 7: Inversion layer
Color: Blue
Start height: 11 km
End height: 20 km

Question 8: Red station tropopause
Height: 11 km
Temperature: -55°C

Question 9: Blue station tropopause
Height: 9 km
Temperature: -55°C

Question 10: Magenta station tropopause
Height: 16 km
Temperature: -75°C

Question 11: Which station is Alaska?
Answer: Blue (Station A)

Question 12: Which station is tropics?
Answer: Magenta

Question 13: Relationship between tropospheric temperature and tropopause height
The warmer the average temperature in the troposphere, the higher the tropopause. 
This is because warmer air expands and takes up more vertical space, making the 
troposphere thicker. Colder regions like Alaska have a lower tropopause.

Question 14: How do pressure, density, and temperature vary with height?
Air pressure decreases with height because there is less weight of air above. 
Density also decreases because there is less air to compress the atmosphere. 
Temperature generally decreases due to gravity and the lapse rate.
"""


def test_parser():
    """Test the parser"""
    print("=" * 60)
    print("TESTING PARSER")
    print("=" * 60)

    # Create a temp file
    test_file = "test_submission.txt"
    with open(test_file, "w") as f:
        f.write(SAMPLE_SUBMISSION)

    parser = Lab3Parser()
    answers = parser.parse_submission(test_file)

    print(f"\nParsed {len(answers)} questions:")
    for q_id, answer in sorted(answers.items()):
        print(f"\n{q_id}: {answer}")

    # Cleanup
    os.remove(test_file)

    return answers


def test_grader(answers):
    """Test the grader"""
    print("\n" + "=" * 60)
    print("TESTING GRADER")
    print("=" * 60)

    grader = Lab3Grader(AUTOGRADER_KEY)
    total_score, detailed_results = grader.grade_submission(answers)

    print(f"\nDetailed Results:")
    for q_id in sorted(detailed_results.keys()):
        result = detailed_results[q_id]
        print(f"\n{q_id.upper()}: {result['score']:.1f}/{result['max_points']}")
        print(f"   Feedback: {result['feedback']}")

    print(f"\n{'='*60}")
    print(f"TOTAL SCORE: {total_score:.1f}/30")
    percentage = (total_score / 30) * 100
    print(f"PERCENTAGE: {percentage:.1f}%")
    print(f"{'='*60}")

    return total_score


def main():
    print("\n🧪 Testing Lab 3 Autograder\n")

    # Test parser
    answers = test_parser()

    # Test grader
    total_score = test_grader(answers)

    # Expected score
    expected_score = 30.0  # Perfect submission

    print(f"\n{'='*60}")
    if total_score == expected_score:
        print(f"✅ TEST PASSED - Score matches expected: {expected_score}/30")
    else:
        print(
            f"⚠️  TEST RESULT - Score: {total_score}/30 (Expected: {expected_score}/30)"
        )
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
