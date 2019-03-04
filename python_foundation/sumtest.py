#!/usr/bin/env python3
#-*- coding=utf-8 -*-
"""
#Author: Dang_h
#Creat Time:2019年03月03日 星期日 14时03分46秒
#File Name:sumtest.py
#Description:使用input()获取用户输入的三个整数；对这三个数进香相加求和并打印输出；打印时使用format()
"""

a = input('Please enter the first number: ')
b = input('Please enter the second number: ')
c = input('Please enter the third number: ')

sum = int(a) + int(b) + int(c)

print('a is {}, b is {}, c is {}, a+b+c = {}'.format(a, b, c, sum))
