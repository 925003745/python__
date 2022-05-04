import time

adv = input("请输入一段广告语：")
adv = adv + " "
k = input('请输入您想让广告持续滚动的时间（单位：秒）:')
j = 0
while True:
    fx = input("请输入滚动的方向（L/R):")
    if fx.upper() in ['L', 'R']:
        break
    else:
        print("您输入的有误，请重新输入！")

while True:
    sd = input("请输入滚动的速度（越小越快）:")
    if (sd.split(".")[0]).isdigit() or sd.isdigit():
        break
    else:
        print("您输入的有误，请重新输入！")

while True:
    j += float(sd)
    if float(j) <= float(k):
        if fx == "R":
            adv = adv[-1] + adv[:-1]
        else:
            adv = adv[1:] + adv[0]
        print('\r' + adv, end='', flush=True)
        time.sleep(float(sd))
    else:
        break
