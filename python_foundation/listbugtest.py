#!/usr/bin/env python3
#-*- coding=utf-8 -*-
"""
#Author: Dang_h
#Creat Time:2019年02月27日 星期三 23时10分40秒
#File Name:listbugtest.py
#Description:
"""

def compute(base, value):
    base_add = base[:]
    base_add.append(value)
    print(sum(base_add))

if __name__ == '__main__':
    testlist = [10, 20, 30]
    compute(testlist, 15)
    compute(testlist, 25)
    compute(testlist, 35)

