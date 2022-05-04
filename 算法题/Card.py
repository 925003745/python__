# -*- coding: utf-8 -*-                                                       
# @Time       :   2021/11/13 22:19
num = 0
for i in range(1, 10000):
    num += str(i).count("1")
    if 2021 == num:
        print(i)
        break
