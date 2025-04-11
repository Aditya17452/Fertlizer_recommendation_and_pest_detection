# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# from werkzeug.utils import secure_filename
# from pest_detection import detect_pests  
# import os

# app = Flask(__name__)

# # ✅ Enable full CORS access for all domains with credentials
# CORS(app, supports_credentials=True)

# UPLOAD_FOLDER = 'uploads'
# OUTPUT_FOLDER = 'outputs'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# @app.route('/outputs/<filename>')
# def send_annotated_image(filename):
#     return send_from_directory(OUTPUT_FOLDER, filename)

# @app.route('/detect', methods=['POST'])
# def detect():
#     if 'image' not in request.files:
#         return jsonify({'error': 'No file uploaded'}), 400

#     file = request.files['image']
#     filename = secure_filename(file.filename)
#     image_path = os.path.join(UPLOAD_FOLDER, filename)
#     file.save(image_path)

#     output_image_path = os.path.join(OUTPUT_FOLDER, filename)
#     results, _ = detect_pests(image_path, output_image_path)

#     return jsonify({
#         'detections': results,
#         'annotated_image': f"/outputs/{filename}"
#     })

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from pest_detection import detect_pests  
import os
import uuid

app = Flask(__name__)
# CORS(app, supports_credentials=True)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

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
    
    # Use unique filename to avoid cache/overwrite issues
    unique_filename = f"{uuid.uuid4().hex}_{secure_filename(file.filename)}"
    image_path = os.path.join(UPLOAD_FOLDER, unique_filename)
    file.save(image_path)

    output_image_path = os.path.join(OUTPUT_FOLDER, unique_filename)
    results = detect_pests(image_path, output_image_path)

    return jsonify({
        'detections': results,
        'annotated_image': f"/outputs/{unique_filename}"
    })

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
