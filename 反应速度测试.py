import time
import random

for abc in range(5):
    def decorator(func):
        def inner():
            global end_time, k
            t1 = random.randint(2, 9)  # 随机时间打印红色字体（开始测试）
            time.sleep(t1)
            i = time.time()
            func()
            k1 = end_time - i
            k = (k1 * 1000) - Correction_parameters  # 将秒转换为毫秒
            k = round(k, 2)  # 保留两位小数
            print(f'你的此次反应速度为：{k}毫秒')
            if 500 > k > 50:  # 异常数据排除
                statistics()
            if abc == 4:
                average()

        return inner


    @decorator
    def test():
        global end_time
        user = input('\033[1;31m 按下回车！！！ \033[0m')
        if user == '':
            end_time = time.time()


    def statistics():
        global k
        outfile = open(r"D:\Capture Information file (python)\fysdcs.txt", "a")
        c_file = str(k) + ','
        outfile.write(c_file)
        outfile.close()


    def clear(func):
        def inner():
            func()
            file = open(r"D:\Capture Information file (python)\fysdcs.txt", "w+")
            file.truncate()  # 清空txt文件
            file.close()

        return inner


    @clear
    def average():
        with open(r'D:\Capture Information file (python)\fysdcs.txt', 'r') as f:
            date1 = f.read()
        p = date1.split(',')
        p.pop()
        pp = len(p)
        ppp = 0
        sum1 = 0
        while ppp < pp:
            pppp = float(p[ppp])
            sum1 += pppp
            ppp += 1
        average1 = sum1 / pp
        average2 = round(average1, 2)
        print(f'你的平均反应速度为：\033[4;32m{average2}\033[0m'
              f'\n此测试不保证准确性，精准测试建议访问 '
              f'https://humanbenchmark.com/tests/reactiontime')


    k = 0
    end_time = 0
    Correction_parameters = 340
    if abc == 0:
        print('当你看见红色字体时，请以最快速度按下回车\n（请先将光标置于此文本的下一行）[共有5次]')

    test()
