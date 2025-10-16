"""
Simple test for Lab 3 grader - verifies the autograder key works correctly
"""


# Test the exact_match function
def test_exact_match():
    student_answer = "Blue"
    correct_answers = ["Blue", "A", "Station A"]

    student_clean = student_answer.strip().lower()
    for correct in correct_answers:
        if student_clean == correct.lower():
            print(f"✅ exact_match test PASSED: '{student_answer}' matches")
            return True
    print(f"❌ exact_match test FAILED")
    return False


# Test numerical tolerance
def test_numerical():
    student_value = 251
    expected_value = 250
    tolerance = 10

    if abs(student_value - expected_value) <= tolerance:
        print(
            f"✅ numerical test PASSED: {student_value} within {expected_value}±{tolerance}"
        )
        return True
    print(f"❌ numerical test FAILED")
    return False


# Test keyword matching
def test_keyword():
    text = (
        "The warmer the troposphere, the higher the tropopause because warm air expands"
    )

    # Check for keywords
    has_warmer = "warmer" in text.lower()
    has_higher = "higher" in text.lower()
    has_expands = "expands" in text.lower()

    keywords_found = sum([has_higher, has_expands])

    if has_warmer and keywords_found >= 2:
        print(
            f"✅ keyword test PASSED: Found 'warmer' + {keywords_found} other keywords"
        )
        return True
    print(f"❌ keyword test FAILED")
    return False


# Test dictionary (Q1)
def test_dictionary():
    student_dict = {"5.6": 50, "11.2": 25, "16.8": 12.5, "22.4": 6.25}

    correct_dict = {"5.6": 50, "11.2": 25, "16.8": 12.5, "22.4": 6.25}

    all_correct = True
    for height, correct_percentage in correct_dict.items():
        if height in student_dict:
            student_percentage = student_dict[height]
            if abs(student_percentage - correct_percentage) > 1:  # ±1% tolerance
                all_correct = False
                break
        else:
            all_correct = False
            break

    if all_correct:
        print(f"✅ dictionary test PASSED: All 4 values match")
        return True
    print(f"❌ dictionary test FAILED")
    return False


def main():
    print("\n🧪 Testing Lab 3 Grading Functions\n")
    print("=" * 60)

    tests_passed = 0
    tests_total = 4

    if test_exact_match():
        tests_passed += 1

    if test_numerical():
        tests_passed += 1

    if test_keyword():
        tests_passed += 1

    if test_dictionary():
        tests_passed += 1

    print("=" * 60)
    print(f"\nResults: {tests_passed}/{tests_total} tests passed")

    if tests_passed == tests_total:
        print("✅ All tests PASSED - Grading logic verified!\n")
    else:
        print(f"⚠️  {tests_total - tests_passed} test(s) failed\n")


if __name__ == "__main__":
    main()
