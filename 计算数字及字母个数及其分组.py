# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 15:16:46 2021

@author: 92500
"""

str = [[], []]
num = 0
alpha = 0
i = input('请输入一串字符：\n')
for j in i:
    if j.isdigit():
        str[0].append(j)
        num += 1
    elif j in i:
        if j.isalpha():
            str[1].append(j)
            alpha += 1
    else:
        continue

print('数字有%d个，字母有%d个，分别是：\n' % (num, alpha))
print('数字：', end='')
print(str[0])
print('\n')
print('字母：', end='')
print(str[1])
