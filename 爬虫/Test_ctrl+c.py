# -*- coding: utf-8 -*-                                                       
# @Time       :   2021/10/22 19:22
import requests
import json
import time

url_1 = "https://www.zaixian100f.com/exam/test_paper/item/type/1/term_id/769.html"

headers_1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                      '90.0.4430.212 Safari/537.36 Edg/90.0.818.66'}
response = requests.post(url=url_1, headers=headers_1)

page_text = response.text

print(page_text)