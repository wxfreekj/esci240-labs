# Lab 3: Temperature, Pressure, and Density - Reference Material

## Lab Overview

**Title**: Temperature, Pressure, and Density in the Atmosphere  
**Points**: 30 points total  
**Format**: Numerical calculations + graph analysis + short answer  
**Lab URL**: https://wxfreekj.github.io/lab03-student/

## Grading Approach

**Hybrid Grading System**:

- **Questions 1-12** (24 pts): Rule-based automatic grading with numerical tolerance
- **Questions 13-14** (6 pts): AI-based grading for conceptual explanations

---

## Part 1: Atmospheric Mass Distribution (5 pts)

### Question 1: Complete the table (2 pts)

**Key Rule**: Atmospheric mass halves every 5.6 km

**Expected Answers**:
| Height (km) | Percentage Above | Calculation |
|-------------|------------------|-------------|
| 22.4 | 6.25% | 100% × (1/2)^4 |
| 16.8 | 12.5% | 100% × (1/2)^3 |
| 11.2 | 25% | 100% × (1/2)^2 |
| 5.6 | 50% | 100% × (1/2)^1 |
| 0 | 100% | Sea Level |

**Grading**:

- 0.5 pts per correct answer (4 values)
- Accept ±1% tolerance (e.g., 6.25% ± 1% = 5.25-7.25%)
- Common errors: 6%, 12%, 25%, 50% (accept these)

---

### Question 2: Select the correct curve (3 pts)

**Instructions**: Which curve represents exponential decrease of atmospheric mass?

**Expected Answer**: Will vary based on image, but looking for:

- Exponential decay curve (not linear)
- Curve that shows rapid decrease initially, then slower decrease
- Typically labeled as one option (A, B, C, or D)

**Grading**:

- 3 pts: Correct curve selected
- 0 pts: Wrong curve
- **Note**: Need to verify correct answer from actual graph

---

## Part 2: Barometric Pressure at Different Altitudes (6 pts)

### Key Formula

Pressure ≈ 1000 mb × (1/2)^(height/5.6 km)  
Percentage ≈ 100% × (1/2)^(height/5.6 km)

### Question 3a: Cruising airliner at 11 km (2 pts)

**Calculation**:

- Height: 11 km = 2 × 5.6 km
- Pressure: 1000 × (1/2)^2 = 1000 × 0.25 = **250 mb**
- Percentage: 100 × (1/2)^2 = **25%**

**Grading**:

- 1 pt: Pressure within 225-275 mb
- 1 pt: Percentage within 22-28%

---

### Question 3b: Mt. Everest at 8.85 km (2 pts)

**Calculation**:

- Height: 8.85 km = 1.58 × 5.6 km
- Pressure: 1000 × (1/2)^1.58 ≈ 1000 × 0.334 = **334 mb**
- Percentage: 100 × (1/2)^1.58 ≈ **33.4%**

**Grading**:

- 1 pt: Pressure within 300-370 mb
- 1 pt: Percentage within 30-37%

**Accept**: 340 mb, 34% (rounded)

---

### Question 3c: Denver, CO at 1.6 km (2 pts)

**Calculation**:

- Height: 1.6 km = 0.286 × 5.6 km
- Pressure: 1000 × (1/2)^0.286 ≈ 1000 × 0.820 = **820 mb**
- Percentage: 100 × (1/2)^0.286 ≈ **82%**

**Grading**:

- 1 pt: Pressure within 780-860 mb
- 1 pt: Percentage within 78-86%

**Accept**: 800-850 mb, 80-85% (reasonable estimates)

---

## Part 3: Atmospheric Lapse Rate (0 pts - informational)

**Standard Lapse Rate**: 6.5°C per km  
**Surface Temperature**: 15°C  
**Formula**: T(h) = 15°C - (6.5°C/km × h)

_No questions in this section, but used for Part 4_

---

## Part 4: Atmospheric Temperature Profiles (13 pts)

### Questions 4-6: Surface and Upper Atmosphere Temps (3 pts)

**From Temperature Profile Graph**:

- Three stations: Blue, Red, Magenta
- Typical pattern:
  - **Tropics (warmest surface)**: Usually highest at surface
  - **Standard atmosphere**: Middle
  - **Alaska (coldest surface)**: Lowest at surface
  - **At stratosphere**: Order often reverses

**Expected Answers** (based on typical profiles):

**Q4: Highest surface temperature** (1 pt)

- Expected: Station with warmest surface (likely Red or Magenta - tropics)
- **Grading**: Exact color match required

**Q5: Highest temperature at 10 km** (1 pt)

- Expected: Station with highest tropopause (likely tropics)
- **Grading**: Exact color match required

**Q6: Highest temperature at 14 km** (1 pt)

- Expected: Station in stratosphere (often coldest at surface = warmest at 14km)
- **Grading**: Exact color match required

---

### Question 7: Inversion Layer (2 pts)

**Temperature Inversion**: Layer where temperature increases with height

**Expected Answer**:

- **Color**: One of Blue/Red/Magenta
- **Start height**: X km (where temp starts increasing)
- **End height**: Y km (where temp stops increasing or reaches tropopause)

**Grading**:

- 1 pt: Correct color
- 0.5 pt: Start height ±0.5 km
- 0.5 pt: End height ±0.5 km

**Common Answer**: Blue (Alaska) often has surface inversion 0-1 km

---

### Questions 8-10: Tropopause Identification (6 pts)

**Tropopause**: Height where temperature stops decreasing (becomes isothermal or increases)

**Q8: Red station tropopause** (2 pts)

- 1 pt: Height (read from graph) ±0.5 km
- 1 pt: Temperature (read from graph) ±2°C

**Q9: Blue station tropopause** (2 pts)

- 1 pt: Height ±0.5 km
- 1 pt: Temperature ±2°C

**Q10: Magenta station tropopause** (2 pts)

- 1 pt: Height ±0.5 km
- 1 pt: Temperature ±2°C

**Typical Values**:

- Tropics: ~16 km, ~-75°C
- Standard: ~11 km, ~-56°C
- Polar/Alaska: ~9 km, ~-45°C

---

### Questions 11-12: Location Identification (2 pts)

**Q11: Alaska** (1 pt)

- Expected: Blue (lowest tropopause, coldest surface typically)
- **Grading**: Exact color match

**Q12: Tropics** (1 pt)

- Expected: Red or Magenta (highest tropopause, warmest surface)
- **Grading**: Exact color match

---

## Part 5: Analysis and Synthesis (6 pts - AI GRADED)

### Question 13: Tropopause-Temperature Relationship (3 pts)

**Prompt**: "What relationship do you see between average tropospheric temperature and the height of the tropopause?"

**Expected Concepts**:

1. **Direct/positive relationship**: Warmer troposphere → higher tropopause
2. **Inverse/negative relationship**: Colder troposphere → lower tropopause
3. **Mechanism** (bonus): Warmer air expands, making troposphere thicker

**Grading Rubric**:

- 3 pts: Clearly states warmer temps = higher tropopause with explanation
- 2-2.5 pts: Identifies relationship but lacks clarity or completeness
- 1-1.5 pts: Vague reference to relationship
- 0-0.5 pts: Incorrect or missing

**Example Excellent Answer**:

> "There is a direct relationship between tropospheric temperature and tropopause height. Warmer average temperatures in the troposphere result in a higher tropopause. This is because warmer air expands and occupies more vertical space, making the troposphere thicker. The tropics have the warmest troposphere and highest tropopause (~16 km), while polar regions have colder troposphere and lower tropopause (~9 km)."

**Example Good Answer**:

> "Warmer tropospheric temperatures lead to a higher tropopause. The tropics have a higher tropopause than Alaska because it's warmer."

**Example Poor Answer**:

> "Temperature affects the tropopause."

---

### Question 14: Atmospheric Variables (3 pts)

**Prompt**: "In your own words, describe how air pressure, density, and temperature vary with height in the troposphere."

**Expected Concepts**:

1. **Pressure**: Decreases with height (exponentially)
2. **Density**: Decreases with height (less air above)
3. **Temperature**: Decreases with height (lapse rate of ~6.5°C/km)

**Grading Rubric**:

- 3 pts: Correctly describes all three variables with direction of change
- 2-2.5 pts: Correctly describes 2 of 3 variables
- 1-1.5 pts: Correctly describes 1 variable or vague description
- 0-0.5 pts: Incorrect or missing

**Example Excellent Answer**:

> "In the troposphere, all three variables decrease with height. Air pressure decreases because there is less atmosphere above pushing down. Air density decreases because molecules spread out at lower pressure. Temperature decreases at an average rate of 6.5°C per kilometer due to the lapse rate, making it colder as you go higher."

**Example Good Answer**:

> "Pressure, density, and temperature all decrease as you go higher in the troposphere. There is less air pushing down at higher altitudes."

**Example Poor Answer**:

> "They all change with height."

---

## Implementation Notes for Grader

### Rule-Based Questions (1-12)

**Numerical Tolerance**:

```python
def check_numerical(student_answer, expected, tolerance_percent=5):
    try:
        student_val = float(student_answer)
        tolerance = expected * (tolerance_percent / 100)
        return abs(student_val - expected) <= tolerance
    except:
        return False
```

**String Matching** (colors, curves):

```python
def check_exact_match(student_answer, expected, case_sensitive=False):
    if not case_sensitive:
        return student_answer.strip().lower() == expected.lower()
    return student_answer.strip() == expected
```

### AI-Graded Questions (13-14)

Use existing `AIGrader` with specific rubrics for each question.

**Confidence Thresholds**:

- Auto-approve if score ≥ 90% AND confidence ≥ 0.85
- Flag for review if score < 70% OR confidence < 0.7

---

## Answer Key Template

```json
{
  "q1": {
    "22.4km": 6.25,
    "16.8km": 12.5,
    "11.2km": 25,
    "5.6km": 50
  },
  "q2": "B",
  "q3a": { "pressure": 250, "percentage": 25 },
  "q3b": { "pressure": 334, "percentage": 33.4 },
  "q3c": { "pressure": 820, "percentage": 82 },
  "q4": "red",
  "q5": "red",
  "q6": "blue",
  "q7": { "color": "blue", "start": 0, "end": 1 },
  "q8": { "height": 16, "temp": -75 },
  "q9": { "height": 9, "temp": -45 },
  "q10": { "height": 11, "temp": -56 },
  "q11": "blue",
  "q12": "red",
  "q13": "AI_GRADED",
  "q14": "AI_GRADED"
}
```

---

## Common Student Errors

1. **Q1**: Using addition instead of halving (50%, 25%, 12.5%, 6.25%)
2. **Q3**: Forgetting to interpolate between 5.6 km intervals
3. **Q7**: Identifying stratosphere instead of surface inversion
4. **Q8-10**: Reading wrong axis or misidentifying tropopause
5. **Q13**: Stating inverse relationship instead of direct
6. **Q14**: Only describing one or two variables

---

## Grading Workflow

1. **Parse submission** file (Lab03_AtmosphericAnalysis.txt)
2. **Grade Q1-Q12** automatically with rule-based checker
3. **Grade Q13-Q14** with AI using specific rubrics
4. **Calculate total score** (24 pts + 6 pts = 30 pts)
5. **Flag for review** if:
   - Total score < 21/30 (70%)
   - Any AI question confidence < 0.7
   - Numerical answers outside tolerance ranges
6. **Generate feedback** for each question

---

## Testing Data Needed

To finalize answer key, need to verify from actual lab image:

- Q2: Which curve is correct (A, B, C, or D)?
- Q4-Q6: Which color has highest temps at each altitude?
- Q7: Which station has inversion and at what heights?
- Q8-10: Exact tropopause heights and temps from graph

**Recommendation**: Use Test Student submission to validate answer key.
