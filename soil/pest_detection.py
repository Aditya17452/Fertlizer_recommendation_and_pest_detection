# import torch
# from ultralytics import YOLO
# from PIL import Image, ImageDraw, ImageFont
# import os

# # Load YOLOv9 model from your trained weights
# model = YOLO("model/best.pt")

# # Predefined treatments for your specific pests
# PEST_TREATMENTS = {
#     "aphids": "Use insecticidal soap or neem oil. Encourage natural predators like ladybugs.",
#     "army worm": "Apply Bacillus thuringiensis (Bt) or spinosad. Remove infected plants.",
#     "black cutworm": "Use pheromone traps and apply Bt in early stages.",
#     "corn borer": "Apply Bt spray and rotate crops regularly.",
#     "grub": "Apply neem oil or milky spore. Water deeply before treatment.",
#     "large cutworm": "Till the soil before planting. Use diatomaceous earth around plants.",
#     "mole cricket": "Apply insecticidal soap. Use nematodes for biological control.",
#     "peach borer": "Use pheromone traps and apply insecticide to the base of trunks.",
#     "potosiabre vitarsis": "Use light traps. Apply appropriate insecticides after consulting experts.",
#     "red spider": "Use miticides. Encourage predatory mites and maintain humidity.",
#     "white margined moth": "Apply Bt spray. Remove larvae manually if infestation is low.",
#     "wireworm": "Rotate crops. Apply insecticides during planting if high infestation.",
#     "yellow cutworm": "Use baited traps. Apply insecticides at dusk when active.",
# }

# def detect_pests(image_path, output_image_path=None):
#     """
#     Detects pests in an image using a trained YOLOv9 model.
    
#     Args:
#         image_path (str): Path to the input image.
#         output_image_path (str, optional): If provided, saves an annotated output image.

#     Returns:
#         List of dicts containing detected pest info and treatment.
#     """
#     print(f"Running detection on: {image_path}")    # remove


#     results = model(image_path)

#     print("Raw results:", results)         # remove
    
#     detections = results.pandas().xyxy[0]  # Get detections as a pandas DataFrame

#     print("Detections:", detections)  # remove

#     pest_results = []
#     image = Image.open(image_path).convert("RGB")
#     draw = ImageDraw.Draw(image)

#     try:
#         font = ImageFont.truetype("arial.ttf", size=16)
#     except:
#         font = ImageFont.load_default()

#     for _, row in detections.iterrows():
#         class_name = row['name']
#         confidence = float(row['confidence'])
#         bbox = [float(row['xmin']), float(row['ymin']), float(row['xmax']), float(row['ymax'])]

#         treatment = PEST_TREATMENTS.get(class_name.lower(), "No treatment info available.")

#         pest_info = {
#             'class': class_name,
#             'confidence': round(confidence, 2),
#             'bbox': bbox,
#             'treatment': treatment
#         }
#         pest_results.append(pest_info)

#         # Draw bounding box and label
#         if output_image_path:
#             draw.rectangle(bbox, outline="red", width=2)
#             label = f"{class_name} ({confidence:.2f})"
#             draw.text((bbox[0], bbox[1] - 10), label, fill="red", font=font)

#     # Save annotated image
#     if output_image_path:
#         os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
#         image.save(output_image_path)

#     return pest_results
#     #return pest_results, image if output_image_path is None else pest_results

# # def detect_pests(image_path, output_image_path=None):
# #     print(f"Running detection on: {image_path}")
# #     results = model(image_path)
# #     detections = results.pandas().xyxy[0]

# #     pest_results = []
# #     image = Image.open(image_path).convert("RGB")
# #     draw = ImageDraw.Draw(image)

# #     try:
# #         font = ImageFont.truetype("arial.ttf", size=16)
# #     except:
# #         font = ImageFont.load_default()

# #     for _, row in detections.iterrows():
# #         class_name = row['name']
# #         confidence = float(row['confidence'])
# #         bbox = [float(row['xmin']), float(row['ymin']), float(row['xmax']), float(row['ymax'])]

# #         treatment = PEST_TREATMENTS.get(class_name.lower(), "No treatment info available.")

# #         pest_info = {
# #             'class': class_name,
# #             'confidence': round(confidence, 2),
# #             'bbox': bbox,
# #             'treatment': treatment
# #         }
# #         pest_results.append(pest_info)

# #         # Draw box and label
# #         if output_image_path:
# #             draw.rectangle(bbox, outline="red", width=2)
# #             label = f"{class_name} ({confidence:.2f})"
# #             draw.text((bbox[0], bbox[1] - 10), label, fill="red", font=font)

# #     if output_image_path:
# #         os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
# #         image.save(output_image_path)

# #     return pest_results









import torch
from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont
import os

# Trained YOLO weights live at the repository root (best.pt)
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "best.pt")
model = YOLO(MODEL_PATH)

PEST_TREATMENTS = {
    "aphids": "Use insecticidal soap or neem oil. Encourage natural predators like ladybugs.",
    "army worm": "Apply Bacillus thuringiensis (Bt) or spinosad. Remove infected plants.",
    "black cutworm": "Use pheromone traps and apply Bt in early stages.",
    "corn borer": "Apply Bt spray and rotate crops regularly.",
    "grub": "Apply neem oil or milky spore. Water deeply before treatment.",
    "large cutworm": "Till the soil before planting. Use diatomaceous earth around plants.",
    "mole cricket": "Apply insecticidal soap. Use nematodes for biological control.",
    "peach borer": "Use pheromone traps and apply insecticide to the base of trunks.",
    "potosiabre vitarsis": "Use light traps. Apply appropriate insecticides after consulting experts.",
    "red spider": "Use miticides. Encourage predatory mites and maintain humidity.",
    "white margined moth": "Apply Bt spray. Remove larvae manually if infestation is low.",
    "wireworm": "Rotate crops. Apply insecticides during planting if high infestation.",
    "yellow cutworm": "Use baited traps. Apply insecticides at dusk when active.",
}

def detect_pests(image_path, output_image_path=None):
    results = model(image_path)[0]
    pest_results = []

    boxes = results.boxes
    class_ids = boxes.cls.cpu().numpy().astype(int)
    confidences = boxes.conf.cpu().numpy()
    bboxes = boxes.xyxy.cpu().numpy()  # [xmin, ymin, xmax, ymax]

    image = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", size=16)
    except:
        font = ImageFont.load_default()

    for i in range(len(class_ids)):
        class_id = class_ids[i]
        class_name = results.names[class_id]
        confidence = float(confidences[i])
        bbox = bboxes[i].tolist()

        treatment = PEST_TREATMENTS.get(class_name.lower(), "No treatment info available.")

        pest_info = {
            'class': class_name,
            'confidence': round(confidence, 2),
            'bbox': bbox,
            'treatment': treatment
        }
        pest_results.append(pest_info)

        if output_image_path:
            draw.rectangle(bbox, outline="red", width=2)
            label = f"{class_name} ({confidence:.2f})"
            draw.text((bbox[0], bbox[1] - 10), label, fill="red", font=font)

    if output_image_path:
        os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
        image.save(output_image_path)

    return pest_results
