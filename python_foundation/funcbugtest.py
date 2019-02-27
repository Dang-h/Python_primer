#!/usr/bin/env python3
#-*- coding=utf-8 -*-
"""
#Author: Dang_h
#Creat Time:2019年02月27日 星期三 22时19分26秒
#File Name:funcbugtest.py
#Description:
"""

result = 0
start = 1

def compute():
    global start, result
    while start <= end:
        result += start
        start += 1
    print(result)

end = 100

if __name__ == '__main__':
    compute()
