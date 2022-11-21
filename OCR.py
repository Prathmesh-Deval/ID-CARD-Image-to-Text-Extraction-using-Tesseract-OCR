import cv2
import pytesseract
import os
from PIL import Image

#provide tesseract path to your system
p=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = p

#provide aadhar card/pan card high defination image from which we need to extract text

img_path = 'test.jpeg'
image= cv2.imread(img_path)

#convert the image to gray scale and resize it to detect proper edges and features
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
gray = cv2.bilateralFilter(thresh, 9, 75, 75)

#save our preprocessed image
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

#use pytesseract module to detect text from given image
text = pytesseract.image_to_string(Image.open(filename), lang = 'eng')

#save detected text into a .txt file
text_output = open('Image_to_text.txt', 'w', encoding='utf-8')
text_output.write(text)
text_output.close()

