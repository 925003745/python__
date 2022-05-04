# -*- coding: utf-8 -*-                                                       
# @Time       :   2021/6/10 20:00
import pygame

WIN_WIDTH = 400
WIN_HEIGHT = 600
FPS = 60

pygame.init()
abc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('123456')
abc.fill((255, 255, 255))
pygame.display.flip()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()
