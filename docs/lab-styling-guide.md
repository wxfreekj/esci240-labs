# Lab Styling Guide - Lab 8 Pattern

## Overview

This guide documents the consistent styling pattern used across all ESCI 240 labs, based on the Lab 7/Lab 8 implementation.

## 1. HTML Head Section

### Replace Custom Styles with Shared Stylesheets

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Lab X: Title</title>
  <link rel="stylesheet" href="../shared/styles/common.css" />
  <link rel="stylesheet" href="../shared/styles/lab-styles.css" />
</head>
```

## 2. Page Structure

### Header

```html
<div class="container">
  <div class="header">
    <h1>Lab X: Title</h1>
    <p>ESCI 240 - Fall 2025</p>
  </div>

  <div class="content">
    <!-- Lab content goes here -->
  </div>
</div>
```

## 3. Question Pattern (Lab 8 Style)

### Old Pattern (DO NOT USE)

```html
<div class="question">
  <label class="question-label">
    <strong>Question 1</strong>: What is the answer?
    <span class="question-points">(2 pts)</span>
  </label>
  <input type="text" id="q1" />
</div>
```

### New Pattern (USE THIS)

```html
<!-- Section for each major topic -->
<div class="section">
  <h2>Question 1: Brief Descriptive Title (2 pts)</h2>

  <!-- Optional: Instructions paragraph -->
  <p><strong>Instructions:</strong> Provide specific guidance here.</p>

  <!-- Form group for each question/input -->
  <div class="form-group">
    <label for="q1">What is the actual question text?</label>
    <input type="text" id="q1" placeholder="Enter answer..." />
  </div>
</div>
```

### For Multiple Sub-Questions

```html
<div class="section">
  <h2>Section 2: Topic Name</h2>

  <p><strong>Instructions:</strong> General instructions for this section.</p>

  <div class="intro-box">
    <!-- Background information, definitions, etc. -->
  </div>

  <h2>Question 2a: First Sub-Question (2 pts)</h2>
  <div class="form-group">
    <label for="q2a">Question text here?</label>
    <select id="q2a">
      <option value="">Select...</option>
      <option value="option1">Option 1</option>
    </select>
  </div>

  <h2>Question 2b: Second Sub-Question (2 pts)</h2>
  <div class="form-group">
    <label for="q2b">Question text here?</label>
    <select id="q2b">
      <option value="">Select...</option>
      <option value="option2">Option 2</option>
    </select>
  </div>
</div>
```

## 4. Input Types

### Text Inputs

```html
<div class="form-group">
  <label for="q1-temp">Enter temperature:</label>
  <input
    type="number"
    id="q1-temp"
    placeholder="Enter temperature"
    step="0.1"
  />
</div>
```

### Dropdowns/Selects

```html
<div class="form-group">
  <label for="q2-airMass">Select air mass type:</label>
  <select id="q2-airMass" class="form-select">
    <option value="">Select...</option>
    <option value="cP">cP</option>
    <option value="mT">mT</option>
  </select>
</div>
```

### Textareas

```html
<div class="form-group">
  <label for="q3-explanation">Explain your reasoning:</label>
  <textarea
    id="q3-explanation"
    rows="4"
    placeholder="Enter your explanation..."
  ></textarea>
</div>
```

### Inline Inputs (From/To Ranges)

```html
<div class="form-group">
  <label>Temperature range:</label>
  <div class="inline-inputs">
    <input type="number" id="q4-temp-from" placeholder="From" step="1" />
    <span>to</span>
    <input type="number" id="q4-temp-to" placeholder="To" step="1" />
    <span class="unit-label">degrees F</span>
  </div>
</div>
```

## 5. Information Boxes

### Intro Box (Blue)

```html
<div class="intro-box">
  <h3>Topic Overview</h3>
  <p>Background information or definitions...</p>
  <ul>
    <li><strong>Term:</strong> Definition</li>
  </ul>
</div>
```

### Info Box (Light Blue)

```html
<div class="info-box">
  <p>Important note or instruction...</p>
</div>
```

## 6. Canvas Drawing Tools

```html
<h2>Question 3: Drawing Analysis (18 pts)</h2>
<p><strong>Instructions:</strong> Draw the required features on the map.</p>

<div class="curve-widget-wrapper">
  <h2>Drawing Tool Title</h2>
  <div class="stage">
    <img id="bg-img" src="map.png" alt="Map" />
    <canvas id="draw-canvas"></canvas>
  </div>
  <div class="controls">
    <label for="line-select">Draw Feature:</label>
    <select id="line-select">
      <option value="0">Feature 1</option>
      <option value="1">Feature 2</option>
    </select>
    <button onclick="clearCanvas()">Clear</button>
  </div>
</div>
```

## 7. Buttons

```html
<div class="button-container">
  <button type="button" class="download-btn" onclick="exportAnswers()">
    📥 Download Answers
  </button>
  <button type="button" class="clear-btn" onclick="clearForm()">
    🗑️ Clear All
  </button>
</div>
```

## 8. Key Styling Classes

- **`.section`** - Wraps each major question/topic area
- **`.form-group`** - Wraps each label/input pair
- **`.inline-inputs`** - For horizontal input arrangements
- **`.intro-box`** - Blue background info box
- **`.info-box`** - Light blue instruction box
- **`.diagram-container`** - Centers images with captions
- **`.image-caption`** - Caption below images
- **`.button-container`** - Horizontal button layout
- **`.download-btn`** - Primary action button
- **`.clear-btn`** - Secondary action button

## 9. Point Values in Headings

Always include point values in the h2 heading:

- ✅ `<h2>Question 1: Description (3 pts)</h2>`
- ❌ `<span class="question-points">(3 pts)</span>` inside labels

## 10. Migration Checklist

For each lab:

1. ✅ Replace `<style>` tag with shared stylesheet links
2. ✅ Ensure header uses `.header` class
3. ✅ Wrap content in `.content` div
4. ✅ Convert all questions to use `<h2>` with points
5. ✅ Wrap questions in `.section` div
6. ✅ Use `.form-group` for label/input pairs
7. ✅ Remove old `.question-number` and `.question-text` divs
8. ✅ Move point values from labels to h2 headings
9. ✅ Add Instructions paragraphs where helpful
10. ✅ Update buttons to use `.download-btn` and `.clear-btn`

## Examples from Completed Labs

### Lab 7 - Question 1 (Air Mass Identification)

```html
<div class="section">
  <h2>Section 1: Air Mass Identification</h2>

  <p>
    <strong>Instructions:</strong> Examine the air mass source regions on the
    map and identify the air mass type for each labeled location.
  </p>

  <div class="intro-box">
    <p>Air masses are classified based on their source region:</p>
    <ul>
      <li><strong>Continental (c):</strong> Forms over land - dry</li>
      <li><strong>Maritime (m):</strong> Forms over water - moist</li>
    </ul>
  </div>

  <h2>Question 1: Air Mass Type Classification (7 pts)</h2>
  <p>
    Identify the air mass type for each location labeled A through G in Figure 1
    above.
  </p>

  <!-- 7 dropdowns in grid layout -->
</div>
```

### Lab 8 - Question 2 (Pressure Drop)

```html
<div class="section">
  <h2>Question 2: Pressure Drop (2 pts)</h2>
  <p>
    <strong>Instructions:</strong> Examine the surface maps labeled A through D
    showing the storm development from November 9 to November 11.
  </p>

  <img
    src="Fig2.PNG"
    height="600px"
    style="display: block; margin: 0 auto"
    alt="Atmospheric Pressure Curves"
  />

  <div class="form-group">
    <label for="q2-pressure"
      >How much did the pressure drop in the storm's center from November 9,
      1200z, until November 11, 0000z? (in millibars)</label
    >
    <input
      type="number"
      id="q2-pressure"
      name="q2-pressure"
      placeholder="Enter pressure drop in mb"
      step="1"
    />
  </div>
</div>
```

## Benefits of This Pattern

1. **Consistency** - All labs look and feel the same
2. **Maintainability** - Changes to shared CSS affect all labs
3. **Readability** - Clear hierarchy with h2 headings
4. **Accessibility** - Proper label/input associations
5. **Professional** - Clean, modern appearance
6. **Responsive** - Works on all screen sizes
7. **Easy Grading** - Clear point values in headings
