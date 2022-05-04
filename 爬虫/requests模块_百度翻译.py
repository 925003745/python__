# -*- coding: utf-8 -*-
# @Time       :   2021/5/22 20:16
import requests
import json


def baidu_translate():
    word = input('input a word:')
    # UA伪装：
    headers_1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                      '90.0.4430.212 Safari/537.36 Edg/90.0.818.66'}
    # -post请求(携带了参数)
    # -响应数据是一组json数据
    post_url = r'https://fanyi.baidu.com/sug'
    data_1 = {'kw': word}
    response = requests.post(url=post_url, data=data_1, headers=headers_1)
    # 获取响应数据 json返回的是一个obj(对象)[如果确认响应数据为json时才可用]
    dic_obj = response.json()
    # print(dic_obj)
    # 存储
    fp = open('../project/爬虫/百度翻译result.json', 'w+', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
    # print('完成！')


def handle():
    with open(r'../project/爬虫/百度翻译result.json', 'r+', encoding='utf-8') as f:
        i = json.load(f)
        data_1 = i['data']
        num = 1
        for k_1 in data_1:
            temp_1 = k_1['k']
            temp_2 = k_1['v']
            print(f'{num} --- ', end='')
            num += 1
            print(temp_1 + ' : ' + temp_2)


if __name__ == "__main__":
    baidu_translate()
    handle()
