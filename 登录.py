# -*- coding: utf-8 -*-                                                       
# @Time       :   2021/6/24 15:56
import tkinter as tk
from tkinter import Tk, Toplevel, messagebox


def main2():
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
        name = user_name_entry.get()
        pwd = user_pwd_entry.get()
        user_dict = read_data()
        if name != "" and pwd != "":
            if name in user_dict.keys():
                if pwd == user_dict[name]:
                    messagebox.showinfo(title="针不错", message="恭喜" + name + "登陆成功")

                else:
                    messagebox.showerror(title="FBI WARNING", message="密码错误")
            else:
                messagebox.showerror(title="FBI WARNING", message="账号不存在")
        else:
            messagebox.showerror(title="FBI WARNING", message="用户名不能为空")

    def pop_with():
        def get_info():
            dict_a = read_data()
            name = user_set_name.get()
            pwd = user_set_pwd.get()
            if name != "" and pwd != "":
                if name not in dict_a.keys():
                    with open("images/id_password.txt", "w+", encoding="utf-8") as f:
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
        top.title("注册")
        screen_w, screen_h = my_window.maxsize()
        str_abc = ("%dx%d+%d+%d" % (250, 200, (screen_w - w) / 2, (screen_h - h) / 2))
        top.geometry(str_abc)
        user_n1 = tk.Label(top, text="账号")
        user_n1.place(x=80, y=50)
        user_n2 = tk.Label(top, text="密码")
        user_n2.place(x=80, y=90)
        user_set_name = tk.StringVar()
        user_set_name.set("输入账号")
        user_name_emtry = tk.Entry(top, textvariable=user_set_name, width=10)
        user_name_emtry.place(x=130, y=50)
        user_set_pwd = tk.StringVar()
        user_set_pwd.set("输入密码")
        user_pwd_emtry = tk.Entry(top, textvariable=user_set_pwd, width=10)
        user_pwd_emtry.place(x=130, y=90)
        user_login_button = tk.Button(top, text="注册", command=get_info)
        user_login_button.place(x=110, y=120)

    my_window = Tk()
    my_window.title("登陆界面1")
    h = 300
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
    user_name_text.set("输入账号")
    user_name_entry = tk.Entry(my_window, textvariable=user_name_text, width=15)
    user_name_entry.place(x=160, y=90)
    # 密码输入框
    user_pwd_text = tk.StringVar()
    user_pwd_text.set("输入密码")
    user_pwd_entry = tk.Entry(my_window, textvariable=user_pwd_text, width=15)
    user_pwd_entry.place(x=160, y=130)
    # 按钮
    user_login_button = tk.Button(my_window, text="登录", command=user_login)
    user_login_button.place(x=80, y=180)
    user_reg_button = tk.Button(my_window, text="注册", command=pop_with)
    user_reg_button.place(x=180, y=180)

    read_data()
    my_window.mainloop()


main2()
