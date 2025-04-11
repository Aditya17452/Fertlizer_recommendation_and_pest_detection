document.getElementById("analyzeSoil").addEventListener("click", function () {
    const ph = parseFloat(document.getElementById("ph").value);
    const nitrogen = parseFloat(document.getElementById("nitrogen").value);
    const phosphorus = parseFloat(document.getElementById("phosphorus").value);
    const potassium = parseFloat(document.getElementById("potassium").value);
    const moisture = document.getElementById("moisture").value;
    const soilType = document.getElementById("soilType").value;

    let recommendation = "General Fertilizer";
    let remark = "Soil condition is optimal.";

    if (ph > 8) {
        remark = "Soil is alkaline. Consider adding organic matter.";
        recommendation = "Organic Compost";
    } else if (ph < 5.5) {
        remark = "Soil is acidic. Consider using lime.";
        recommendation = "Lime Treatment";
    }

    if (nitrogen < 50) {
        recommendation = "Urea Fertilizer";
        remark = "Low nitrogen detected. Use nitrogen-based fertilizer.";
    } else if (phosphorus < 40) {
        recommendation = "DAP Fertilizer";
        remark = "Low phosphorus detected. Use phosphorus-based fertilizer.";
    } else if (potassium < 50) {
        recommendation = "MOP Fertilizer";
        remark = "Low potassium detected. Use potassium-based fertilizer.";
    }

    document.getElementById("fertilizer").textContent = recommendation;
    document.getElementById("remark").textContent = remark;
});