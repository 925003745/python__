# -*- coding: utf-8 -*-                                                       
# @Time       :   2021/5/22 19:49
import requests

if __name__ == "__main__":
    url_1 = 'https://www.sogou.com/web'
    # UA伪装：
    headers_1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                      '90.0.4430.212 Safari/537.36 Edg/90.0.818.66'}
    # 处理url携带的参数：封装到字典中
    kw = input('输入您想搜索的内容：')
    param = {'query': kw}
    # 对指定url发起的请求对应的url时携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url_1, params=param, headers=headers_1)
    page_text = response.text
    filename = kw + '.html'
    with open(filename, 'w+', encoding='utf-8') as fp:
        fp.write(page_text)
    print('完成！')

# 反爬机制：UA检测
# UA:user-agent(请求载体的身份标识（浏览器）)
# UA检测：网站会检测请求载体的身份标识，若标识不是浏览器，访问请求可能会被拒绝
# UA:伪装：(将user-agent封装到字典中)
