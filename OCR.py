import cv2
import pytesseract
import os
from PIL import Image

p=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = p

img_path = '5.jpeg'
image= cv2.imread(img_path)
img2 = image.copy()


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
gray = cv2.bilateralFilter(thresh, 9, 75, 75)


filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

text = pytesseract.image_to_string(Image.open(filename), lang = 'eng')
text_output = open('Image_to_text.txt', 'w', encoding='utf-8')
text_output.write(text)
text_output.close()

