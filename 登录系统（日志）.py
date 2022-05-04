def warp_1(func):
    def log():
        func()
        import time
        def ipconfig():
            import socket
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            return ip
        present_time = time.strftime(f'%Y年%m月%d日，%H点%M分%S秒,'
                                     f'{Results_the_login}. IPv4地址:{ipconfig()}\n\n')
        file_1 = open(r"D:\Capture Information file (python)\log_1.txt", "a")
        file_1.write(present_time)
        file_1.close()

    return log


Results_the_login = ''


@warp_1
def login():
    global Results_the_login
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "admin":
        if password == "888888":
            print("登录成功！")
            Results_the_login = '登陆成功'
        else:
            print("密码错误！")
            Results_the_login = '登录失败'
    else:
        print("用户名错误！")
        Results_the_login = '登录失败'


login()
