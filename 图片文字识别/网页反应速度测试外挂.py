import time
import webbrowser
import pyautogui as pag
import tkinter as tk
import pytesseract
import cv2
from PIL import ImageGrab
from ctypes import windll


def prtsc():
    time.sleep(2)
    size = (734, 463, 1420, 775)
    pic = ImageGrab.grab(size)
    pic.save(r"D:\Capture Information file (python)\PrtSc\picture.jpg")


def get_color(x, y):
    gdi32 = windll.gdi32
    user32 = windll.user32
    hdc = user32.GetDC(None)  # 获取颜色值
    pixel = gdi32.GetPixel(hdc, x, y)  # 提取RGB值
    r = pixel & 0x0000ff
    g = (pixel & 0x00ff00) >> 8
    b = pixel >> 16
    return [r, g, b]


def click():
    """请用浏览器打开https://humanbenchmark.com/tests/reactiontime，
    并将pycharm和打开网页的浏览器窗口化，并将pycharm放在屏幕左半边,
    浏览器放在屏幕右半边(先运行此程序，然后点击网页,使网页显示Wait for green)"""

    # 上面三引号里的内容为程序开发初期所需，现已无需执行上述操作，程序全自动运行
    green = [75, 219, 106]
    blue = [43, 135, 209]
    red = [206, 38, 54]
    n = 0
    while n < 5:
        end_time = time.time()
        i = get_color(1437, 430)
        if i == green:
            time.sleep(0.07)
            # 休眠70ms，使最后的平均结果达到三位数，因为两位数的OCR数字内容识别正确率极其感人
            # 也可以删掉，经测最快大约为20ms左右
            # 删掉后最后的弹窗显示99%会报错导致无法正常显示，错误原因为：文字识别函数无法识别到两位数的数字
            # 导致php()未检测到数字，从而导致str_php未赋值，以至于导致ValueError
            pag.click(1437, 430)
            # print(f'点击已完成{n+1}次！')
            n += 1
        elif i == blue:
            time.sleep(1)
            pag.click(1437, 430)
        elif i == red:
            continue
        elif end_time - start > 30:
            exit()


def open_url():
    webbrowser.open('https://humanbenchmark.com/tests/reactiontime', new=0, autoraise=True)


def error_hint():
    window = tk.Tk()
    window.title('Error')
    window.geometry('400x150')
    var = tk.StringVar()
    var.set('Error！！！\n未检测到标准颜色！')
    i1 = tk.Label(window, textvariable=var, bg='white', font=('黑体', 10), width=42, height=7)
    i1.pack()

    window.mainloop()


def end1():
    OCR()
    window = tk.Tk()
    window.title('Prompt')
    window.geometry('500x250')
    var = tk.StringVar()
    var.set(f'程序结束!\n平均反应时间为：{str_php}ms\n'
            f'程序实际平均反应时间为{int(str_php) - 70}ms\n（time.sleep()使用了70ms）')
    i1 = tk.Label(window, textvariable=var, bg='white', font=('黑体', 14), width=42, height=10)
    i1.pack()

    window.mainloop()


def ready():
    window = tk.Tk()
    window.title('Prompt')
    window.geometry('400x150')
    var = tk.StringVar()
    var.set('这是一个自动程序，\n无需点击，关闭此窗口开始自动运行')
    i1 = tk.Label(window, textvariable=var, bg='white', font=('黑体', 10), width=42, height=7)
    i1.pack()

    window.mainloop()


def OCR():
    prtsc()
    global text
    a = r"D:\Capture Information file (python)\PrtSc\picture.jpg"
    i = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'
    # 解决编码问题
    im = cv2.imread(a)
    img = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    # imread读到的是BGR格式，cvColor用于将其转为RGB
    text = pytesseract.image_to_string(img, lang='eng', config=i, )
    # chi_sim表示中文简体，英文为eng,更多字体需要去官网下载更多包
    php()
    files()


def files():
    global text
    file_1 = open(r"D:\Capture Information file (python)\OCR文字识别.txt", "w+")
    file_1.write(text + '\b')
    file_1.close()


def php():
    list_php = []
    global str_php
    for php1 in text:
        if php1.isdigit():
            list_php.append(php1)
    for php2 in list_php:
        str_php += str(php2)


str_php = ''
text = ''
ready()
start = time.time()
open_url()
n1 = 0
while True:
    if get_color(1901, 602) == [43, 135, 209]:
        click()
        end1()
        time.sleep(3)
        exit()
    elif n1 > 20:
        error_hint()
        exit()
    else:
        time.sleep(0.5)
        n1 += 1
        continue
