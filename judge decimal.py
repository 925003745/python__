i = ["-0.3", "0", "2", "0.002", "-5", "china", "中国", "-like", "-中国"]
for i in i:
    if (i.split(".")[0]).isdigit() or i.isdigit() or (i.split('-')[-1]).split(".")[-1].isdigit():
        print(i + "是数字")
    else:
        print(i + "不是数字")
