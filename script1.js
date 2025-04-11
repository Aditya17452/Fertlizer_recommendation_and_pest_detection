// Navigation Handling
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        document.querySelectorAll('.nav-links a').forEach(l => l.classList.remove('active'));
        link.classList.add('active');
        document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
        document.querySelector(link.getAttribute('href')).classList.add('active');
    });
});



// Soil Analysis Form
document.getElementById('soilForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const soilData = {
        ph: parseFloat(document.getElementById('ph').value),
        nitrogen: parseFloat(document.getElementById('nitrogen').value),
        phosphorus: parseFloat(document.getElementById('phosphorus').value),
        potassium: parseFloat(document.getElementById('potassium').value)
    };

    const recommendation = analyzeSoil(soilData);
    generateReport(recommendation);
});

// Pest Detection
document.querySelector('.upload-area').addEventListener('click', function() {
    document.getElementById('pestImage').click();
});

document.getElementById('pestImage').addEventListener('change', function(e) {
    if (e.target.files.length > 0) {
        detectPest(e.target.files[0]);
    }
});

// Analysis Functions
function analyzeSoil(data) {
    let recommendations = [];
    
    if (data.ph < 6) {
        recommendations.push("Soil is acidic - apply lime (2-5 tons/ha)");
    } else if (data.ph > 7.5) {
        recommendations.push("Soil is alkaline - apply sulfur (1-3 kg/acre)");
    }
    
    if (data.nitrogen < 20) {
        recommendations.push("Nitrogen deficient - apply urea (100-150 kg/ha)");
    }
    
    if (data.phosphorus < 15) {
        recommendations.push("Phosphorus deficient - apply DAP (50-100 kg/ha)");
    }
    
    if (data.potassium < 150) {
        recommendations.push("Potassium deficient - apply MOP (50-100 kg/ha)");
    }
    
    return recommendations.length > 0 ? recommendations : ["Soil parameters are optimal - no fertilizer needed"];
}

function detectPest(imageFile) {
    // Simulate pest detection
    const pestResult = {
        pest: "Aphids",
        severity: "Moderate",
        treatment: "Apply neem oil spray (2.8 tsp per liter) weekly for 3 weeks"
    };
    
    generateReport(null, pestResult);
}

function generateReport(soilRecommendations, pestResult = null) {
    let reportHTML = "<h2>Soil Health Report</h2>";
    
    if (soilRecommendations) {
        reportHTML += "<h3>Soil Analysis Results:</h3><ul>";
        soilRecommendations.forEach(rec => {
            reportHTML += <li>${rec}</li>;
        });
        reportHTML += "</ul>";
    }
    
    if (pestResult) {
        reportHTML += `
            <h3>Pest Detection Results:</h3>
            <p><strong>Detected Pest:</strong> ${pestResult.pest}</p>
            <p><strong>Severity:</strong> ${pestResult.severity}</p>
            <p><strong>Recommended Treatment:</strong> ${pestResult.treatment}</p>
        `;
    }
    
    document.getElementById('report-content').innerHTML = reportHTML;
    document.querySelector('.nav-links a[href="#report"]').click();
}

document.querySelectorAll(".nav-links a").forEach(link => {
    link.addEventListener("click", function() {
        document.querySelectorAll(".section").forEach(section => {
            section.classList.remove("active");
        });

        const target = document.querySelector(this.getAttribute("href"));
        if (target) {
            target.classList.add("active");
        }
    });
});

document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', (e) => {
        const targetSection = link.getAttribute('href');
        
        if (targetSection === "login.html") {
            window.location.href = "login.html"; // Redirects to login page
            return; // Stop further execution
        }

        e.preventDefault();
        document.querySelectorAll('.nav-links a').forEach(l => l.classList.remove('active'));
        link.classList.add('active');
        document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
        document.querySelector(targetSection)?.classList.add('active');
    });
});