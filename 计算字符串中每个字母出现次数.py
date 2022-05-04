# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 11:28:48 2021

@author: 92500
"""
str = input('输入一串字母：')
str = str.lower()
dict = {}
for i in str:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)
