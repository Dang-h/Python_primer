#!/usr/bin/env python3
#-*- coding=utf-8 -*-
"""
#Author: Dang_h
#Creat Time:2019年03月03日 星期日 16时33分12秒
#File Name:copy.py
#Description:
"""

import sys

#定义复制文件的函数。该函数需要传入两个参数，分别是当前目录下的源文件和输出文件名
def copy_file(src, dst):
    with open(src, 'r') as src_file:    #打开源文件，读入
        with open(dst, 'w') as dst_file:    #打开目标文件，写入
            dst_file.write(src_file.read())

if __name__ == '__main__':
    if len(sys.argv) == 3:      #判断文件名是否合法，合法执行复制
        copy_file(sys.argv[1], sys.argv[2])
    else:
        print("Paramenter Error")
        print(sys.argv[0], "srcfile dstfile")
        sys.exit(-1)
    sys.exit(-1)
