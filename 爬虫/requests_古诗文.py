import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '90.0.4430.212 Safari/537.36 Edg/90.0.818.66'}
BASE_DOMIN = 'https://www.gushiwen.cn/default_1.aspx'


def parse_page(url):
    response = requests.get(url, headers=headers)
    text = response.text
    titles = re.findall(r'<b>(.*?)</b>', text, flags=re.DOTALL)
    authors = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>', text, flags=re.DOTALL)
    dynasty = re.findall(r'<p class="source">.*?<a.*?<a.*?>(.*?)</a>', text, flags=re.DOTALL)
    poems_ret = re.findall(r'<div class="contson".*?>(.*?)</div>', text, flags=re.DOTALL)
    poems = []
    for poem in poems_ret:
        temp = re.sub("<.*?>", "", poem)
        poems.append(temp.strip())
    results = []
    for value in zip(titles, dynasty, authors, poems):
        title, time, author, poem = value
        result = {
            "标题": title,
            "朝代": time,
            "作者": author,
            "原文": poem
        }

        results.append(result)
    for _ in results:
        __ = str(_["原文"])
        ___ = __.split('。')
        print(f'{_["标题"]}\n{_["朝代"]}  {_["作者"]}\n')
        for ____ in ___:
            _____ = ____ + '。'
            print(_____)
        print('\n\n')


def spider():
    url_base = 'https://www.gushiwen.cn/default_{}.aspx'
    for i in range(1, 2):
        print(f'正在爬取第{i}页：')
        url = url_base.format(i)
        print(" " * 20 + "优美古诗文" + " " * 20)
        print('=' * 55)
        parse_page(url)


if __name__ == '__main__':
    spider()
