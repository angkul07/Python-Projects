import cv2
import pytesseract
from pathlib import Path
from pdf2image import convert_from_path

def image_to_text(input_path):

    img = cv2.imread(input_path)
    text = pytesseract.image_to_string(img)

    return text.strip()

def pdf_to_image(pdf_path, output_folder: str="."):
    if not Path(output_folder).exists():
        Path(output_folder).mkdir()

    pages = convert_from_path(pdf_path, output_folder=output_folder, fmt="png")

    return pages

pdf_path = "lecun-89e.pdf"
pdf_to_image(pdf_path, output_folder="document")

# Path of the image which we want to convert to searchable pdf
final_img = "document/7b8e8773-639e-466b-9f63-4127c4d1d88a-08.png"

output_pdf = pytesseract.image_to_pdf_or_hocr(final_img)

with open("your_pdf.pdf", "w+b") as f:
    f.write(bytearray(output_pdf))
