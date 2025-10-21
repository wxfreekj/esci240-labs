/**
 * Generic form export utility for lab assignments
 */

/**
 * Export lab answers to a text file for Canvas submission (OLD METHOD)
 * @param {Object} config - Lab configuration object
 * @returns {string} - Filename of the exported file
 */
export function exportLabAnswers(config) {
  const { labNumber, labName, totalPoints, questions } = config;

  let output = "";
  output += `ASSIGNMENT=${labName}\n`;
  output += `LAB_NUMBER=${labNumber}\n`;
  output += `DATE=${new Date().toISOString()}\n`;
  output += `TOTAL_POINTS=${totalPoints}\n`;
  output += "---BEGIN_ANSWERS---\n";

  questions.forEach((q) => {
    if (q.id) {
      const element = document.getElementById(q.id);
      if (element) {
        output += `${q.key}=${element.value}\n`;
      }
    } else if (q.note) {
      output += `${q.key}=${q.note}\n`;
    }
  });

  output += "---END_ANSWERS---\n";
  output += "\nIMPORTANT: Please also upload any required images to Canvas.\n";

  const blob = new Blob([output], { type: "text/plain" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  const filename = `Lab${labNumber}_Answers_${Date.now()}.txt`;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);

  return filename;
}

/**
 * Export lab answers AND images as a single ZIP file for Canvas submission (NEW METHOD)
 * @param {Object} config - Lab configuration object
 * @returns {Promise<string>} - Filename of the exported zip file
 */
export async function exportLabAnswersAsZip(config) {
  const { labNumber, labName, totalPoints, questions } = config;

  // Check if JSZip is available
  if (typeof JSZip === "undefined") {
    alert(
      "Error: JSZip library not loaded. Please refresh the page and try again."
    );
    throw new Error("JSZip not available");
  }

  // Create a new zip file
  const zip = new JSZip();

  // 1. Create the text file with answers
  let textContent = "";
  textContent += `ASSIGNMENT=${labName}\n`;
  textContent += `LAB_NUMBER=${labNumber}\n`;
  textContent += `DATE=${new Date().toISOString()}\n`;
  textContent += `TOTAL_POINTS=${totalPoints}\n`;
  textContent += "---BEGIN_ANSWERS---\n";

  questions.forEach((q) => {
    if (q.id) {
      const element = document.getElementById(q.id);
      if (element) {
        textContent += `${q.key}=${element.value}\n`;
      }
    } else if (q.note) {
      textContent += `${q.key}=${q.note}\n`;
    }
  });

  textContent += "---END_ANSWERS---\n";
  zip.file(`${labName}.txt`, textContent);

  // 2. Add the Station Model Builder image (Question 3)
  try {
    const stationModelWorkspace = document.getElementById("workspace");
    if (stationModelWorkspace) {
      const stationModelCanvas = await html2canvas(stationModelWorkspace, {
        backgroundColor: null,
      });
      const stationModelData = stationModelCanvas
        .toDataURL("image/png")
        .split(",")[1];
      zip.file("Lab05_StationModel.png", stationModelData, { base64: true });
    }
  } catch (error) {
    console.warn("Could not capture station model:", error);
  }

  // 3. Add the Single Line Canvas image (Question 4)
  try {
    const singleCanvas = document.getElementById("draw-canvas-single");
    const singleImg = document.getElementById("bg-img-single");
    if (singleCanvas && singleImg) {
      const mergedSingleCanvas = mergeCanvasWithImage(singleCanvas, singleImg);
      const singleData = mergedSingleCanvas
        .toDataURL("image/png")
        .split(",")[1];
      zip.file("Lab05_Isodrosotherm_45F.png", singleData, { base64: true });
    }
  } catch (error) {
    console.warn("Could not capture isodrosotherm canvas:", error);
  }

  // 4. Add the Multi-Line Canvas image (Question 5)
  try {
    const multiCanvas = document.getElementById("draw-canvas-multi");
    const multiImg = document.getElementById("bg-img-multi");
    if (multiCanvas && multiImg) {
      const mergedMultiCanvas = mergeCanvasWithImage(multiCanvas, multiImg);
      const multiData = mergedMultiCanvas.toDataURL("image/png").split(",")[1];
      zip.file("Lab05_Isotherms.png", multiData, { base64: true });
    }
  } catch (error) {
    console.warn("Could not capture isotherms canvas:", error);
  }

  // Generate the zip file and trigger download
  const zipBlob = await zip.generateAsync({ type: "blob" });
  const url = URL.createObjectURL(zipBlob);
  const link = document.createElement("a");
  link.href = url;
  const filename = `Lab05_Complete_Submission.zip`;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(url);

  return filename;
}

/**
 * Helper function to merge a canvas drawing with its background image
 * @param {HTMLCanvasElement} canvas - The drawing canvas
 * @param {HTMLImageElement} img - The background image
 * @returns {HTMLCanvasElement} - New canvas with merged content
 */
function mergeCanvasWithImage(canvas, img) {
  const tempCanvas = document.createElement("canvas");
  tempCanvas.width = canvas.width;
  tempCanvas.height = canvas.height;
  const ctx = tempCanvas.getContext("2d");

  // Draw the background image first
  ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

  // Draw the student's drawing on top
  ctx.drawImage(canvas, 0, 0);

  return tempCanvas;
}

/**
 * Clear all form inputs
 */
export function clearLabForm() {
  if (
    confirm(
      "⚠️ Are you sure you want to clear all answers? This cannot be undone."
    )
  ) {
    const inputs = document.querySelectorAll(
      'input[type="text"], input[type="number"], select, textarea'
    );
    inputs.forEach((input) => {
      input.value = "";
    });

    inputs.forEach((input) => {
      input.dispatchEvent(new Event("change"));
    });

    alert("✅ All answers have been cleared.");
  }
}
