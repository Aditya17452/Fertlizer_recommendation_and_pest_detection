from flask import Flask, request, jsonify
from flask_cors import CORS
from app import get_fertilizer_recommendation, generate_remark  # import your function

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend JS can call the API

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    print("Received JSON:", data)  # 👈 Add this line

    try:
        ph = float(data.get("ph", 0))
        soil_type = int(data.get("soilType", 0))
        crop_type = int(data.get("cropType", 0))
        potassium = float(data.get("potassium", 0))
        carbon = float(data.get("carbon", 0))
        nitrogen = float(data.get("nitrogen", 0))

        moisture = float(data.get("moisture", 0))
        phosphorous = float(data.get("phosphorous", 0))
        rainfall = float(data.get("rainfall", 0))
        temperature = float(data.get("temperature", 0))

        input_params = {
            "Temperature": temperature,
            "Moisture": moisture,
            "Rainfall": rainfall,
            "pH": ph,
            "Nitrogen": nitrogen,
            "Phosphorous": phosphorous,
            "Potassium": potassium,
            "Carbon": carbon,
            "Soil_Type": soil_type,
            "Crop_Type": crop_type,
        
        }

        fert_name, fert_dosage = get_fertilizer_recommendation(input_params)
        remark = generate_remark(fert_name)

        return jsonify({
            "fertilizer": fert_name,
            "dosage": f"{fert_dosage:.2f} kg/acre",
            "remark": remark
        })

    except Exception as e:
        print("💥 Error occurred:", e)  # Full trace
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
