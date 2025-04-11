// image uploadation

document.getElementById("imageUpload").addEventListener("change", function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById("imagePreview").innerHTML = `<img src="${e.target.result}" alt="Uploaded Image" style="max-width:100%; max-height:200px;">`;
        };
        reader.readAsDataURL(file);
    }
});

// Simulated pest detection
function detectPest() {
    const imagePreview = document.getElementById("imagePreview").querySelector("img");
    if(imagePreview )
    {
    document.getElementById("pestName").textContent = "Aphids";
    document.getElementById("pestSeverity").textContent = "High";
    document.getElementById("pestSolution").textContent = "Use neem oil or insecticidal soap.";
    }
    else if(!imagePreview) {
        alert("Error: You have not uploaded the image. Please upload an image first.");
        return;
    }
}

document.getElementById("detectPest").addEventListener("click", detectPest);