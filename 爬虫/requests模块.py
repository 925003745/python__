# -*- coding: utf-8 -*-                                                       
# @Time       :   2021/5/22 19:21

# requests:模拟浏览器发请求
# -指定url
# -发起请求
# -获取响应数据
# -持久化数据

import requests

if __name__ == "__main__":
    # 1.指定url
    url_1 = 'https://www.sogou.com/'
    # 2.发起请求
    response = requests.get(url=url_1)
    # 3.获取响应数据
    page_text = response.text  # 获取了网页源码数据（字符串形式）
    print(page_text)
    # 持久存储
    with open('../project/爬虫/sogou.html', 'w+', encoding='utf-8') as fp:
        fp.write(page_text)
    print('结束')
