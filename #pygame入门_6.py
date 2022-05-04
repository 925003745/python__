# -*- coding: utf-8 -*-                                                       
# @Time       :   2021/6/10 18:43
import pygame

WIN_WIDTH = 400
WIN_HEIGHT = 600
FPS = 60

pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('显示图形')
window.fill((255, 255, 255))
pygame.display.flip()

count = 0
while True:
    for event in pygame.event.get():  # pygame.event.get()为获取事件
        count += 1
        # print(count)
        # print(event)
        '''
        QUIT 点击关闭时的时间
        
        '''
        if event.type == pygame.QUIT:  # 检测到时间类型为pygame.QUIT时执行exit()
            # pygame.QUIT为模块已有type，判断即可
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('鼠标按下')
        elif event.type == pygame.MOUSEBUTTONUP:
            print('鼠标 松开')
        elif event.type == pygame.MOUSEMOTION:
            pygame.draw.circle(window, (0, 0, 0), event.pos, 1)
            pygame.display.update()
            print(f'鼠标移动,坐标：{event.pos}')
