# -*- coding: utf-8 -*-                                                       
# @Time       :   2021/6/10 19:17
import pygame

WIN_WIDTH = 400
WIN_HEIGHT = 600
FPS = 60

pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('显示图形')
window.fill((255, 255, 255))
pygame.display.flip()

font = pygame.font.SysFont('arial', 50)


while True:
    for event in pygame.event.get():  # pygame.event.get()为获取事件

        if event.type == pygame.QUIT:  # 检测到时间类型为pygame.QUIT时执行exit()
            # pygame.QUIT为模块已有type，判断即可
            exit()
        elif event.type == pygame.KEYDOWN:
            print('按下', end='')
            try:
                window.fill((255, 255, 255))
                text = font.render(chr(event.key), True, (0, 0, 0))
                window.blit(text, (180, 280))
                pygame.display.update()
                print(f'{chr(event.key)}')
            except ValueError:
                print('  此按键未对应ASCII值')
        elif event.type == pygame.KEYUP:
            print(f'弹起')
