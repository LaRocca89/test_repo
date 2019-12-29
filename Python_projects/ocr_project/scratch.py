import pytesseract
from PIL import Image
patch = './pdf_2_jpg/image.jpg'
multi = Image.open(patch)
result = pytesseract.image_to_string(multi)