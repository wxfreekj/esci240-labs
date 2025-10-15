/**
 * Lab 5 Configuration
 * All lab-specific settings in one place
 */

export const lab05Config = {
  labNumber: 5,
  labName: "Lab05_SurfaceMapAnalysis",
  totalPoints: 30,

  // Station Model Builder Configuration (Question 3)
  stationModelBuilder: {
    saveFilename: "Lab05_StationModel.png",
    weatherData: {
      currentWeather: "Continuous light rain",
      pressure: "1004.5 mb",
      temperature: "53°F",
      dewpoint: "51°F",
      skyCoverage: "Completely overcast",
      windSpeed: "15 knots",
      windDirection: "NE",
    },
  },

  // Single Line Canvas Configuration (Question 4)
  singleLineCanvas: {
    canvasId: "draw-canvas-single",
    imageId: "bg-img-single",
    undoLastBtnId: "undo-last-btn-single",
    undoAllBtnId: "undo-all-btn-single",
    saveBtnId: "save-btn-single",
    saveFilename: "Lab05_Isodrosotherm_45F.png",
    lineColor: "#FF0000",
    lineWidth: 2,
    lineDash: [6, 10],
  },

  // Multi-Line Canvas Configuration (Question 5)
  multiLineCanvas: {
    canvasId: "draw-canvas-multi",
    imageId: "bg-img-multi",
    selectId: "line-select-multi",
    undoLastBtnId: "undo-last-btn-multi",
    undoAllBtnId: "undo-all-btn-multi",
    saveBtnId: "save-btn-multi",
    saveFilename: "Lab05_Isotherms.png",
    lineTypes: {
      0: {
        color: "#0070FF",
        width: 3,
        label: "35° T",
        dash: [10, 10],
      },
      1: {
        color: "#00B050",
        width: 3,
        label: "40° T",
        dash: [10, 10],
      },
      2: {
        color: "#7500FF",
        width: 3,
        label: "45° T",
        dash: [10, 10],
      },
      3: {
        color: "#E00000",
        width: 3,
        label: "45° Td",
        dash: [10, 10],
      },
    },
  },

  // Form Export Configuration
  questions: [
    // Question 1 (4 points)
    { id: "q1_pressure", key: "Q1_PRESSURE" },
    { id: "q1_temp", key: "Q1_TEMP" },
    { id: "q1_dewpoint", key: "Q1_DEWPOINT" },
    { id: "q1_sky", key: "Q1_SKY" },

    // Question 2 (8 points)
    { id: "q2_weather", key: "Q2_WEATHER" },
    { id: "q2_pressure", key: "Q2_PRESSURE" },
    { id: "q2_temp", key: "Q2_TEMP" },
    { id: "q2_dewpoint", key: "Q2_DEWPOINT" },
    { id: "q2_sky", key: "Q2_SKY" },
    { id: "q2_windspeed", key: "Q2_WINDSPEED" },
    { id: "q2_winddir", key: "Q2_WINDDIR" },
    { id: "q2_pressurechange", key: "Q2_PRESSURECHANGE" },
    { id: "q2_precipamount", key: "Q2_PRECIPAMOUNT" },

    // Question 3 (6 points) - Station Model Builder
    {
      key: "Q3_NOTE",
      note: "Interactive station model builder - see uploaded image",
    },

    // Question 4 (4 points) - Isodrosotherm
    { key: "Q4_NOTE", note: "45F isodrosotherm drawing - see uploaded image" },

    // Question 5 (8 points) - Isotherms
    {
      key: "Q5_NOTE",
      note: "35F, 40F, 45F isotherms drawing - see uploaded image",
    },
  ],
};
