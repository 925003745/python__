# -*- coding: utf-8 -*-                                                       
# @Time       :   2021/6/10 18:33
import time

import pygame

WIN_WIDTH = 400
WIN_HEIGHT = 600
FPS = 60

pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('显示图形')
window.fill((255, 255, 255))
pygame.display.flip()

y = 100
x = 100
r = 10
flag = 1
pygame.draw.circle(window, (255, 0, 0), (100, y), r)
pygame.display.update()

while True:
    # fill()把整个界面填成某个颜色
    # window.fill((255, 255, 255))
    pygame.draw.circle(window, (255, 255, 255), (x, y), r)
    y += flag
    pygame.draw.circle(window, (255, 0, 0), (x, y), r)
    pygame.display.update()
    time.sleep(0.005)
    if y + r >= WIN_HEIGHT:
        flag *= -1
    if y + r <= 0:
        flag *= -1

    for event in pygame.event.get():  # pygame.event.get()为获取事件
        if event.type == pygame.QUIT:  # 检测到时间类型为pygame.QUIT时执行exit()
            # pygame.QUIT为模块已有type，判断即可
            exit()
