//   analysis soil button working
    document.getElementById("analyzeSoil").addEventListener("click", () => {
        const carbon = document.getElementById("carbon").value;
        const nitrogen = document.getElementById("nitrogen").value;
        const potassium = document.getElementById("potassium").value;
        const pH = document.getElementById("ph").value;

        validateInputs(carbon, nitrogen, potassium, pH);
    });
