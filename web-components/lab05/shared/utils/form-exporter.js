/**
 * Export lab answers AND images as a single ZIP file for Canvas submission
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

  // Export each question
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

  // Add the text file to the zip
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
      const mergedSingleCanvas = await mergeCanvasWithImage(
        singleCanvas,
        singleImg
      );
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
      const mergedMultiCanvas = await mergeCanvasWithImage(
        multiCanvas,
        multiImg
      );
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
async function mergeCanvasWithImage(canvas, img) {
  const tempCanvas = document.createElement("canvas");
  tempCanvas.width = canvas.width;
  tempCanvas.height = canvas.height;
  const ctx = tempCanvas.getContext("2d");

  // Draw the background image
  ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

  // Draw the canvas on top
  ctx.drawImage(canvas, 0, 0);

  return tempCanvas;
}
