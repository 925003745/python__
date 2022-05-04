# -*- coding: utf-8 -*-
# @Time       :   2021/6/16 18:29
import time
import pygame  # 导入’pygame‘模块
import random  # 导入’random‘模块
import sqlite3
import tkinter as tk
from tkinter import Tk, Toplevel, messagebox
import pyautogui as pag


ALL_SPEED_var = 5
WIN_WIDTH = 1000  # 窗口宽度
WIN_HEIGHT = 800  # 窗口高度
PLANE_FLAG_UP = 1  # 飞机状态判断变量_UP表示向上
PLANE_FLAG_DOWN = -1  # 飞机状态判断变量_DOWN表示向下
PLANE_FLAG_LEFT = -1  # 飞机状态判断变量_LEFT表示向左
PLANE_FLAG_RIGHT = -1  # 飞机状态判断变量_RIGHT表示向右
TIME = 0
boolean = False
boolean1 = False
name = ''
SCORE = 0
score = 0
DIE = 100
__ = 0


def sqlite_out():
    global score, a

    conn = sqlite3.connect('./SQL/__score.db')
    cursor = conn.cursor()

    cursor.execute('select * from user2')

    values = cursor.fetchall()

    a = sorted(values, key=lambda x: int(x[1]), reverse=True)

    cursor.close()
    conn.close()


def main2():
    global boolean

    def read_data():
        with open("images/id_password.txt", "r", encoding="utf-8") as f:
            rows = f.readlines()
            user_info_dict = {}
            for row in rows:
                list_a = row.strip().split(":")
                user_info_dict[list_a[0]] = list_a[1]
        f.close()
        return user_info_dict

    def user_login():
        global boolean, name
        name = user_name_entry.get()
        pwd = user_pwd_entry.get()
        user_dict = read_data()
        if name != "" and pwd != "":
            if name in user_dict.keys():
                if pwd == user_dict[name]:
                    messagebox.showinfo(title="Prompt", message="恭喜" + name + "登陆成功\n关闭登陆器自动开始游戏")
                    pag.click(1416, 489)
                    boolean = True
                else:
                    messagebox.showerror(title="Warning", message="密码错误")
            else:
                messagebox.showerror(title="Warning", message="账号不存在")
        else:
            messagebox.showerror(title="Warning", message="用户名或密码不能为空")

    def pop_with():
        global name

        def get_info():
            dict_a = read_data()
            name = user_set_name.get()
            pwd = user_set_pwd.get()
            if name != "" and pwd != "":
                if name not in dict_a.keys():
                    with open("images/id_password.txt", "a", encoding="utf-8") as f:
                        str_abc = name + ":" + pwd + "\n"
                        f.write(str_abc)
                    f.close()
                    messagebox.showinfo(title="注册成功", message="恭喜" + name + "的用户注册成功")
                    top.destroy()
                else:
                    messagebox.showerror(title="警告", message="账号重复")
            else:
                messagebox.showerror(title="警告", message="账号 密码不能为空")

        top = Toplevel()
        top.title("注册器")
        screen_w, screen_h = my_window.maxsize()
        str_abc = ("%dx%d+%d+%d" % (250, 200, (screen_w - w) / 2, (screen_h - h) / 2))
        top.geometry(str_abc)
        user_n1 = tk.Label(top, text="账号")
        user_n1.place(x=80, y=50)
        user_n2 = tk.Label(top, text="密码")
        user_n2.place(x=80, y=90)
        user_set_name = tk.StringVar()
        user_set_name.set("")
        user_name_emtry = tk.Entry(top, textvariable=user_set_name, width=10)
        user_name_emtry.place(x=130, y=50)
        user_set_pwd = tk.StringVar()
        user_set_pwd.set("")
        user_pwd_emtry = tk.Entry(top, textvariable=user_set_pwd, width=10)
        user_pwd_emtry.place(x=130, y=90)
        user_login_button = tk.Button(top, text="    注册    ", command=get_info)
        user_login_button.place(x=110, y=120)

    my_window = Tk()
    my_window.title("登录器")
    h = 500
    w = 300
    screen_w, screen_h = my_window.maxsize()
    str_abc = ("%dx%d+%d+%d" % (h, w, (screen_w - w) / 2, (screen_h - h) / 2))
    my_window.geometry(str_abc)
    my_window.resizable(width=False, height=False)

    user_la = tk.Label(my_window, text="账号")
    user_la.place(x=80, y=90)

    user_la = tk.Label(my_window, text="密码")
    user_la.place(x=80, y=130)

    # 账号输入框
    user_name_text = tk.StringVar()
    user_name_text.set("")
    user_name_entry = tk.Entry(my_window, textvariable=user_name_text, width=20)
    user_name_entry.place(x=160, y=90)
    # 密码输入框
    user_pwd_text = tk.StringVar()
    user_pwd_text.set("")
    user_pwd_entry = tk.Entry(my_window, textvariable=user_pwd_text, width=20)
    user_pwd_entry.place(x=160, y=130)
    # 按钮
    user_login_button = tk.Button(my_window, text="    登录    ", command=user_login)
    user_login_button.place(x=120, y=180)
    user_reg_button = tk.Button(my_window, text="    注册    ", command=pop_with)
    user_reg_button.place(x=230, y=180)

    read_data()
    if not boolean:
        my_window.mainloop()


def password():
    while True:
        if boolean:
            break
        else:
            exit()


def password2():
    while True:
        if boolean1:
            break
        else:
            exit()


def start():
    window_ = tk.Tk()
    window_.title('飞机大战开始界面')
    window_.geometry('380x620+475+134')

    def button1():
        global boolean1
        boolean1 = True
        messagebox.showinfo(title='Prompt', message='关闭开始界面窗口以开始游戏')
        pag.click(855, 137)

    def button2():
        sqlite_out()
        window1 = tk.Tk()
        window1.title('排行榜')
        window1.geometry('300x550')
        label2 = tk.Label(window1, bg='white', width=300, height=1, text='======排行榜======')
        label2.pack()
        label3 = tk.Label(window1, bg='white', width=300, height=1, text='    用户        分数    ')
        label3.pack()
        for info in a:
            label1 = tk.Label(window1, bg='white', width=300, height=1, text=info)
            label1.pack()

        window1.mainloop()

    def button3():
        window2 = Tk()
        window2.title('制作人员')
        window2.geometry('450x240')
        label3 = tk.Label(window2, bg='white',
                          width=450, height=250, text=f'制作人员:\n\n\n'
                                                      f'成浩洋  陈影  李博  石沅松  杨志  张良基\n\n\n'
                                                      f'【排名不分先后，只与字母顺序有关】')
        label3.pack()
        window2.mainloop()

    b1 = tk.Button(window_, text='开始游戏', bg='yellow', width=15, height=1, command=button1)
    b1.place(relx=0.5, rely=0.2, anchor="center")

    b2 = tk.Button(window_, text='排行榜', bg='green', width=15, height=1, command=button2)
    b2.place(relx=0.5, rely=0.4, anchor="center")

    b3 = tk.Button(window_, text='制作团队', bg='red', width=15, height=1, command=button3)
    b3.place(relx=0.5, rely=0.6, anchor="center")

    window_.mainloop()


main2()
password()
start()
password2()


def music():
    pygame.mixer.init()
    pygame.mixer.music.load('./images/mc.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)


def sqlite_in():
    global SCORE, name
    conn = sqlite3.connect('./SQL/__score.db')
    cursor = conn.cursor()

    try:
        cursor.execute('create table user2 (id varchar (20), name varchar(20))')
    except sqlite3.OperationalError:
        pass
    cursor.execute(f'insert into user2 (id, name) values (\'{name}\', \'{SCORE}\')')

    conn.commit()

    cursor.close()
    conn.close()


pygame.init()  # pygame初始化
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # 构造基本窗口
pygame.display.set_caption('飞机大战')  # 窗口标题
window.fill((255, 255, 255))  # 将整个窗口绘制为某个颜色(255，255，255)表示白色
pygame.display.flip()  # 第一次刷新

font = pygame.font.Font(r'./images/bg.ttc', 20)  # 创建字体对象，字号为20
text = font.render('按space发射子弹，wasd以及上下左右方向键均可移动',
                   True, (0, 0, 0), (255, 255, 255))  # 编辑字体内容 平滑度 文字颜色 背景颜色

background1 = pygame.image.load('./images/pb.png')
background = pygame.transform.scale(background1, (1000, 800))
plane_up = pygame.image.load('./images/plane.png')  # 读取飞机图像
plane_right = pygame.transform.rotozoom(plane_up, -90, 1)  # 顺时针转动90度
plane_down = pygame.transform.rotozoom(plane_right, -90, 1)  # 顺时针转动90度
plane_left = pygame.transform.rotozoom(plane_down, -90, 1)  # 顺时针转动90度
# 飞机图像转为向下 向左 向右

enemy_temp = pygame.image.load('./images/enemy_1.png')  # 读取敌机图像
enemy1 = pygame.transform.rotozoom(enemy_temp, 180, 0.15)
enemy2 = pygame.transform.rotozoom(enemy_temp, -90, 0.15)
enemy3 = pygame.transform.rotozoom(enemy_temp, 90, 0.15)

size_x, size_y = plane_up.get_size()  # 获取飞机图片尺寸
size_ex, size_ey = enemy1.get_size()  # 获取敌机图片尺寸
size_bx, size_by = 10, 17  # 子弹尺寸，子弹的load在class中，所以这里我人工读取了子弹尺寸

plane_x, plane_y = WIN_WIDTH / 2 - size_x / 2, WIN_HEIGHT / 2 - size_y / 2  # 飞机初始位置

window.blit(plane_up, (plane_x, plane_y))  # 将飞机添加到窗口中
pygame.display.update()  # 刷新


class Bullet:  # 创建子弹类
    def __init__(self):
        self.bullet_temp = pygame.image.load('./images/bullet1.png')  # 读取子弹图像
        self.bullet_up = pygame.transform.rotozoom(self.bullet_temp, 0, 1)
        self.bullet_right = pygame.transform.rotozoom(self.bullet_up, -90, 1)  # 顺时针选择90度
        self.bullet_down = pygame.transform.rotozoom(self.bullet_right, -90, 1)  # 顺时针选择90度
        self.bullet_left = pygame.transform.rotozoom(self.bullet_down, -90, 1)  # 顺时针选择90度
        self.bullet_x = plane_x + size_x / 2  # 子弹初始位置x坐标
        self.bullet_y = plane_y + size_y / 2  # 子弹初始位置y坐标
        self.SpeedBullet_X = 0  # 子弹x轴飞行速度
        self.SpeedBullet_Y = 0  # 子弹y轴飞行速度
        self.Old_or_New = True

    def impact(self):  # 子弹碰撞检测方法
        global SCORE
        global is_over, is_over_r, is_over_l  # 声明子弹销毁全局布尔变量
        if enemy_x <= self.bullet_x + size_bx / 2 <= enemy_x + size_ex and \
                enemy_y <= self.bullet_y <= enemy_y + size_ey:  # 判断子弹与敌机是否发生碰撞
            is_over = False
            SCORE += 100
            bullets.remove(self)  # if检测到碰撞就用remove()方法删除该子弹对象
        if enemy_x_r <= self.bullet_x + size_bx / 2 <= enemy_x_r + size_ex and \
                enemy_y_r <= self.bullet_y <= enemy_y_r + size_ey:  # 判断子弹与敌机是否发生碰撞
            is_over_r = False
            SCORE += 100
            bullets.remove(self)  # if检测到碰撞就用remove()方法删除该子弹对象
        if enemy_x_l <= self.bullet_x + size_bx / 2 <= enemy_x_l + size_ex and \
                enemy_y_l <= self.bullet_y <= enemy_y_l + size_ey:  # 判断子弹与敌机是否发生碰撞
            is_over_l = False
            SCORE += 100
            bullets.remove(self)  # if检测到碰撞就用remove()方法删除该子弹对象


bullets = []  # 子弹列表，内部存储的是发射子弹时创建的子弹对象


def bullet_show():  # 子弹飞行函数

    global PLANE_FLAG_LEFT, PLANE_FLAG_RIGHT, PLANE_FLAG_DOWN, PLANE_FLAG_UP  # 声明飞机状态判断变量

    for _ in bullets:  # 从子弹对象列表中遍历子弹对象
        if _.Old_or_New:
            if PLANE_FLAG_UP == 1:  # 判断飞机当前状态（上）
                _.SpeedBullet_Y = -ALL_SPEED_var * 1.5  # 将子弹的Y方向速度赋为-ALL_SPEED_var * 1.5（y坐标减即为向上走）
                _.SpeedBullet_X = 0  # X坐标保持为0即为在x方向上保持不动
                _.bullet_temp = _.bullet_up  # 将子弹图像调换为向上的子弹图像  【下面的三个if语句同理】

            if PLANE_FLAG_DOWN == 1:  # 判断飞机当前状态（下）
                _.SpeedBullet_Y = ALL_SPEED_var * 1.5
                _.SpeedBullet_X = 0
                _.bullet_temp = _.bullet_down

            if PLANE_FLAG_RIGHT == 1:  # 判断飞机当前状态（右）
                _.SpeedBullet_X = ALL_SPEED_var * 1.5
                _.SpeedBullet_Y = 0
                _.bullet_temp = _.bullet_right

            if PLANE_FLAG_LEFT == 1:  # 判断飞机当前状态（左）
                _.SpeedBullet_X = -ALL_SPEED_var * 1.5
                _.SpeedBullet_Y = 0
                _.bullet_temp = _.bullet_left

            _.Old_or_New = False
        _.bullet_x += _.SpeedBullet_X  # 更改子弹x坐标【子弹移动】
        _.bullet_y += _.SpeedBullet_Y  # 更改子弹y坐标【子弹移动】
        window.blit(_.bullet_temp, (_.bullet_x, _.bullet_y))  # 绘制子弹
        _.impact()  # 碰撞检测
        if _.bullet_y <= 0 or _.bullet_x <= 0 or \
                _.bullet_x >= WIN_WIDTH or _.bullet_y >= WIN_HEIGHT:  # 判断子弹是否飞出了边界
            bullets.remove(_)  # 如果飞出了边界就删除该对象


enemy_y = 0  # 敌机y坐标
enemy_y_r = random.randint(0, WIN_HEIGHT - size_ey)
enemy_y_l = random.randint(0, WIN_HEIGHT - size_ey)

e_speed = random.uniform(ALL_SPEED_var * 0.1, ALL_SPEED_var * 0.4)  # 随机生成一个0.1到0.4之间的小数作为敌机速度
e_speed_r = random.uniform(ALL_SPEED_var * 0.1, ALL_SPEED_var * 0.4)
e_speed_l = random.uniform(ALL_SPEED_var * 0.1, ALL_SPEED_var * 0.4)

enemy_x_l = WIN_WIDTH
enemy_x_r = 0
enemy_x = random.randint(0, WIN_WIDTH - size_ex)  # 随机生成一个敌机出生的x坐标

is_over = True  # 子弹销毁布尔变量
is_over_r = True
is_over_l = True


def enemy_show():  # 敌机飞行函数
    global is_over, DIE
    global e_speed, enemy_x
    global enemy_y
    if enemy_y > WIN_HEIGHT:
        is_over = False  # 出界判断
        DIE -= 1
    __enemy = enemy1  # 将敌机图片对象重新赋给__enemy，虽然没什么用，但我当时就是这么写了
    enemy_y += e_speed  # 敌机y坐标改变【敌机移动】
    window.blit(__enemy, (enemy_x, enemy_y))  # 绘制敌机


def enemy_show_LEFT():  # 敌机飞行函数a
    global is_over_l, e_speed_l, DIE
    global e_speed, enemy_x_l
    global enemy_y_l
    if enemy_x_l < 0:
        is_over_l = False  # 出界判断
        DIE -= 1
    __enemy = enemy3  # 将敌机图片对象重新赋给__enemy，虽然没什么用，但我当时就是这么写了
    enemy_x_l -= e_speed_l  # 敌机y坐标改变【敌机移动】
    window.blit(__enemy, (enemy_x_l, enemy_y_l))  # 绘制敌机


def enemy_show_RIGHT():  # 敌机飞行函数
    global is_over_r, e_speed_r, DIE
    global e_speed, enemy_x_r
    global enemy_y_r
    if enemy_x_r > WIN_WIDTH:
        is_over_r = False  # 出界判断
        DIE -= 1
    __enemy = enemy2  # 将敌机图片对象重新赋给__enemy，虽然没什么用，但我当时就是这么写了
    enemy_x_r += e_speed_r  # 敌机y坐标改变【敌机移动】
    window.blit(__enemy, (enemy_x_r, enemy_y_r))  # 绘制敌机


def over():  # 敌机与飞机碰撞检测函数
    """该函数使用取了敌机四个角的坐标判断是否与飞机发生了相遇，
    在csdn上曾看到过好像有专门用于碰撞检测的方法好像是叫rect()还是什么，当时懒得花时间搞懂那个了，所以就自己写了该函数用于检测碰撞"""
    global is_over, is_over_r, is_over_l, DIE
    if plane_x <= enemy_x <= plane_x + size_x and plane_y <= enemy_y <= plane_y + size_y:  # (0,0)
        is_over = False
        DIE -= 10
    if plane_x <= enemy_x + size_ex <= plane_x + size_x and plane_y <= enemy_y <= plane_y + size_y:  # (1,0)
        is_over = False
        DIE -= 10
    if plane_x <= enemy_x <= plane_x + size_x and plane_y <= enemy_y + size_ey <= plane_y + size_y:  # (0,-1)
        is_over = False
        DIE -= 10
    if plane_x <= enemy_x + size_ex <= plane_x + size_x and plane_y <= enemy_y + size_ey <= plane_y + size_y:  # (1,-1)
        is_over = False  # 碰撞检测
        DIE -= 10

    if plane_x <= enemy_x_r <= plane_x + size_x and plane_y <= enemy_y_r <= plane_y + size_y:  # (0,0)
        is_over_r = False
        DIE -= 10
    if plane_x <= enemy_x_r + size_ex <= plane_x + size_x and plane_y <= enemy_y_r <= plane_y + size_y:  # (1,0)
        is_over_r = False
        DIE -= 10
    if plane_x <= enemy_x_r <= plane_x + size_x and plane_y <= enemy_y_r + size_ey <= plane_y + size_y:  # (0,-1)
        is_over_r = False
        DIE -= 10
    if plane_x <= enemy_x_r + size_ex <= plane_x + size_x and plane_y <= enemy_y_r + size_ey <= plane_y + size_y:
        # (1,-1)
        is_over_r = False
        DIE -= 10

    if plane_x <= enemy_x_l <= plane_x + size_x and plane_y <= enemy_y_l <= plane_y + size_y:  # (0,0)
        is_over_l = False
        DIE -= 10
    if plane_x <= enemy_x_l + size_ex <= plane_x + size_x and plane_y <= enemy_y_l <= plane_y + size_y:  # (1,0)
        is_over_l = False
        DIE -= 10
    if plane_x <= enemy_x_l <= plane_x + size_x and plane_y <= enemy_y_l + size_ey <= plane_y + size_y:  # (0,-1)
        is_over_l = False
        DIE -= 10
    if plane_x <= enemy_x_l + size_ex <= plane_x + size_x and plane_y <= enemy_y_l + size_ey <= plane_y + size_y:
        # (1,-1)
        is_over_l = False
        DIE -= 10


def move_me():  # 飞机飞行函数
    global plane_x, plane_y, x_speed, y_speed
    # time.sleep(1 / FPS)  # 其实这个和fps(frames per second)没有关系，可以控制飞机飞行速度，FPS越小越慢
    plane_x += x_speed  # 飞机x坐标更改【飞机移动】
    plane_y += y_speed  # 飞机y坐标更改【飞机移动】

    if plane_x >= WIN_WIDTH - size_x:  # 判断飞机是否飞出窗口右边界[下面三个if同理]
        plane_x = WIN_WIDTH - size_x
    if plane_x <= 0:  # 左
        plane_x = 0
    if plane_y >= WIN_HEIGHT - size_y:  # 下
        plane_y = WIN_HEIGHT - size_y
    if plane_y <= 50:  # 上
        plane_y = 50


x_speed = 0  # 飞机x方向速度
y_speed = 0  # 飞机y方向速度
plane_temp = plane_up  # 飞机图像初始为向上
music()

while True:  # 游戏主体循环
    window.blit(background, (0, 0))
    pygame.draw.line(window, (255, 0, 0), (0, 50), (WIN_WIDTH, 50))  # 在界面上部50处绘制一条红色的线
    TIME = pygame.time.get_ticks()
    __text = font.render(f'时间：{int(TIME / 1000)}s 分数：{SCORE} 生命值：{DIE}', True, (0, 0, 0), (117, 187, 232))
    tx, ty = __text.get_size()
    window.blit(__text, (WIN_WIDTH - tx - 3, 3))

    press_down = pygame.key.get_pressed()  # 按下检测
    if press_down[pygame.K_w] or press_down[pygame.K_UP]:  # 判断是否按下了‘w’或‘上’键
        x_speed = 0  # 飞机x方向移动速度为0
        y_speed = -ALL_SPEED_var * 0.75  # 飞机y方向移动速度为-ALL_SPEED_var * 0.75，即为向上移动
        plane_temp = plane_up  # 飞机图像改为朝上的图像
        PLANE_FLAG_UP, PLANE_FLAG_DOWN, PLANE_FLAG_RIGHT, PLANE_FLAG_LEFT = 1, -1, -1, -1  # 更改飞机状态判断变量
        # 下面三个elif同理
    elif press_down[pygame.K_a] or press_down[pygame.K_LEFT]:  # 判断是否按下了‘a’或‘左’键
        x_speed = -ALL_SPEED_var * 0.75
        y_speed = 0
        plane_temp = plane_left
        PLANE_FLAG_UP, PLANE_FLAG_DOWN, PLANE_FLAG_RIGHT, PLANE_FLAG_LEFT = -1, -1, -1, 1
    elif press_down[pygame.K_s] or press_down[pygame.K_DOWN]:  # 判断是否按下了‘s’或‘下’键
        x_speed = 0
        y_speed = ALL_SPEED_var * 0.75
        plane_temp = plane_down
        PLANE_FLAG_UP, PLANE_FLAG_DOWN, PLANE_FLAG_RIGHT, PLANE_FLAG_LEFT = -1, 1, -1, -1
    elif press_down[pygame.K_d] or press_down[pygame.K_RIGHT]:  # 判断是否按下了‘d’或‘右’键
        x_speed = ALL_SPEED_var * 0.75
        y_speed = 0
        plane_temp = plane_right
        PLANE_FLAG_UP, PLANE_FLAG_DOWN, PLANE_FLAG_RIGHT, PLANE_FLAG_LEFT = -1, -1, 1, -1

    for event in pygame.event.get():  # 事件检测循环

        if event.type == pygame.QUIT:  # 退出检测
            exit()
        elif event.type == pygame.KEYDOWN:  # 按下检测
            if event.key == pygame.K_SPACE:  # 检测是否按下了空格键
                bullets.append(Bullet())  # 发射子弹(创建一个子弹对象添加到子弹列表中)
            if event.key == pygame.K_j:  # 当时想实现按j一直发射子弹，但是因为懒，所以pass了
                pass
        elif event.type == pygame.KEYUP:  # 按键弹起检测
            x_speed, y_speed = 0, 0  # 检测到按键弹起就修改速度值为0，使飞机停止不动

    move_me()  # 飞机移动
    bullet_show()  # 子弹移动
    over()  # 敌机被摧毁

    if is_over:
        enemy_show()  # 敌机移动
    if not is_over:
        is_over = True
        enemy_y = 0  # 重新赋敌机y坐标为0，使其回到起点
        enemy_x = random.randint(0, WIN_WIDTH - size_ex)  # 重新给敌机一个出现的位置
        e_speed = random.uniform(ALL_SPEED_var * 0.1, ALL_SPEED_var * 0.4)  # 重新给敌机一个速度

    if is_over_r:
        enemy_show_RIGHT()
    if not is_over_r:
        is_over_r = True
        enemy_x_r = 0
        enemy_y_r = random.randint(0, WIN_HEIGHT - size_ey)
        e_speed_r = random.uniform(ALL_SPEED_var * 0.1, ALL_SPEED_var * 0.4)

    if is_over_l:
        enemy_show_LEFT()
    if not is_over_l:
        is_over_l = True
        enemy_x_l = WIN_WIDTH
        enemy_y_l = random.randint(0, WIN_HEIGHT - size_ey)
        e_speed_l = random.uniform(ALL_SPEED_var * 0.1, ALL_SPEED_var * 0.4)
    window.blit(plane_temp, (plane_x, plane_y))  # 绘制飞机
    pygame.display.update()  # 刷新
    if DIE <= 0:
        screen = tk.Tk()
        screen.title('Prompt')
        screen.geometry('400x150+900+650')
        i1 = tk.Label(screen, bg='white', font=('黑体', 14), width=42, height=10,
                      text=f'游戏结束!\n您获得的分数为：{SCORE}\n\n[关掉此窗口自动退出]\n')
        i1.pack()
        sqlite_in()
        screen.mainloop()
        time.sleep(0.001)
        exit()
