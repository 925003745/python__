# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 19:29:26 2021

@author: 92500
"""
import time

def progress_bar():
    print('loading',end=(''))
    for j in range(4):
        for i in range(2):
            print('/', end='')
            time.sleep(0.28)
            print('\b', end='')
            print('-', end='')
            time.sleep(0.28)
            print('\b', end='')
            print('\\', end='')
            time.sleep(0.28)
            print('\b', end='')
            print('*', end='')
            print(' ', end='')

progress_bar()