#!/usr/bin/env python3
#-*- coding=utf-8 -*-
"""
#Author: Dang_h
#Creat Time:2019年03月03日 星期日 17时12分20秒
#File Name:copyfile.py
#Description:读取shiyanlou.txt文件内容，并将其写入/home/shiyanlou/shiyanlou_copy.txt
中；文件代码中必须使用readline()方法；shiyanlou_copy.txt内容按格式输出
"""

import sys

with open('shiyanlou.txt') as f1:
    with open('shiyanlou_copy.txt', 'w') as f2:
        for i, value in enumerate(f1.readlines()):
            f2.write('{} {}'.format(i+1, value))

#def copy_file(src, dst):
#    with open(src) as f1:
#        with open(dst, 'w') as f2:
#            for n, w in f1:
#                f2.write('{} {}'.format(n+1, w))

#def copy_file(src, dst):
#    with open(src) as src_file:
#        with open(dst, 'w') as dst_file:
#            for line in src_file:
#                dst_file.write(line)
#
#def print_file(filename):
#    with open(filename, 'r') as f2:
#        for n, line in enumerate(f2):
#            print('{} {}'.format(n+1, line))
#
#if __name__ == '__main__':
#    if len(sys.argv) == 3:
#        copy_file(sys.argv[1], sys.argv[2])
#        print_file(sys.argv[2])
#    else:
#        print("Paramenter Error\n{}srcfile dstfile".format(sys.argv[0]))
#        sys.exit(-1)
#    sys.exit(0)
#
