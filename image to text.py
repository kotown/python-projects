import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:/Users/Bramwel/OneDrive/Documents/Code/python/tesseract-main/tesseract-main"#path to tesseract

def convert():
    img = Image.open('img.jpg')
    