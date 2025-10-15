# File Naming Conventions - ESCI 240 Labs

All lab output files now follow a consistent `LabXX_DescriptiveName` format.

## Standardized File Names

### Lab 01 - Nature of Science
- **Text File:** `Lab01_NatureOfScience.txt`

### Lab 02 - Weather Data
- **Text File:** `Lab02_WeatherData.txt`

### Lab 03 - Atmospheric Analysis
- **Text File:** `Lab03_AtmosphericAnalysis.txt`

### Lab 04 - Earth-Sun Geometry
- **Text File:** `Lab04_EarthSunGeometry.txt`

### Lab 05 - Surface Map Analysis
- **Text File:** `Lab05_SurfaceMapAnalysis.txt`
- **Image 1:** `Lab05_StationModel.png` (Station model diagram)
- **Image 2:** `Lab05_Isodrosotherm_45F.png` (45°F isodrosotherm)
- **Image 3:** `Lab05_Isotherms.png` (Temperature isotherms)

### Lab 06 - Upper Air Analysis
- **Text File:** `Lab06_UpperAirAnalysis.txt`

### Lab 07 - Air Masses and Fronts
- **Text File:** `Lab07_AirMassesAndFronts.txt`
- **Image:** `Lab07_SurfaceAnalysis.png` (Surface analysis with fronts)

### Lab 08 - Mid-Latitude Cyclones
- **Text File:** `Lab08_MidLatitudeCyclones.txt`

### Lab 09 - Weather Forecasting
- **Text File:** `Lab09_WeatherForecasting.txt`

### Lab 10 - Severe Weather
- **Text File:** `Lab10_SevereWeather.txt`

## Naming Convention Rules

1. **Lab Number:** Two-digit format (01-10)
2. **Separator:** Underscore (`_`)
3. **Description:** CamelCase with no spaces
4. **Extension:** `.txt` for answers, `.png` for images
5. **No Timestamps:** Files use static names for consistency

## Previous Naming Conventions (Now Deprecated)

The following naming patterns were used previously but have been standardized:

- ❌ `lab01_lowercase_with_underscores.txt`
- ❌ `Lab2.txt` (single digit)
- ❌ `lab3_submission_[timestamp].txt` (timestamps removed)
- ❌ `Lab4_[timestamp].txt` (timestamps removed)
- ❌ `Lab5_With_Underscores.txt`
- ❌ `station_model.png` (no lab prefix)
- ❌ `lab7_lowercase_image.png`

## Changes Made

### Text Files
- All answer files now use `LabXX_DescriptiveName.txt` format
- Timestamps removed from Labs 3, 4, and 6 for consistency
- Single-digit lab numbers converted to two digits (Lab2 → Lab02)

### Image Files
- All image files now include lab prefix: `LabXX_Description.png`
- Station model renamed: `station_model.png` → `Lab05_StationModel.png`
- Lab 5 images: `lab5_lowercase.png` → `Lab05_CamelCase.png`
- Lab 7 image: `lab7_surface_analysis.png` → `Lab07_SurfaceAnalysis.png`

## Implementation Details

File naming is configured in:
- **HTML files:** Direct filename in download attribute
- **Config files:** `lab05-config.js`, `lab07-config.js` for canvas tools
- **Main JS files:** `lab08-main.js`, `lab09-main.js`, `lab10-main.js`
- **Shared component:** `station-model-builder.js` accepts `saveFilename` config

## Benefits of Standardization

✅ **Consistent sorting:** All files sort naturally by lab number  
✅ **Professional appearance:** CamelCase looks clean and modern  
✅ **Easy identification:** Lab number always visible in filename  
✅ **No duplicates:** Removed timestamps prevent accidental overwriting  
✅ **Clear documentation:** Students know exactly what files to submit
