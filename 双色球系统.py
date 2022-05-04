# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 12:59:55 2021

@author: 92500
"""

import random as ra
import time


def progress_bar():
    print('开奖中', end='')
    for j in range(4):
        for i in range(2):
            print('/', end='')
            time.sleep(0.28)
            print('\b', end='')
            print('-', end='')
            time.sleep(0.28)
            print('\b', end='')
            print('\\', end='')
            time.sleep(0.28)
            print('\b', end='')
            print('*', end='')
            print(' ', end='')


list_boll = []  # 球池列表
boll = []  # 奖池列表
list_del = []  # 保存奖池列表
for i in range(1, 34):
    list_boll.append(i)  # 创建球池
for l in range(6):
    j = ra.randint(1, len(list_boll))  # 随机创建红球奖池
    k = list_boll.pop(j - 1)
    boll.append(k)
blueboll = ra.randint(1, 17)  # 随机创建蓝球中奖号码
list_del.extend(boll)  # 用list_del保存红球奖池，因为红球奖池列表boll后期会逐个删除
an = input('是否显示开奖号码？ （T/F）')
if an.upper() == 'T':
    print(boll, blueboll)

p = 1
list_user = []  # 记录用户买到的红球号码
m = 0
while m < 6:
    m += 1
    user_red = input('请输入您想买的红球号码，第%d个:' % p)
    if user_red.isdigit() and 0 < int(user_red) < 34:  # 判断用户输入的是否为数字
        list_user.append(int(user_red))
    else:
        m -= 1
        continue
    p += 1

g = 0
while g < 1:
    g += 1
    user_blue1 = input('请输入您想买的蓝球号码：')
    if user_blue1.isdigit():
        user_blue = int(user_blue1)
    else:
        g -= 1
        continue

print('\n')
time.sleep(0.3)
print('您买到的是：', end='')
list_user.sort(reverse=False)  # 排序
print(list_user, user_blue)
time.sleep(0.3)
print('\n')

progress_bar()

q = 0
r = 0  # 记录红球中奖次数
r1 = 0  # 记录蓝球中奖次数
for n in range(6):
    if list_user[q] in boll:  # 判断中奖
        r += 1
        q += 1
        boll.remove(list_user[q - 1])  # 将已中奖的号码从奖池中删除，防止二次判断
    else:
        q += 1
        continue

print('\n')
if blueboll == user_blue:
    r1 += 1
if r1 == 1 and r == 6:
    print('\033[1;31m 恭喜你，一等奖\n \033[0m')
elif r == 6:
    print('\033[1;31m 恭喜你，二等奖\n \033[0m')
elif r1 == 1 and r == 5:
    print('\033[1;31m 恭喜你，三等奖\n \033[0m')
elif (r1 == 1 and r == 4) or r == 5:
    print('\033[1;35m 恭喜你，四等奖\n \033[0m')
elif (r1 == 1 and r == 3) or r == 4:
    print('\033[1;35m 恭喜你，五等奖\n \033[0m')
elif (r1 == 1 and r == 1) or (r1 == 1 and r == 2) or (r1 == 1 and r == 0):
    print('\033[1;35m 恭喜你，六等奖\n \033[0m')
else:
    print('\033[4;32m很遗憾，未中奖\n\033[0m')

list_del.sort(reverse=False)  # 排序
print('开奖号码是：', end='')
print(list_del, blueboll)
