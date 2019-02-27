#!/usr/bin/env python3
#-*- coding=utf-8 -*-
"""
#Author: Dang_h
#Creat Time:2019年02月27日 星期三 23时33分30秒
#File Name:test.py
#Description:
"""

def compute(base,value):
    print(base, value)
    base.append(value)
    print(base)

if __name__ == '__main__':
    testlist = [1,2,3,4]
    compute(testlist, 10)
    compute(testlist, 20)

