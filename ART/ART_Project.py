# -*- coding: utf-8 -*-                                                       
# @Time       :   2021/12/28 16:21
import random
import time
from PIL import Image
import pyautogui as pag
import pyperclip as ppp


def ART():
    pag.hotkey('win', 'r')
    pag.typewrite('WeChat')
    pag.keyDown('enter')
    pag.keyDown('enter')

    first = Image.open('search_1.png')

    while True:
        while True:
            F = pag.locateCenterOnScreen(first, confidence=0.9)
            if F is not None:
                break
        pag.click(F.x, F.y)

        boolean = Image.open('Boolean.png')
        B = pag.locateCenterOnScreen(boolean, confidence=0.8)
        if B is not None:
            break
        else:
            continue

    pag.typewrite('lei')  # Step First
    pag.keyDown('enter')
    second = Image.open('lei.png')  # Step Second
    while True:
        S = pag.locateCenterOnScreen(second, confidence=0.8)
        if S is not None:
            break
    pag.click(S.x, S.y)
    str_1 = f'李俊林，今日体温{round(random.uniform(36.1, 36.9), 1)}，张艳林，今日体温{round(random.uniform(36.1, 36.9), 1)}'
    ppp.copy(str_1)
    ppp.paste()
    pag.hotkey('ctrl', 'v')

    time.sleep(2)
    pag.keyDown('enter')


file = open('log.txt', 'a')

while True:
    Now = time.strftime('%H:%M', time.localtime())
    if Now == "09:00" or Now == "14:29":
        print("*")
        ART()
        realNow = time.strftime('%H:%M:%S', time.localtime())
        file.write(f'TimeBoolean : True ; 程序已执行, ExecuteTime: {realNow}' + '\n')
    print(f".")
    file.write(f'TimeBoolean : False ; time : {Now}' + '\n')
    time.sleep(59)
