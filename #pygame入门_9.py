# -*- coding: utf-8 -*-
# @Time       :   2021/6/10 20:46
import time
import pygame
import random

WIN_WIDTH = 1000
WIN_HEIGHT = 800
FPS = 144

pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Title')
window.fill((255, 255, 255))
pygame.display.flip()  # 绘制基本窗口

plane_up = pygame.image.load('images/plane.png')
plane_right = pygame.transform.rotozoom(plane_up, -90, 1)
plane_down = pygame.transform.rotozoom(plane_right, -90, 1)
plane_left = pygame.transform.rotozoom(plane_down, -90, 1)  # 飞机图像转为向下 向左 向右

bullet_up = pygame.image.load('./images/bullet1.png')
bullet_right = pygame.transform.rotozoom(bullet_up, -90, 1)
bullet_down = pygame.transform.rotozoom(bullet_right, -90, 1)
bullet_left = pygame.transform.rotozoom(bullet_down, -90, 1)  # 子弹图像转为向下 向左 向右

enemy_temp = pygame.image.load('./images/enemy_1.png')
enemy1 = pygame.transform.scale(enemy_temp, (60, 60))  # 敌机

size_x, size_y = plane_up.get_size()  # 获取图片尺寸
size_ex, size_ey = enemy1.get_size()
size_bx, size_by = bullet_up.get_size()

plane_x, plane_y = WIN_WIDTH / 2 - size_x / 2, WIN_HEIGHT / 2 - size_y / 2  # 飞机初始位置

window.blit(plane_up, (plane_x, plane_y))  # 将飞机添加到窗口中
pygame.display.update()

enemy_y = 0


def enemy():
    time.sleep(0.75)
    global enemy_y
    enemy = enemy1
    e_speed = random.randint(2, 4)
    enemy_x = random.randint(0, WIN_WIDTH - size_ex)
    enemy_y += e_speed
    window.blit(enemy, (enemy_x, enemy_y))
    pygame.display.update()


is_move = False  # 移动判断布尔变量
x_speed = 0
y_speed = 0
plane_temp = plane_up

while True:
    # FLY_BULLET_X = plane_x + size_x / 2 - size_bx / 2
    # FLY_BULLET_Y = plane_y - size_by
    # FLY_BULLET_Y -= 0.03
    # window.blit(bullet_up, (FLY_BULLET_X, FLY_BULLET_Y))
    # pygame.display.update()

    if is_move:
        time.sleep(1 / FPS)  # 其实这个和fps(frames per second)没有关系，可以控制飞机飞行速度，FPS越小越慢
        window.fill((255, 255, 255))
        plane_x += x_speed
        plane_y += y_speed

        if plane_x >= WIN_WIDTH - size_x:
            plane_x = WIN_WIDTH - size_x
        if plane_x <= 0:
            plane_x = 0
        if plane_y >= WIN_HEIGHT - size_y:
            plane_y = WIN_HEIGHT - size_y
        if plane_y <= 0:
            plane_y = 0  # 控制边界
        window.blit(plane_temp, (plane_x, plane_y))
        print(plane_x, plane_y)
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            _ = event.key
            if _ == 119 or _ == 1073741906:  # w
                is_move = True
                x_speed = 0
                y_speed = -2
                plane_temp = plane_up
            elif _ == 97 or _ == 1073741904:  # a
                is_move = True
                x_speed = -2
                y_speed = 0
                plane_temp = plane_left
            elif _ == 115 or _ == 1073741905:  # s
                is_move = True
                x_speed = 0
                y_speed = 2
                plane_temp = plane_down
            elif _ == 100 or _ == 1073741903:  # d
                is_move = True
                x_speed = 2
                y_speed = 0
                plane_temp = plane_right
            elif _ == 106:
                pass
        elif event.type == pygame.KEYUP:
            is_move = False
