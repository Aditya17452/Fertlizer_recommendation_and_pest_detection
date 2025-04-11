from flask import Flask, request, jsonify
from flask_cors import CORS
from pest_detection  import detect_pests  
from flask import send_from_directory
from werkzeug.utils import secure_filename
import os
# print("Current working dir:", os.getcwd())


app = Flask(__name__)
CORS(app)  # Allow frontend to connect

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/outputs/<filename>')
def send_annotated_image(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['image']
    filename = secure_filename(file.filename)
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(image_path)

    output_image_path = os.path.join(OUTPUT_FOLDER, filename)
    results = detect_pests(image_path, output_image_path)

    return jsonify({
        'detections': results,
        'annotated_image': f"/{output_image_path}"  # Optionally return image path
    })

if __name__ == '__main__':
    app.run(debug=True)
