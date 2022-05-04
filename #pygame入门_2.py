# -*- coding: utf-8 -*-                                                       
# @Time       :   2021/6/10 17:30
import pygame

pygame.init()
window = pygame.display.set_mode((400, 600))
pygame.display.set_caption('显示图形')
window.fill((255, 255, 255))

# 图形部分
# 1.画直线
# line(画在哪， 线的颜色， 起点， 终点， 线宽=1)
pygame.draw.line(window, (255, 0, 0), (10, 20), (200, 20))
# lines(画在哪， 线的颜色，是否闭合，点列表，线宽)
list_points = [(10, 300), (100, 160), (180, 260), (300, 100)]
pygame.draw.lines(window, (0, 255, 0), True, list_points, 3)
# 画圆
# circle(画在哪， 线的颜色，圆心坐标，半径，线宽=0（0表示填充）)
pygame.draw.circle(window, (0, 0, 255), (200, 250), 100, 1)
# 画矩形
# rect(画在哪， 线的颜色，矩形范围，线宽=0)
pygame.draw.rect(window, (20, 10, 20), (15, 70, 50, 70), 1)
# 画椭圆
# ellipse(画在哪， 线的颜色，矩形范围，线宽=0)(矩形内切椭圆)
pygame.draw.ellipse(window, (250, 20, 200), (100, 70, 50, 70), 1)
# 画弧线.arc()
pygame.display.flip()
while True:
    for event in pygame.event.get():  # pygame.event.get()为获取事件
        if event.type == pygame.QUIT:  # 检测到时间类型为pygame.QUIT时执行exit()
            # pygame.QUIT为模块已有type，判断即可
            exit()
