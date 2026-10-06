import cv2
import numpy as np
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def prepare_images(image):
    if isinstance(image, Image.Image):
        image = np.array(image)

    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    else:
        gray = image

    height, width = gray.shape

    if width < 1600:
        scale = 1600 / width

        gray = cv2.resize(
            gray,
            None,
            fx=scale,
            fy=scale,
            interpolation=cv2.INTER_CUBIC
        )

    original = gray

    blur = cv2.GaussianBlur(
        gray,
        (3, 3),
        0
    )

    threshold = cv2.adaptiveThreshold(
        blur,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        11
    )

    return original, threshold


def run_ocr(image, psm, language="eng"):

    config = f"--oem 3 --psm {psm}"

    data = pytesseract.image_to_data(
        image,
        lang=language,
        config=config,
        output_type=pytesseract.Output.DICT
    )

    words = []
    confidences = []

    for i in range(len(data["text"])):

        word = data["text"][i].strip()

        try:
            confidence = float(data["conf"][i])
        except ValueError:
            confidence = -1

        if word and confidence >= 0:

            words.append(word)
            confidences.append(confidence)

    text = " ".join(words)

    if confidences:
        average_confidence = sum(confidences) / len(confidences)
    else:
        average_confidence = 0

    return text, average_confidence


def extract_text(image, language="eng"):

    original, processed = prepare_images(image)

    images = [
        ("original", original),
        ("processed", processed)
    ]

    psm_modes = [6, 4, 11]

    results = []

    for image_type, current_image in images:

        for psm in psm_modes:

            text, confidence = run_ocr(
                current_image,
                psm,
                language
            )

            results.append({
                "image_type": image_type,
                "psm": psm,
                "text": text,
                "confidence": confidence
            })

    best_result = max(
        results,
        key=lambda x: x["confidence"]
    )

    return (
        best_result["text"],
        best_result["image_type"],
        best_result["psm"],
        best_result["confidence"]
    )