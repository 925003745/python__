# -*- coding: utf-8 -*-                                                       
# @Time       :   2021/5/22 20:55
import requests
import json


# 当发起请求后地址栏中的url没变，则说明此请求为阿贾克斯请求（XHR）
def douban():
    """运行结束后，打开douban.json，复制内容粘贴到https://www.json.cn/可查看"""
    if __name__ == "__main__":
        # UA伪装：
        headers_1 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                          '90.0.4430.212 Safari/537.36 Edg/90.0.818.66'}

        url_1 = 'https://movie.douban.com/j/chart/top_list'

        param_1 = {
            'type': '24',
            'interval_id': '100:90',
            'action': '',
            'start': '0',  # 从库中第几部电影开始取
            'limit': '20'  # 一次取多少部
        }
        response = requests.get(url=url_1, params=param_1, headers=headers_1)
        list_data = response.json()
        fp = open('../project/爬虫/douban.json', 'w+', encoding='utf-8')
        json.dump(list_data, fp=fp, ensure_ascii=False)
        print('完成！')


douban()
