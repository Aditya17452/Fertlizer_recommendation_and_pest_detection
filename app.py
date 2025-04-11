import pickle
import pandas as pd

# Mapping dictionaries for reverse lookup
fertilizer_mapping = {
    1: "Compost",
    2: "Balanced NPK Fertilizer",
    3: "Water Retaining Fertilizer",
    4: "Organic Fertilizer",
    5: "Gypsum",
    6: "Lime",
    7: "DAP",
    8: "Urea",
    9: "Muriate of Potash",
    10: "General Purpose Fertilizer"
}

soil_mapping = {
    1: "Loamy Soil",
    2: "Peaty Soil",
    3: "Acidic Soil",
    4: "Neutral Soil",
    5: "Alkaline Soil"
}

crop_mapping = {
    1: "rice", 2: "wheat", 3: "Mung Bean", 4: "Tea", 5: "millet", 6: "maize", 7: "Lentil",
    8: "Jute", 9: "Coffee", 10: "Cotton", 11: "Ground Nut", 12: "Peas", 13: "Rubber",
    14: "Sugarcane", 15: "Tobacco", 16: "Kidney Beans", 17: "Moth Beans", 18: "Coconut",
    19: "Black gram", 20: "Adzuki Beans", 21: "Pigeon Peas", 22: "Chickpea", 23: "banana",
    24: "grapes", 25: "apple", 26: "mango", 27: "muskmelon", 28: "orange", 29: "papaya",
    30: "pomegranate", 31: "watermelon"
}

def load_models():
   # with open("models/fert_name_model.pkl", "rb") as f:
    with open("models/fert_name_model .pkl", "rb") as f:
        name_model = pickle.load(f)
    #with open("models/fert_dosage_model.pkl", "rb") as f:
    with open("models/fert_dosage_model .pkl", "rb") as f:
        dosage_model = pickle.load(f)
    #with open("models/scaler.pkl", "rb") as f:
    with open("models/scaler .pkl", "rb") as f:
        scaler = pickle.load(f)
    return name_model, dosage_model, scaler

def get_fertilizer_recommendation(params):
    name_model, dosage_model, scaler = load_models()

    input_data = pd.DataFrame([params])

    # Scale features
    input_scaled = scaler.transform(input_data)

    # Predict fertilizer name (as code) and dosage
    fert_code = name_model.predict(input_scaled)[0]
    fert_dosage = dosage_model.predict(input_scaled)[0]

    # Map predicted code back to fertilizer name
    fert_name = fertilizer_mapping.get(fert_code, f"Unknown Fertilizer ({fert_code})")

    return fert_name, fert_dosage

def generate_remark(fertilizer_name):
    remarks = {
        "Urea": "Rich in nitrogen, promotes leafy growth.",
        "DAP": "Rich in phosphorus, ideal for root development.",
        "Muriate of Potash": "Contains potassium, strengthens plant immunity.",
        "Compost": "Improves soil structure and microbial activity.",
        "Balanced NPK Fertilizer": "Provides a mix of essential nutrients.",
        "Organic Fertilizer": "Natural and eco-friendly option.",
        "Gypsum": "Improves soil structure and reduces compaction.",
        "Lime": "Adjusts soil pH and adds calcium.",
        "Water Retaining Fertilizer": "Enhances moisture retention in dry soils.",
        "General Purpose Fertilizer": "Suitable for a variety of crops and conditions."
    }
    return remarks.get(fertilizer_name, "No remark available for this fertilizer.")
