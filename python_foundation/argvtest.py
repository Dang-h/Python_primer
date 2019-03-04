#!/usr/bin/env python3
#-*- coding=utf-8 -*-
"""
#Author: Dang_h
#Creat Time:2019年03月03日 星期日 16时47分13秒
#File Name:argvtest.py
#Description:读取程序名称和终端输入参数，通过函数enumerate(iterable_objct)顺序输出终端输入参数
"""

import sys

print("Program: ", sys.argv[0])     #读取程序名称
print('Parameters: ')           #顺序输出终端参数
for i, x in enumerate(sys.argv):
    if (i == 0):
        continue
    print(i, x)

