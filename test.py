import pytesseract
import cv2


def OCR():
    global SCORe
    a = r'D:\Capture Information file (python)\Binaryzation\test5.jpg'
    i = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'
    im = cv2.imread(a)
    img = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    text1 = pytesseract.image_to_string(img, lang='chi_sim', config=i, )
    text = text1.replace(' ', '').strip()
    print(text)
