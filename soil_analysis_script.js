// Wait for the DOM to fully load
// document.addEventListener("DOMContentLoaded", function () {
//     // Smooth scrolling for navigation links
//     const navLinks = document.querySelectorAll(".nav-links a");
    
//     navLinks.forEach(link => {
//         link.addEventListener("click", function (event) {
//             event.preventDefault();
//             const targetId = this.getAttribute("href").substring(1);
//             const targetSection = document.getElementById(targetId);
//             if (targetSection) {
//                 window.scrollTo({
//                     top: targetSection.offsetTop - 50,
//                     behavior: "smooth"
//                 });
//             }
//         });
//     });

//     // Highlight active section in navigation
//     window.addEventListener("scroll", function () {
//         let scrollPosition = window.scrollY;
//         navLinks.forEach(link => {
//             const section = document.querySelector(link.getAttribute("href"));
//             if (section.offsetTop <= scrollPosition + 100 && 
//                 section.offsetTop + section.offsetHeight > scrollPosition + 100) {
//                 navLinks.forEach(nav => nav.classList.remove("active"));
//                 link.classList.add("active");
//             }
//         });
//     });

//     // Newsletter form validation
//     const newsletterForm = document.querySelector(".news-form");
//     if (newsletterForm) {
//         newsletterForm.addEventListener("submit", function (event) {
//             event.preventDefault();
//             const emailInput = document.querySelector(".news-email");
//             const email = emailInput.value.trim();
//             if (validateEmail(email)) {
//                 alert("Thank you for subscribing!");
//                 emailInput.value = ""; // Clear input field after successful submission
//             } else {
//                 alert("Please enter a valid email address.");
//             }
//         });
//     }

//     // Email validation function
//     function validateEmail(email) {
//         const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//         return regex.test(email);
//     }
// });





document.addEventListener("DOMContentLoaded", function () {
    async function fetchWeather() {
        // Get user input values
        const city = document.getElementById("city").value.trim();
        const state = document.getElementById("state").value.trim();
        const country = document.getElementById("country").value.trim();

        // Validate inputs
        if (!city || !country) {
            alert("Please enter at least City and Country!");
            return;
        }

        // API details
        const apiKey = "128e32e9484d4902805165732252603";  // 🔹 Replace with your actual API key
        const locationQuery = state ? `${city},${state},${country}` : `${city},${country}`;
        const apiUrl = `https://api.weatherapi.com/v1/current.json?key=${apiKey}&q=${locationQuery}`;

        try {
            // Fetch data from API
            const response = await fetch(apiUrl);
            if (!response.ok) throw new Error("Weather data not found!");

            const data = await response.json();  // Convert response to JSON

            // Extract required weather details
            const temperature = data.current.temp_c;
            const humidity = data.current.humidity;
            const rainfall = data.current.precip_mm;

            // Display data in HTML
            document.getElementById("temperature").innerText = `${temperature}`;
            document.getElementById("humidity").innerText = `${humidity}`;
            document.getElementById("rainfall").innerText = `${rainfall}`;

            // Show weather card
            document.getElementById("weatherCard").classList.remove("hidden");

        } catch (error) {
            console.error("Error fetching weather data:", error);
            alert("Failed to fetch weather data. Please check your inputs and try again.");
        }
    }

    // Attach function to global scope so it works on button click
    window.fetchWeather = fetchWeather;
});
