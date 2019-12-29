from pdfrw import PdfReader
from pdf2image import convert_from_path

# Read the PDF
ipdf = PdfReader("N314EU.pdf")
# Successfully coverts 1 page of a pdf into a JPEG file.
images = convert_from_path('N314EU.pdf')
for image in images:
    image.save('test.jpg', 'JPEG')

# This actually works.