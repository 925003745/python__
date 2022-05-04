import time

print(time.strftime('今天是%Y年%m月%d日，现在时间是%H点%M分%S秒，今天是星期%w,是%y年的第%j天', time.localtime()))
