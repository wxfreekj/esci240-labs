#!/usr/bin/env python3
"""
Simple, readable parser for Lab 3 - with explanations
Shows why we need pattern matching
"""


def parse_lab3_simple(file_path):
    """Parse Lab 3 without complex regex - just simple string operations"""

    with open(file_path, "r") as f:
        content = f.read()

    answers = {}

    # ========================================================================
    # Q1: Find the table section
    # ========================================================================
    # Strategy: Find "Question 1" then grab the next 4 lines with percentages

    lines = content.split("\n")

    for i, line in enumerate(lines):
        if "Question 1" in line:
            # Found Q1, now look at next few lines
            q1_data = {}
            for j in range(i + 1, min(i + 10, len(lines))):  # Look ahead 10 lines max
                if "km:" in lines[j] and "%" in lines[j]:
                    # Extract: "  Height 22.4 km: 6.25%"
                    parts = lines[j].split("km:")
                    if len(parts) == 2:
                        height = parts[0].strip().split()[-1]  # Get "22.4"
                        percentage = parts[1].strip().replace("%", "")  # Get "6.25"
                        q1_data[height] = float(percentage)

            if q1_data:
                answers["q1"] = q1_data
                print(f"✓ Q1 found: {q1_data}")
            break

    # ========================================================================
    # Q2: Find "Answer: Curve B"
    # ========================================================================
    # Strategy: Find line with "Question 2", then find line with "Answer:"

    for i, line in enumerate(lines):
        if "Question 2" in line:
            # Look at next few lines for the answer
            for j in range(i + 1, min(i + 5, len(lines))):
                if "Answer:" in lines[j] and "Curve" in lines[j]:
                    # Extract: "  Answer: Curve B"
                    answer_part = lines[j].split("Curve")[-1].strip()
                    if answer_part and answer_part[0] in "ABCD":
                        answers["q2"] = answer_part[0]
                        print(f"✓ Q2 found: {answer_part[0]}")
            break

    # ========================================================================
    # Q3: Find pressure/percentage pairs
    # ========================================================================
    # Strategy: Find "a. Cruising", then grab next lines with Pressure/Percentage

    for part, keyword in [("a", "Cruising"), ("b", "Everest"), ("c", "Denver")]:
        for i, line in enumerate(lines):
            if keyword in line and (f"{part}." in line or f"Question 3{part}" in line):
                # Found the subsection, now extract data
                pressure = None
                percentage = None

                for j in range(i, min(i + 5, len(lines))):
                    if "Pressure:" in lines[j]:
                        # Extract: "     Pressure: 220 mb"
                        pressure_str = lines[j].split("Pressure:")[1].strip().split()[0]
                        pressure = float(pressure_str)

                    if "Percentage" in lines[j]:
                        # Extract: "     Percentage above: 22%"
                        pct_str = lines[j].split(":")[-1].strip().replace("%", "")
                        percentage = float(pct_str)

                if pressure and percentage:
                    answers[f"q3{part}"] = {
                        "pressure": pressure,
                        "percentage": percentage,
                    }
                    print(f"✓ Q3{part} found: {pressure} mb, {percentage}%")
                break

    # ========================================================================
    # Q4-6: Simple exact matches
    # ========================================================================

    question_map = {
        4: "highest surface temperature",
        5: "highest temperature at 10 km",
        6: "highest temperature at 14 km",
    }

    for q_num, keyword in question_map.items():
        for i, line in enumerate(lines):
            if f"Question {q_num}" in line:
                # Look at next few lines for "Answer: Station C"
                for j in range(i + 1, min(i + 5, len(lines))):
                    if "Answer:" in lines[j] or "Station" in lines[j]:
                        # Extract station letter or color
                        answer = lines[j].split(":")[-1].strip()
                        answers[f"q{q_num}"] = answer
                        print(f"✓ Q{q_num} found: {answer}")
                        break
                break

    # ========================================================================
    # Q13-14: Essay questions - just grab everything until next question
    # ========================================================================

    for q_num in [13, 14]:
        for i, line in enumerate(lines):
            if f"Question {q_num}" in line:
                # Collect lines until we hit next question or end
                essay_lines = []
                for j in range(i + 1, len(lines)):
                    if "Question" in lines[j] or "===" in lines[j]:
                        break
                    if lines[j].strip():  # Skip blank lines
                        essay_lines.append(lines[j].strip())

                if essay_lines:
                    answers[f"q{q_num}"] = " ".join(essay_lines)
                    print(f"✓ Q{q_num} found: {answers[f'q{q_num}'][:50]}...")
                break

    return answers


# ============================================================================
# Test it
# ============================================================================

if __name__ == "__main__":
    import sys

    file_path = r"c:\Users\jayma\source\repos\esci240-labs\canvas-api\submissions\lab03\raw\Test_Student_6299\Lab03_AtmosphericAnalysis.txt"

    print("\n" + "=" * 80)
    print("SIMPLE PARSER (No Complex Regex)")
    print("=" * 80 + "\n")

    answers = parse_lab3_simple(file_path)

    print("\n" + "=" * 80)
    print(f"RESULTS: Found {len(answers)} questions")
    print("=" * 80 + "\n")

    for q_id, answer in sorted(answers.items()):
        print(f"{q_id}: {answer}")
