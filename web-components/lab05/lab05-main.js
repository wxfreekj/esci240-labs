/**
 * Lab 5 Main Script
 * Initializes all components for Surface Map Analysis lab
 */

import { initializeStationModelBuilder } from "./shared/components/station-model-builder.js?v=6";
import { initializeSingleLineCanvas } from "./shared/components/single-line-canvas.js?v=6";
import { initializeMultiLineCanvas } from "./shared/components/multi-line-canvas.js?v=6";
import {
  exportLabAnswers,
  clearLabForm,
} from "./shared/utils/form-exporter.js";
import { lab05Config } from "./lab05-config.js";

// Initialize all components when DOM is loaded
document.addEventListener("DOMContentLoaded", function () {
  // Initialize progress tracking
  initializeProgressTracking();

  // Initialize Station Model Builder (Question 3)
  initializeStationModelBuilder({
    containerId: "station-model-builder-container",
    ...lab05Config.stationModelBuilder,
  });

  // Initialize Single Line Canvas (Question 4)
  initializeSingleLineCanvas(lab05Config.singleLineCanvas);

  // Initialize Multi-Line Canvas (Question 5)
  initializeMultiLineCanvas(lab05Config.multiLineCanvas);

  // Make export functions globally available
  window.exportAnswers = () => {
    const filename = exportLabAnswers(lab05Config);
    alert(
      "✅ Answers exported successfully!\n\nFile: " +
        filename +
        "\n\nPlease submit this file AND your images for Questions 3, 4, and 5 to Canvas."
    );
  };

  window.clearForm = () => {
    clearLabForm();
  };
});

/**
 * Initialize progress bar tracking based on points
 */
function initializeProgressTracking() {
  function updateProgress() {
    let earnedPoints = 0;
    const totalPoints = 30; // 4+8+6+4+8

    // Question 1: 4 points (q1_pressure, q1_temp, q1_dewpoint, q1_wind)
    const q1Inputs = ["q1_pressure", "q1_temp", "q1_dewpoint", "q1_wind"];
    let q1Complete = 0;
    q1Inputs.forEach((id) => {
      const el = document.getElementById(id);
      if (el && el.value.trim() !== "") q1Complete++;
    });
    earnedPoints += (q1Complete / q1Inputs.length) * 4;

    // Question 2: 8 points (q2a through q2h)
    const q2Inputs = ["q2a", "q2b", "q2c", "q2d", "q2e", "q2f", "q2g", "q2h"];
    let q2Complete = 0;
    q2Inputs.forEach((id) => {
      const el = document.getElementById(id);
      if (el && el.value.trim() !== "") q2Complete++;
    });
    earnedPoints += (q2Complete / q2Inputs.length) * 8;

    // Question 3: 6 points (station model builder - check if image saved)
    const stationModelContainer = document.getElementById(
      "station-model-builder-container"
    );
    if (stationModelContainer) {
      const canvas = stationModelContainer.querySelector("canvas");
      if (canvas && hasCanvasContent(canvas)) {
        earnedPoints += 6;
      }
    }

    // Question 4: 4 points (single line canvas drawing)
    const singleCanvas = document.getElementById("draw-canvas-single");
    if (singleCanvas && hasCanvasContent(singleCanvas)) {
      earnedPoints += 4;
    }

    // Question 5: 8 points (multi-line canvas drawing)
    const multiCanvas = document.getElementById("draw-canvas-multi");
    if (multiCanvas && hasCanvasContent(multiCanvas)) {
      earnedPoints += 8;
    }

    const progress = (earnedPoints / totalPoints) * 100;
    const progressBar = document.getElementById("progressBar");
    if (progressBar) {
      progressBar.style.width = progress + "%";
    }
  }

  function hasCanvasContent(canvas) {
    const ctx = canvas.getContext("2d", { willReadFrequently: true });
    if (!ctx) return false;

    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    const pixels = imageData.data;

    // Check if any non-white/non-transparent pixels exist
    for (let i = 0; i < pixels.length; i += 4) {
      const r = pixels[i];
      const g = pixels[i + 1];
      const b = pixels[i + 2];
      const a = pixels[i + 3];

      if (a > 0 && (r !== 255 || g !== 255 || b !== 255)) {
        return true;
      }
    }
    return false;
  }

  const inputs = document.querySelectorAll("input, select, textarea");
  inputs.forEach((input) => {
    input.addEventListener("input", updateProgress);
    input.addEventListener("change", updateProgress);
  });

  // Initial update
  updateProgress();

  // Periodic update for canvas changes
  setInterval(updateProgress, 3000);
}

// Prevent accidental page navigation
window.addEventListener("beforeunload", function (e) {
  const inputs = document.querySelectorAll(
    'input[type="text"], input[type="number"], select, textarea'
  );
  let hasContent = false;
  inputs.forEach((input) => {
    if (input.value.trim() !== "") hasContent = true;
  });

  if (hasContent) {
    e.preventDefault();
    e.returnValue = "";
  }
});
