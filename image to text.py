import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"path to tesseract"#path to tesseract

#function to read text in picture
def convert():
    img = Image.open('img.jpg')
    text = pytesseract.image_to_string(img)
    print(text)
convert()
