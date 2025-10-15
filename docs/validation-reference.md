# Lab Input Validation Reference

This document lists all form inputs across all labs, their validation requirements, and error messages.

---

## Lab 1: Nature of Science

### Questions (All Textareas)

| Question ID | Question Text                                             | Validation        | Error Message            |
| ----------- | --------------------------------------------------------- | ----------------- | ------------------------ |
| `q1`        | What is science?                                          | Min 20 characters | "Q1 - needs more detail" |
| `q2`        | What is the scientific method?                            | Min 20 characters | "Q2 - needs more detail" |
| `q3`        | What is a hypothesis?                                     | Min 20 characters | "Q3 - needs more detail" |
| `q4`        | What is a theory?                                         | Min 20 characters | "Q4 - needs more detail" |
| `q5`        | What is the difference between a hypothesis and a theory? | Min 20 characters | "Q5 - needs more detail" |
| `q6`        | What is the difference between science and pseudoscience? | Min 20 characters | "Q6 - needs more detail" |

**Total Questions:** 6 textareas  
**Points:** Not specified in form

---

## Lab 2: Weather Forecasting Tools

### Image Links and Captions (10 Items)

| Item # | Title                                   | Link ID  | Caption ID  | Validation                                   |
| ------ | --------------------------------------- | -------- | ----------- | -------------------------------------------- |
| 1      | Satellite Image – Minnesota             | `link1`  | `caption1`  | Valid URL (http/https), Caption min 20 chars |
| 2      | Radar Image – Chicago                   | `link2`  | `caption2`  | Valid URL (http/https), Caption min 20 chars |
| 3      | Surface Observations – Kansas           | `link3`  | `caption3`  | Valid URL (http/https), Caption min 20 chars |
| 4      | 7-Day Forecast – Fargo, ND              | `link4`  | `caption4`  | Valid URL (http/https), Caption min 20 chars |
| 5      | SPC Day 2 Outlook                       | `link5`  | `caption5`  | Valid URL (http/https), Caption min 20 chars |
| 6      | WPC QPF Forecast                        | `link6`  | `caption6`  | Valid URL (http/https), Caption min 20 chars |
| 7      | Ensemble Forecast Probability           | `link7`  | `caption7`  | Valid URL (http/https), Caption min 20 chars |
| 8      | Model Precipitation Forecast            | `link8`  | `caption8`  | Valid URL (http/https), Caption min 20 chars |
| 9      | 500 mb Heights and Winds – Central U.S. | `link9`  | `caption9`  | Valid URL (http/https), Caption min 20 chars |
| 10     | Visible Satellite – Southeast U.S.      | `link10` | `caption10` | Valid URL (http/https), Caption min 20 chars |

**Error Messages:**

- Missing links: "Missing links for item(s): [numbers]"
- Invalid URL format: "Invalid URL format for item(s): [numbers] (must start with http:// or https://)"
- Missing captions: "Missing captions for item(s): [numbers]"
- Short captions: "Caption(s) too short (need at least 20 characters) for item(s): [numbers]"

**Total Questions:** 20 inputs (10 URLs + 10 textareas)  
**Points:** Not specified in form

---

## Lab 3: Temperature, Pressure, and Density in the Atmosphere

### Part 1: Atmospheric Mass Distribution

| Question | Input ID   | Question Text                            | Type     | Validation | Points |
| -------- | ---------- | ---------------------------------------- | -------- | ---------- | ------ |
| Q1a      | `q1_224`   | Percentage at 22.4 km                    | Number   | 0-100%     | 0.5    |
| Q1b      | `q1_168`   | Percentage at 16.8 km                    | Number   | 0-100%     | 0.5    |
| Q1c      | `q1_112`   | Percentage at 11.2 km                    | Number   | 0-100%     | 0.5    |
| Q1d      | `q1_56`    | Percentage at 5.6 km                     | Number   | 0-100%     | 0.5    |
| Q2       | `q2_curve` | Which curve represents atmospheric mass? | Dropdown | Required   | 3      |

### Part 2: Barometric Pressure at Different Altitudes

| Question | Input ID       | Question Text                         | Type   | Validation | Points |
| -------- | -------------- | ------------------------------------- | ------ | ---------- | ------ |
| Q3a      | `q3a_pressure` | Pressure at cruising airliner (11 km) | Number | ≥ 0 mb     | 1      |
| Q3a      | `q3a_percent`  | Percentage above at 11 km             | Number | ≥ 0%       | 1      |
| Q3b      | `q3b_pressure` | Pressure at Mt. Everest (8.85 km)     | Number | ≥ 0 mb     | 1      |
| Q3b      | `q3b_percent`  | Percentage above at 8.85 km           | Number | ≥ 0%       | 1      |
| Q3c      | `q3c_pressure` | Pressure at Denver, CO (1.6 km)       | Number | ≥ 0 mb     | 1      |
| Q3c      | `q3c_percent`  | Percentage above at 1.6 km            | Number | ≥ 0%       | 1      |

### Part 4: Atmospheric Temperature Profiles

| Question | Input ID     | Question Text                             | Type     | Validation | Points |
| -------- | ------------ | ----------------------------------------- | -------- | ---------- | ------ |
| Q4       | `q4`         | Station with highest surface temperature  | Dropdown | Required   | 1      |
| Q5       | `q5`         | Station with highest temperature at 10 km | Dropdown | Required   | 1      |
| Q6       | `q6`         | Station with highest temperature at 14 km | Dropdown | Required   | 1      |
| Q7       | `q7_color`   | Color plot with inversion layer           | Dropdown | Required   | 0.5    |
| Q7       | `q7_start`   | Inversion layer start height              | Number   | ≥ 0 km     | 0.75   |
| Q7       | `q7_end`     | Inversion layer end height                | Number   | ≥ 0 km     | 0.75   |
| Q8       | `q8_height`  | Tropopause height (red station)           | Number   | Required   | 1      |
| Q8       | `q8_temp`    | Tropopause temperature (red station)      | Number   | Required   | 1      |
| Q9       | `q9_height`  | Tropopause height (blue station)          | Number   | Required   | 1      |
| Q9       | `q9_temp`    | Tropopause temperature (blue station)     | Number   | Required   | 1      |
| Q10      | `q10_height` | Tropopause height (magenta station)       | Number   | Required   | 1      |
| Q10      | `q10_temp`   | Tropopause temperature (magenta station)  | Number   | Required   | 1      |
| Q11      | `q11`        | Color plot representing Alaska            | Dropdown | Required   | 1      |
| Q12      | `q12`        | Color plot representing the tropics       | Dropdown | Required   | 1      |

### Part 5: Analysis and Synthesis

| Question | Input ID | Question Text                                                      | Type     | Validation   | Points |
| -------- | -------- | ------------------------------------------------------------------ | -------- | ------------ | ------ |
| Q13      | `q13`    | Tropopause-Temperature Relationship                                | Textarea | Min 20 chars | 3      |
| Q14      | `q14`    | Atmospheric Variables (pressure, density, temperature vs altitude) | Textarea | Min 20 chars | 3      |

**Error Messages:**

- "Missing or invalid numeric values: • [list]"
- "Missing dropdown selections: • [list]"
- "Missing text responses: • [list]"
- "Text responses too short (need at least 20 characters): • [list]"

**Total Questions:** 28 inputs (18 numbers, 8 dropdowns, 2 textareas)  
**Total Points:** 30

---

## Lab 4: Earth-Sun Geometry

### Part 1: Questions 1-3 (4 points)

| Question | Input ID | Question Text                           | Type     | Validation | Points |
| -------- | -------- | --------------------------------------- | -------- | ---------- | ------ |
| Q1       | `q1`     | [Question about Earth-Sun relationship] | Dropdown | Required   | 1      |
| Q2       | `q2`     | [Question about seasons]                | Dropdown | Required   | 1      |
| Q3a      | `q3a`    | [Part a]                                | Dropdown | Required   | 1      |
| Q3b      | `q3b`    | [Part b]                                | Dropdown | Required   | 1      |

### Part 2: Questions 4-6 (3 points)

| Question | Input ID | Question Text | Type     | Validation | Points |
| -------- | -------- | ------------- | -------- | ---------- | ------ |
| Q4       | `q4`     | [Question 4]  | Dropdown | Required   | 1      |
| Q5       | `q5`     | [Question 5]  | Dropdown | Required   | 1      |
| Q6       | `q6`     | [Question 6]  | Dropdown | Required   | 1      |

### Part 3: Questions 7-10 (8 points)

| Question | Input ID | Question Text          | Type     | Validation   | Points   |
| -------- | -------- | ---------------------- | -------- | ------------ | -------- |
| Q7       | `q7`     | [Question 7]           | Dropdown | Required     | Variable |
| Q8       | `q8`     | [Question 8]           | Dropdown | Required     | Variable |
| Q9       | `q9`     | [Question 9]           | Dropdown | Required     | Variable |
| Q10      | `q10`    | [Explanation question] | Textarea | Min 20 chars | Variable |

### Part 5: Table (15 points - 0.5 each = 30 cells)

| Cell ID        | Description                                       | Type     | Validation      |
| -------------- | ------------------------------------------------- | -------- | --------------- |
| `t_a` - `t_ad` | Solar declination and noon sun angle calculations | Dropdown | Required (each) |

**Table Cell IDs:** a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, date, v, w, x, y, z, aa, ab, ac, ad

**Error Messages:**

- "Missing question answers: • [list]"
- "Text response too short (need at least 20 characters): • [list]"
- "Missing table values: • [list]"

**Total Questions:** 40 inputs (9 dropdowns, 1 textarea, 30 table dropdowns)  
**Total Points:** 30

---

## Lab 5: Surface Map Analysis

### Question 1: Decode Station Model (4 points)

| Question | Input ID      | Question Text         | Type     | Validation | Points |
| -------- | ------------- | --------------------- | -------- | ---------- | ------ |
| Q1a      | `q1_pressure` | Sea-level Pressure    | Dropdown | Required   | 1      |
| Q1b      | `q1_temp`     | Temperature           | Dropdown | Required   | 1      |
| Q1c      | `q1_dewpoint` | Dew-point Temperature | Dropdown | Required   | 1      |
| Q1d      | `q1_sky`      | Sky Coverage          | Dropdown | Required   | 1      |

### Question 2: Decode Detailed Station Model (8 points)

| Question | Input ID            | Question Text            | Type     | Validation | Points |
| -------- | ------------------- | ------------------------ | -------- | ---------- | ------ |
| Q2a      | `q2_weather`        | Current Weather          | Dropdown | Required   | 1      |
| Q2b      | `q2_pressure`       | Sea-level Pressure       | Dropdown | Required   | 1      |
| Q2c      | `q2_temp`           | Temperature              | Dropdown | Required   | 1      |
| Q2d      | `q2_dewpoint`       | Dew-point Temperature    | Dropdown | Required   | 1      |
| Q2e      | `q2_sky`            | Sky Coverage             | Dropdown | Required   | 1      |
| Q2f      | `q2_windspeed`      | Wind Speed               | Dropdown | Required   | 1      |
| Q2g      | `q2_winddir`        | Wind Direction           | Dropdown | Required   | 1      |
| Q2h      | `q2_pressurechange` | Pressure Change (3-hour) | Dropdown | Required   | 1      |
| Q2i      | `q2_precipamount`   | Precipitation Amount     | Dropdown | Required   | 1      |

### Question 3: Create Station Model (Canvas Tool - 6 points)

**Note:** Question 3 uses the Station Model Builder canvas component. Image export required.

### Question 4: Single Line Canvas (Canvas Tool - 6 points)

**Note:** Question 4 uses a single-line drawing canvas. Image export required.

### Question 5: Multi-Line Canvas (Canvas Tool - 6 points)

**Note:** Question 5 uses a multi-line drawing canvas. Image export required.

**Error Messages:**

- Standard dropdown validation: "Please select a value"
- Form export validates that all dropdowns are filled before allowing download

**Total Questions:** 13 dropdowns + 3 canvas tools  
**Total Points:** 30  
**Additional Requirements:** Canvas images must be saved separately and submitted with text file

---

## Lab 6: Upper Air Analysis

### Part 1: 850 mb Map Analysis

| Question | Input ID  | Question Text                          | Type | Validation | Points |
| -------- | --------- | -------------------------------------- | ---- | ---------- | ------ |
| Q1       | `q1`      | Pattern identified                     | Text | Required   | 1      |
| Q2       | `q2_from` | Temperature range - lowest             | Text | Required   | 0.5    |
| Q2       | `q2_to`   | Temperature range - highest            | Text | Required   | 0.5    |
| Q3       | `q3`      | Warmest air location                   | Text | Required   | 1      |
| Q4       | `q4`      | Coldest air location                   | Text | Required   | 1      |
| Q5       | `q5`      | Ridge location (A, B, C, or D)         | Text | Required   | 1      |
| Q6       | `q6`      | Trough location (A, B, C, or D)        | Text | Required   | 1      |
| Q7       | `q7`      | State with best lift for precipitation | Text | Required   | 1      |

### Part 2: 700 mb Map Analysis

| Question | Input ID   | Question Text                      | Type     | Validation   | Points |
| -------- | ---------- | ---------------------------------- | -------- | ------------ | ------ |
| Q8       | `q8`       | Pattern identified                 | Text     | Required     | 1      |
| Q9       | `q9`       | Warmest air location               | Text     | Required     | 1      |
| Q10      | `q10`      | Coldest air location               | Text     | Required     | 1      |
| Q11      | `q11_from` | Humidity range - lowest            | Text     | Required     | 0.5    |
| Q11      | `q11_to`   | Humidity range - highest           | Text     | Required     | 0.5    |
| Q12      | `q12`      | Precipitation forecast explanation | Textarea | Min 20 chars | 2      |

### Part 3: 500 mb Map Analysis

| Question | Input ID | Question Text           | Type | Validation | Points |
| -------- | -------- | ----------------------- | ---- | ---------- | ------ |
| Q13      | `q13`    | Wind direction at point | Text | Required   | 1      |

### Part 4: 300 mb Map Analysis

| Question | Input ID | Question Text                   | Type | Validation | Points |
| -------- | -------- | ------------------------------- | ---- | ---------- | ------ |
| Q14      | `q14`    | Pattern identified              | Text | Required   | 1      |
| Q15      | `q15`    | Jet stream location             | Text | Required   | 1      |
| Q16      | `q16_1`  | Two states under jet core #1    | Text | Required   | 0.5    |
| Q16      | `q16_2`  | Two states under jet core #2    | Text | Required   | 0.5    |
| Q17      | `q17`    | State with best storm potential | Text | Required   | 1      |

**Error Messages:**

- "Please fill in all required fields"
- Textarea: "Please provide at least 20 characters"

**Total Questions:** 20 inputs (18 text, 1 textarea, 1 text pair)  
**Points:** Not specified in form  
**Note:** Lab 6 uses inline styles and basic form validation

---

## Lab 7: Air Masses and Fronts

### Question 1: Air Mass Identification (7 points)

**Identify each air mass labeled A-G in the first image:**

| Question | Input ID | Question Text                | Type     | Validation                    | Points |
| -------- | -------- | ---------------------------- | -------- | ----------------------------- | ------ |
| Q1a      | `q1a`    | Air mass type for location A | Dropdown | Required (cP, cT, mP, mT, cA) | 1      |
| Q1b      | `q1b`    | Air mass type for location B | Dropdown | Required (cP, cT, mP, mT, cA) | 1      |
| Q1c      | `q1c`    | Air mass type for location C | Dropdown | Required (cP, cT, mP, mT, cA) | 1      |
| Q1d      | `q1d`    | Air mass type for location D | Dropdown | Required (cP, cT, mP, mT, cA) | 1      |
| Q1e      | `q1e`    | Air mass type for location E | Dropdown | Required (cP, cT, mP, mT, cA) | 1      |
| Q1f      | `q1f`    | Air mass type for location F | Dropdown | Required (cP, cT, mP, mT, cA) | 1      |
| Q1g      | `q1g`    | Air mass type for location G | Dropdown | Required (cP, cT, mP, mT, cA) | 1      |

**Air Mass Options:**

- **cP** - Continental Polar (cold, dry)
- **cT** - Continental Tropical (hot, dry)
- **mP** - Maritime Polar (cool, moist)
- **mT** - Maritime Tropical (warm, moist)
- **cA** - Continental Arctic (very cold, dry)

### Question 2: Front Classification (3 points)

| Question | Input ID | Question Text             | Type     | Validation | Points |
| -------- | -------- | ------------------------- | -------- | ---------- | ------ |
| Q2a      | `q2a`    | Front type for location A | Dropdown | Required   | 1      |
| Q2b      | `q2b`    | Front type for location B | Dropdown | Required   | 1      |
| Q2c      | `q2c`    | Front type for location C | Dropdown | Required   | 1      |

### Question 3: Surface Analysis (Canvas Tool)

**Note:** Question 3 uses a multi-line canvas drawing tool for drawing fronts and air masses on a surface map. Canvas image export required.

**Error Messages:**

- Standard dropdown validation: "Please select a value"
- Form export validates that all dropdowns are filled before allowing download

**Total Questions:** 10 dropdowns (7 air mass + 3 front) + 1 canvas tool  
**Total Points:** 30 (10 points for dropdowns, 20 points for canvas work)  
**Additional Requirements:** Canvas image must be saved separately and submitted with text file

---

## Lab 8: Station Models

### Station Letter Questions

| Question | Input ID        | Question Text  | Type | Validation         | Error Message                                         |
| -------- | --------------- | -------------- | ---- | ------------------ | ----------------------------------------------------- |
| Station  | `stationLetter` | Station Letter | Text | A, B, C, or D only | "Please enter a valid station letter (A, B, C, or D)" |

### Meteorological Data (Station-specific)

| Question           | Input ID      | Question Text      | Type   | Validation     | Range                                          |
| ------------------ | ------------- | ------------------ | ------ | -------------- | ---------------------------------------------- |
| Temperature        | `temperature` | Temperature        | Number | -100 to 150°F  | "Temperature must be between -100°F and 150°F" |
| Dew Point          | `dewPoint`    | Dew Point          | Number | -100 to 100°F  | "Dew point must be between -100°F and 100°F"   |
| Sea Level Pressure | `pressure`    | Sea Level Pressure | Number | 940 to 1050 mb | "Pressure must be between 940 and 1050 mb"     |

### Analysis Questions (Textareas)

| Question | Input ID | Question Text               | Type     | Validation   |
| -------- | -------- | --------------------------- | -------- | ------------ |
| Q1       | `q1`     | Wind analysis               | Textarea | Min 20 chars |
| Q2       | `q2`     | Temperature analysis        | Textarea | Min 20 chars |
| Q3       | `q3`     | Pressure analysis           | Textarea | Min 20 chars |
| Q4       | `q4`     | Weather conditions analysis | Textarea | Min 20 chars |

**Error Messages:**

- "Please enter a valid station letter (A, B, C, or D)"
- "Temperature must be between -100°F and 150°F"
- "Dew point must be between -100°F and 100°F"
- "Pressure must be between 940 and 1050 mb"
- "Please provide a detailed answer (at least 20 characters) for Question [n]"

**Total Questions:** 8 inputs (1 text, 3 numbers, 4 textareas)

---

## Lab 9: Weather Forecasting

**Note:** Lab 9 uses image loopers and form-exporter.js with standard form validation

---

## Lab 10: Severe Weather

### Location Information

| Question | Input ID | Question Text | Type | Validation | Range |
| -------- | -------- | ------------- | ---- | ---------- | ----- |
| City     | `city`   | City Name     | Text | Required   | N/A   |
| State    | `state`  | State         | Text | Required   | N/A   |
| Date     | `date`   | Date          | Date | Required   | N/A   |

### Meteorological Data

| Question       | Input ID        | Question Text         | Type     | Validation                 | Range                                          |
| -------------- | --------------- | --------------------- | -------- | -------------------------- | ---------------------------------------------- |
| Temperature    | `temperature`   | Temperature           | Number   | -100 to 150°F              | "Temperature must be between -100°F and 150°F" |
| Dew Point      | `dewPoint`      | Dew Point Temperature | Number   | -100 to 100°F              | "Dew point must be between -100°F and 100°F"   |
| Wind Speed     | `windSpeed`     | Wind Speed            | Number   | 0 to 150 knots             | "Wind speed must be between 0 and 150 knots"   |
| Wind Direction | `windDirection` | Wind Direction        | Dropdown | N, S, E, W, NE, NW, SE, SW | "Please select a valid wind direction"         |

### Analysis Questions (Textareas)

| Question | Input ID    | Question Text                      | Type     | Validation   |
| -------- | ----------- | ---------------------------------- | -------- | ------------ |
| Q1       | `analysis1` | Severe weather type identification | Textarea | Min 20 chars |
| Q2       | `analysis2` | Meteorological conditions analysis | Textarea | Min 20 chars |
| Q3       | `analysis3` | Safety recommendations             | Textarea | Min 20 chars |

**Error Messages:**

- "Please fill in [field name]"
- "Temperature must be between -100°F and 150°F"
- "Dew point must be between -100°F and 100°F"
- "Wind speed must be between 0 and 150 knots"
- "Please select a valid wind direction"
- "Please provide a detailed answer (at least 20 characters) for Question [n]"

**Total Questions:** 10 inputs (3 text, 1 date, 3 numbers, 1 dropdown, 3 textareas)

---

## Common Validation Patterns

### Validation Types Used Across Labs

1. **Textarea Validation**

   - Minimum length: 20 characters
   - Error styling: Red border (#dc2626), light red background (#fef2f2)
   - Error message: "[Question] - needs more detail" or "too short (need at least 20 characters)"

2. **Number Input Validation**

   - Range checking (min/max values)
   - NaN detection (empty or non-numeric)
   - Error styling: Red border, light red background

3. **Dropdown/Select Validation**

   - Must have a value selected
   - Cannot be empty string
   - Error styling: Red border, light red background

4. **URL Validation** (Lab 2 only)
   - Must match pattern: `/^https?:\/\/.+/i`
   - Must start with http:// or https://

### Common Error Handling

All labs implement:

- Visual feedback (red border and background on invalid inputs)
- Alert dialog with detailed error list
- Scroll to first invalid field
- Focus on first invalid field
- Prevents form submission if validation fails

### Validation Trigger

All labs validate on:

- Download/Export button click (pre-submission validation)
- Individual field validation happens in `validateAllInputs()` function

---

## File Structure

**Labs with Inline Validation:**

- Lab 1: `web-components/lab01/index.html` (inline script)
- Lab 2: `web-components/lab02/index.html` (inline script)
- Lab 3: `web-components/lab03/index.html` (inline script)
- Lab 4: `web-components/lab04/index.html` (inline script)

**Labs with External JS Files:**

- Lab 5: `web-components/lab05/lab05-main.js`
- Lab 7: `web-components/lab07/lab07-main.js`
- Lab 8: `web-components/lab08/lab08-main.js`
- Lab 9: `web-components/lab09/lab09-main.js`
- Lab 10: `web-components/lab10/lab10-main.js`

**Shared Utilities:**

- `web-components/shared/utils/form-exporter.js` - Used by Labs 5, 7, 8, 9, 10

---

_Last Updated: October 14, 2025_
