#!/usr/bin/env python3
"""
SIMPLIFIED Lab 3 Parser
Since the JavaScript generates a consistent format, we can use exact label matching
No complex regex needed - just find the labels and grab the values
"""


def parse_lab3_structured(file_path: str) -> dict:
    """
    Parse Lab 3 submission using the known structure from the JavaScript export

    Format is guaranteed by the lab's exportToTextFile() function
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    answers = {}

    # Question 1: Four height values with exact labels
    answers["q1"] = {}
    for height, label in [
        ("22.4", "  Height 22.4 km:"),
        ("16.8", "  Height 16.8 km:"),
        ("11.2", "  Height 11.2 km:"),
        ("5.6", "  Height 5.6 km:"),
    ]:
        if label in content:
            # Get everything after the label until %
            start = content.index(label) + len(label)
            value_str = content[start : start + 20].split("%")[0].strip()
            try:
                answers["q1"][height] = float(value_str)
            except ValueError:
                pass

    # Question 2: Exact label "Answer: Curve "
    label = "  Answer: Curve "
    if label in content:
        start = content.index(label) + len(label)
        answers["q2"] = content[start : start + 1]  # Just grab next character (A/B/C/D)

    # Question 3a-c: Exact labels
    for part, desc in [
        ("a", "a. Cruising airliner"),
        ("b", "b. Mt. Everest"),
        ("c", "c. Denver, CO"),
    ]:
        if desc in content:
            section_start = content.index(desc)
            section = content[section_start : section_start + 200]

            answers[f"q3{part}"] = {}

            # Pressure line: "     Pressure: 220 mb"
            if "     Pressure:" in section:
                start = section.index("     Pressure:") + len("     Pressure:")
                pressure_str = section[start : start + 20].split("mb")[0].strip()
                try:
                    answers[f"q3{part}"]["pressure"] = float(pressure_str)
                except ValueError:
                    pass

            # Percentage line: "     Percentage above: 22%"
            if "     Percentage above:" in section:
                start = section.index("     Percentage above:") + len(
                    "     Percentage above:"
                )
                pct_str = section[start : start + 20].split("%")[0].strip()
                try:
                    answers[f"q3{part}"]["percentage"] = float(pct_str)
                except ValueError:
                    pass

    # Questions 4-6: Station letters
    for q_num, text in [
        (4, "Question 4 (1 pt): Station with highest surface temperature"),
        (5, "Question 5 (1 pt): Station with highest temperature at 10 km"),
        (6, "Question 6 (1 pt): Station with highest temperature at 14 km"),
    ]:
        if text in content:
            section_start = content.index(text)
            section = content[section_start : section_start + 150]
            if "  Answer: Station " in section:
                start = section.index("  Answer: Station ") + len("  Answer: Station ")
                answers[f"q{q_num}"] = (
                    section[start : start + 20].split("\n")[0].strip()
                )

    # Question 7: Inversion layer - 3 values
    if "Question 7 (2 pts): Inversion layer identification" in content:
        section_start = content.index(
            "Question 7 (2 pts): Inversion layer identification"
        )
        section = content[section_start : section_start + 200]

        answers["q7"] = {}

        if "  Color:" in section:
            start = section.index("  Color:") + len("  Color:")
            answers["q7"]["color"] = section[start : start + 20].split("\n")[0].strip()

        if "  Start height:" in section:
            start = section.index("  Start height:") + len("  Start height:")
            height_str = section[start : start + 20].split("km")[0].strip()
            try:
                answers["q7"]["start_height"] = float(height_str)
            except ValueError:
                pass

        if "  End height:" in section:
            start = section.index("  End height:") + len("  End height:")
            height_str = section[start : start + 20].split("km")[0].strip()
            try:
                answers["q7"]["end_height"] = float(height_str)
            except ValueError:
                pass

    # Questions 8-10: Tropopause data
    for q_num, color in [(8, "red"), (9, "blue"), (10, "magenta")]:
        question_text = f"Question {q_num} (2 pts): Tropopause for {color} station"
        if question_text in content:
            section_start = content.index(question_text)
            section = content[section_start : section_start + 150]

            answers[f"q{q_num}"] = {}

            if "  Height:" in section:
                start = section.index("  Height:") + len("  Height:")
                height_str = section[start : start + 20].split("km")[0].strip()
                try:
                    answers[f"q{q_num}"]["height"] = float(height_str)
                except ValueError:
                    pass

            if "  Temperature:" in section:
                start = section.index("  Temperature:") + len("  Temperature:")
                temp_str = section[start : start + 20].split("°C")[0].strip()
                try:
                    answers[f"q{q_num}"]["temperature"] = float(temp_str)
                except ValueError:
                    pass

    # Questions 11-12: Color identification
    for q_num, location in [(11, "Alaska"), (12, "tropics")]:
        question_text = f"Question {q_num} (1 pt): Color plot representing {location}"
        if question_text in content:
            section_start = content.index(question_text)
            section = content[section_start : section_start + 100]
            if "  Answer:" in section:
                start = section.index("  Answer:") + len("  Answer:")
                answers[f"q{q_num}"] = (
                    section[start : start + 20].split("\n")[0].strip()
                )

    # Questions 13-14: Essay responses
    for q_num, text in [
        (13, "Question 13 (3 pts): Tropopause-Temperature Relationship"),
        (14, "Question 14 (3 pts): Atmospheric Variables"),
    ]:
        if text in content:
            section_start = content.index(text) + len(text)
            # Find the next question or end marker
            end_markers = [
                "Question 13",
                "Question 14",
                "PART 5",
                "===",
                "END OF SUBMISSION",
            ]
            next_section = len(content)
            for marker in end_markers:
                marker_pos = content.find(marker, section_start + 10)
                if marker_pos != -1 and marker_pos < next_section:
                    next_section = marker_pos

            essay_text = content[section_start:next_section].strip()
            # Remove [NOT ANSWERED] markers
            if "[NOT ANSWERED]" not in essay_text and essay_text:
                answers[f"q{q_num}"] = essay_text

    return answers


# ==============================================================================
# TEST
# ==============================================================================

if __name__ == "__main__":
    file_path = r"c:\Users\jayma\source\repos\esci240-labs\canvas-api\submissions\lab03\raw\Test_Student_6299\Lab03_AtmosphericAnalysis.txt"

    print("\n" + "=" * 80)
    print("SIMPLIFIED PARSER - Using JavaScript Export Format")
    print("=" * 80 + "\n")

    answers = parse_lab3_structured(file_path)

    print(f"Found {len(answers)} questions:\n")
    for q_id, answer in sorted(answers.items()):
        if isinstance(answer, dict):
            print(f"{q_id}: {answer}")
        elif isinstance(answer, str) and len(answer) > 50:
            print(f"{q_id}: {answer[:50]}...")
        else:
            print(f"{q_id}: {answer}")

    print("\n" + "=" * 80)
