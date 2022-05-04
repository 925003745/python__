# -*- coding: utf-8 -*-                                                       
# @Time       :   2021/8/27 14:41

from PIL import Image

i = 1
while i <= 29:
    image = Image.open(f'D:\pycharm_community\project\piccc\\{i}.jpg')
    imagechange = image.resize((144, 192))
    imagechange.save(f'D:\pycharm_community\project\pic\\{i}-.jpg')
    i += 1
print("end!")
