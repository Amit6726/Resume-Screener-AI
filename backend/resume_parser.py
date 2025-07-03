import pytesseract
import easyocr
from PIL import Image
import cv2

def extract_text_from_image(file_path, mode="tesseract"):
    if file_path.lower().endswith(".pdf"):
        return "PDF parsing not yet supported."
    
    image = cv2.imread(file_path)

    if mode == "tesseract":
        text = pytesseract.image_to_string(image)
    elif mode == "easyocr":
        reader = easyocr.Reader(['en'], gpu=False)
        results = reader.readtext(image)
        text = " ".join([res[1] for res in results])
    else:
        text = "Invalid OCR mode selected"

    return text
