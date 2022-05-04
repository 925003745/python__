# -*- coding: utf-8 -*-                                                       
# @Time       :   2021/8/27 14:33
import os

path = 'D:\pycharm_community\project\piccc'
i = 1

for file in os.listdir(path):
    new_name = file.replace(file, f"{i}.jpg")
    os.rename(os.path.join(path, file), os.path.join(path, new_name))
    i += 1
    print("end!")
