from PIL import Image
from utils.ocr import extract_text


image = Image.open("test_document.jpg")

text, image_type, best_psm, confidence = extract_text(
    image,
    language="eng"
)

print("\n========== OCR RESULT ==========\n")

print(text)

print("\n========== OCR INFORMATION ==========\n")

print("Best Image:", image_type)

print("Best PSM Mode:", best_psm)

print("OCR Confidence:", round(confidence, 2), "%")