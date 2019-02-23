#!/usr/bin/env python3
# -*- coding=utf-8 -*-
"""
#Author:Dang_h
#Created Time:2019年02月23日 星期六 22时28分37秒
#File Name:extest.py
"""
#Description:

num = input("Enter number:")
try:
    new_num = int(num)
    print("INT:{}".format(new_num))
except ValueError:
    print('ERROR:{}'.format(num))
