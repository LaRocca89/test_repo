from PIL import Image
import pytesseract
import glob

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract\tesseract.exe'
pdf_files_to_read = glob.glob("*.jpg")


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

text_file = open("result.txt", "w")

for f in pdf_files_to_read:
    text_file.write(ocr_core(f))

text_file.close()