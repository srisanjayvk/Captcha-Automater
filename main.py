import pytesseract as pyt
import cv2

img = cv2.imread("math.png")

pyt.pytesseract.tesseract_cmd = "C:\\Users\\vjpra\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

text = pyt.image_to_string(img)
result = eval(text)
print(result)