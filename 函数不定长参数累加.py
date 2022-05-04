# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 15:50:46 2021

@author: 92500
"""


def a(i, *j):
    sum = i
    for k in j:
        sum += k
    return sum


print(a(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
