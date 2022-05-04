# -*- coding: utf-8 -*-
# @Time       :   2021/5/19 17:58
import pygame

# 初始化
pygame.init()
# 创建窗口
window = pygame.display.set_mode((500, 800))
# 设置标题
pygame.display.set_caption("lb的第一个游戏")

# 设置背景颜色
window.fill((0, 0, 0))

# 游戏开始页面静态图一般写在这里===========================
# 加载图片
image_1 = pygame.image.load(r'D:\pycharm_community\project\飞机大战\images\background.png')
# 渲染图片   blit(渲染对象，位置信息（坐标）)方法即为渲染图片
# 左上角为坐标原点（0，0）
# ====================================window.blit(image_1, (0, 0))
# 需要刷新才会显示图片
# pygame.display.flip()  # 第一次刷新使用flip()方法


# pygame.display.update()  # 第一次以后的刷新使用update()方法，第一次也可以使用
# 操作图片
# 获取图片大小 便于设置窗口大小
w, h = image_1.get_size()
print(w, h)
window.blit(image_1, (500-w, 800-h))# 将图片放在右下角

# 旋转和缩放图片
# 缩放：scale(缩放对象，目标大小) （可能产生形变）
new_image = pygame.transform.scale(image_1, (100, 100))
window.blit(new_image, (400, 700))
# rotozoom（缩放/旋转对象，选择角度，缩放比例）可选择可缩放，缩放不会形变
new_image_1 = pygame.transform.rotozoom(image_1, 180, 0.5)
window.blit(new_image_1, (0, 500))
# ======显示文字========
# 创建字体对象
font = pygame.font.SysFont("arial", 16)  # 系统字体
# 下面这个为可自己设置的字体，该字体暂时有问题，不可用
# font = pygame.font.Font(r'D:\pycharm_community\project\ziti\SFZ_ZHT\书法家中黑体.TTF', 30)
# Font(字体文件路径，字号大小)
# 创建文字对象
# render(文字内容，（文字是否平滑）[一般写True就行],文字颜色，背景颜色(背景颜色可以不写，有默认值))
text_1 = font.render("hello pygame!", True, (255, 0, 0), (255, 255, 0))
window.blit(text_1, (1, 1))
# 文字也可操作，方法与上面的操作图片一模一样


pygame.display.update()
# 让窗口保存运行 game loop
while True:
    # 游戏帧刷新写在这里==================================

    # 事件检测
    for event in pygame.event.get():  # pygame.event.get()为获取事件
        if event.type == pygame.QUIT:  # 检测到时间类型为pygame.QUIT时执行exit()
            # pygame.QUIT为模块已有type，判断即可
            exit()
