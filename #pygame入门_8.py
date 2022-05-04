# -*- coding: utf-8 -*-                                                       
# @Time       :   2021/6/10 19:36
import pygame

WIN_WIDTH = 400
WIN_HEIGHT = 600
FPS = 60

pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('显示图形')
window.fill((255, 255, 255))
pygame.display.flip()

bx1, by1, bw, bh = 30, 100, 100, 50
font = pygame.font.Font(r'D:\pycharm_community\project\ziti\SFZ_ZHT\abc.TTF', 30)
pygame.draw.rect(window, (255, 0, 0), (bx1, by1, bw, bh))

text1 = font.render('确定', True, (255, 255, 255))
tw1, th1 = text1.get_size()
tx1 = bx1 + bw / 2 - tw1 / 2
ty1 = by1 + bh / 2 - th1 / 2
window.blit(text1, (tx1, ty1))

bx2, by2 = 30, 200
pygame.draw.rect(window, (0, 255, 0), (bx2, by2, bw, bh))

text2 = font.render('取消', True, (255, 255, 255))
tw2, th2 = text2.get_size()
tx2 = bx2 + bw / 2 - tw2 / 2
ty2 = by2 + bh / 2 - th2 / 2
window.blit(text2, (tx1, ty2))
pygame.display.update()

while True:
    for event in pygame.event.get():  # pygame.event.get()为获取事件

        if event.type == pygame.QUIT:  # 检测到时间类型为pygame.QUIT时执行exit()
            # pygame.QUIT为模块已有type，判断即可
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if (bx1 <= mx <= bx1 + bw) and (by1 <= my <= by1 + bh):
                pygame.draw.rect(window, (200, 0, 0), (bx1, by1, bw, bh))
                window.blit(text1, (tx1, ty1))
                pygame.display.update()

            elif (bx2 <= mx <= bx2 + bw) and (by2 <= my <= by2 + bh):
                pygame.draw.rect(window, (0, 200, 0), (bx2, by2, bw, bh))
                window.blit(text2, (tx1, ty2))
                pygame.display.update()

        elif event.type == pygame.MOUSEBUTTONUP:

            mx, my = event.pos
            if (bx1 <= mx <= bx1 + bw) and (by1 <= my <= by1 + bh):
                pygame.draw.rect(window, (255, 0, 0), (bx1, by1, bw, bh))
                window.blit(text1, (tx1, ty1))
            elif (bx2 <= mx <= bx2 + bw) and (by2 <= my <= by2 + bh):
                pygame.draw.rect(window, (0, 255, 0), (bx2, by2, bw, bh))
                window.blit(text2, (tx2, ty2))
            pygame.display.update()
