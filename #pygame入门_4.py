# -*- coding: utf-8 -*-                                                       
# @Time       :   2021/6/10 18:26
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

r = 10
y = 250
while True:
    r += 1
    y += 0
    pygame.draw.circle(window, (0, 0, 255), (200, y), r)
    pygame.display.update()
    time.sleep(0.01)

    for event in pygame.event.get():  # pygame.event.get()为获取事件
        if event.type == pygame.QUIT:  # 检测到时间类型为pygame.QUIT时执行exit()
            # pygame.QUIT为模块已有type，判断即可
            exit()
