import pytesseract
import cv2
from PIL import Image


# 此程序识别正确率比较感人，谨慎使用

# Binaryzation()为图像二值化模块，背景为纯色或接近纯色时略有作用，其他情况时纯粹帮倒忙，待调整
# 该模块当前未被调用，更改33和35行可启用此模块
# def Binaryzation():
#     img = Image.open(r'D:\Capture Information file (python)\Binaryzation\test.jpg')
#
#     # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白
#     Img = img.convert('L')
#     Img.save("test1.jpg")
#
#     # 自定义灰度界限，大于这个值为黑色，小于这个值为白色
#     threshold = 50
#
#     table = []
#     for i in range(256):
#         if i < threshold:
#             table.append(0)
#         else:
#             table.append(1)
#
#     # 图片二值化
#     photo = Img.point(table, '1')
#     photo.save(r"D:\Capture Information file (python)\Binaryzation\test2.jpg")


def OCR():
    # Binaryzation()
    global text
    a = r'D:\Capture Information file (python)\Binaryzation\test5'
    i = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'
    # 解决编码问题
    im = cv2.imread(a)
    img = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    # imread读到的是BGR格式，cvColor用于将其转为RGB
    text1 = pytesseract.image_to_string(img, lang='chi_sim', config=i)
    # chi_sim表示中文简体，英文为eng,更多字体需要去官网下载更多包
    text = text1.replace(' ', '').strip()
    print(text)
    files()


def files():
    global text
    file_1 = open(r"D:\Capture Information file (python)\OCR文字识别.txt", "w+")
    file_1.write(text)
    file_1.close()


text = ''

if __name__ == "__main__":
    OCR()
