#!/usr/bin/env python3
# -*- coding=utf-8 -*-
"""
#Author:Dang_h
#Created Time:2019年02月23日 星期六 22时19分47秒
#File Name:fileexc.py
"""
#Description:


filename = '/etc/protocols'
f = open(filename)
try:
    f.write('shiyanlou')
except :
    print("File write error")
finally:
    print('finally')
    f.close()
