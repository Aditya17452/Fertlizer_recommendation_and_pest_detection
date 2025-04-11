from flask import Flask, render_template, request
from ultralytics import YOLO
from PIL import Image, ImageDraw
import os
import uuid

app = Flask(__name__)
model = YOLO("best.pt")

PEST_TREATMENTS = {
    'aphids': 'Use neem oil or insecticidal soap.',
    'beetle': 'Handpick or use neem-based pesticide.',
    'caterpillar': 'Use BT-based pesticide or manually remove.',
    'mite': 'Spray with miticide or insecticidal soap.',
    'whitefly': 'Use yellow sticky traps or neem oil.',
    'thrips': 'Use blue sticky traps or spinosad spray.',
}

def detect_pests(image_path, output_path):
    results = model(image_path)
    names = model.names
    result = results[0]
    pest_results = []

    image = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(image)

    for box in result.boxes:
        cls_id = int(box.cls[0])
        class_name = names[cls_id]
        conf = float(box.conf[0])
        treatment = PEST_TREATMENTS.get(class_name, "No treatment found.")

        pest_results.append({
            'class': class_name,
            'confidence': f"{conf:.2f}",
            'treatment': treatment
        })

        x1, y1, x2, y2 = box.xyxy[0]
        draw.rectangle([x1, y1, x2, y2], outline='red', width=3)
        draw.text((x1, y1), f"{class_name} ({conf:.2f})", fill='red')

    image.save(output_path)
    return pest_results

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['image']
        if image:
            # Generate a unique filename with correct extension
            ext = image.filename.split('.')[-1].lower()
            allowed_exts = ['jpg', 'jpeg', 'png', 'webp']
            if ext not in allowed_exts:
                return "Unsupported file format. Please upload JPG, PNG, or WEBP."

            unique_id = str(uuid.uuid4())
            input_path = f'static/input_{unique_id}.{ext}'
            output_path = f'static/output_{unique_id}.png'

            image.save(input_path)

            # Convert to RGB .png internally for consistency
            with Image.open(input_path).convert("RGB") as img:
                img.save(input_path)

            results = detect_pests(input_path, output_path)

            return render_template('result.html', pest_results=results, image_path=output_path)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
