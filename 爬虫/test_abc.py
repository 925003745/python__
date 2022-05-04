# -*- coding: utf-8 -*-                                                       
# @Time       :   2021/5/31 19:40
import requests
while True:
    # 英文翻译器
    url = r"https://fanyi.baidu.com/sug"
    # 获得用户要查询的单词
    word = input("请输入一个单词：")
    if word=="退出":
        break
    # 将单词封装到请求流中，当成数据发送给服务器
    data = {"kw": word}
    response = requests.post(url=url, data=data)
    result = response.json()
    jieshi = result["data"]
    no = 1
    for i in jieshi:
        print("第%d个解释：%s" % (no, i["v"]))
        no += 1