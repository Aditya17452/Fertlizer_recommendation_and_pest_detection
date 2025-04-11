document.addEventListener("DOMContentLoaded", function () {
    // Example dynamic data (this can be fetched from an API later)
    const soilData = {
        ph: 6.8,
        nitrogen: 45,
        phosphorus: 30,
        potassium: 20,
    };

    // Update table values
    document.getElementById("ph-value").textContent = soilData.ph;
    document.getElementById("nitrogen-value").textContent = soilData.nitrogen;
    document.getElementById("phosphorus-value").textContent = soilData.phosphorus;
    document.getElementById("potassium-value").textContent = soilData.potassium;

    // Generate remarks
    document.getElementById("ph-remark").textContent = soilData.ph > 7 ? "Slightly Alkaline" : "Neutral";
    document.getElementById("nitrogen-remark").textContent = soilData.nitrogen < 50 ? "Low" : "Sufficient";
    document.getElementById("phosphorus-remark").textContent = soilData.phosphorus < 40 ? "Moderate" : "High";
    document.getElementById("potassium-remark").textContent = soilData.potassium < 30 ? "Low" : "Good";

    // Fertilizer recommendation logic
    let recommendation = "Balanced NPK Fertilizer";
    let dosage = "50 kg/acre";
    let advice = "Maintain organic compost use.";

    if (soilData.nitrogen < 50) {
        recommendation = "Urea Fertilizer";
        dosage = "60 kg/acre";
        advice = "Increase nitrogen input.";
    } else if (soilData.phosphorus < 40) {
        recommendation = "DAP Fertilizer";
        dosage = "45 kg/acre";
        advice = "Apply phosphorus-rich fertilizer.";
    } else if (soilData.potassium < 30) {
        recommendation = "MOP Fertilizer";
        dosage = "40 kg/acre";
        advice = "Increase potassium levels.";
    }

    // Update recommendations section
    document.getElementById("fertilizer").textContent = recommendation;
    document.getElementById("dosage").textContent = dosage;
    document.getElementById("advice").textContent = advice;
});