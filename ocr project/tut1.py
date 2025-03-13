import cv2
import pytesseract
from pytesseract import Output

# json and pprint print the tuple, dict in a pretty format
import json
import pprint

import pathlib
from pathlib import Path
from pdf2image import convert_from_path


text_path = "images/image1.png"
img = cv2.imread(text_path)

# text = pytesseract.image_to_string(img)
# print(text)

def image_to_text(input_path):

    img = cv2.imread(input_path)
    text = pytesseract.image_to_string(img)
    
    return text.strip()

medium_text_path = "images/image2.png"

extracted_text = image_to_text(medium_text_path)
# print(extracted_text)


""" drawing bounding boxes around text
first step: pass a loaded image to the image_to_data and which will 
return the image details(Output.Dict)"""
# data = pytesseract.image_to_data(img, output_type=Output.DICT)


# print(data)
# print(json.dumps(data, sort_keys=True))
#pprint.pprint(data)
# print(len(data["text"]))  # 11: this mean pytesseract drew 11 boxes


# def draw_bounding_boxes(input_img_path, output_path):
#     img = cv2.imread(input_img_path)

#     data = pytesseract.image_to_data(img, output_type=Output.DICT)
#     # now lets draw the boxes
#     n_boxes = len(data["text"])

#     for i in range(n_boxes):
#         # if conf=-1 then skip it --> skipping larger bounding boxes(to keep image clean)
#         if data["conf"][i] == -1:
#             continue

#         # Coordinates
#         x, y = data["left"][i], data["top"][i]
#         w, h = data["width"][i], data["height"][i]

#         # Corners
#         top_left = (x, y)
#         bottom_right = (x+w, y+h)

#         # Box params
#         green = (0, 255, 0)
#         thickness = 1 # pixels

#         cv2.rectangle(
#             img = img, pt1=top_left, pt2=bottom_right, color=green, thickness=thickness
#         )

#     # save the image
#     cv2.imwrite(output_path, img)

# output_path = "images/medium_text_with_boxes.png"
# draw_bounding_boxes(medium_text_path, output_path)

def pdf_to_image(pdf_path, output_folder: str = "."):
    if not Path(output_folder).exists():
        Path(output_folder).mkdir()

    pages = convert_from_path(pdf_path, output_folder=output_folder, fmt="png")

    return pages

pdf_path = "lecun-89e.pdf"
pdf_to_image(pdf_path, output_folder="document")

scanned_img_path = "document/33de68eb-6737-450e-8266-712f46ec6e2b-09.png"

# print(image_to_text(scanned_img_path))

raw_pdf = pytesseract.image_to_pdf_or_hocr(scanned_img_path)

with open("search.pdf", "w+b") as f:
    f.write(bytearray(raw_pdf))
