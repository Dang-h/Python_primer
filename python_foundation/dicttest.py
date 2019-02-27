#!/usr/bin/env python
#-*- coding=utf-8 -*-
"""
#Author: Dang_h
#Creat Time:2019年02月27日 星期三 18时56分42秒
#File Name:dicttest.py
#Description:
"""
import sys

output_dict = {}

def handle_data(str_):
    key, value = str_.split(':')
    output_dict[key] = value
    return output_dict

def print_data(keys, values):
    print("ID:{} Name:{}".format(keys, values))

if __name__ == '__main__':

    for arg in sys.argv[1:]:
        handle_data(arg)

    for key in output_dict:
        print_data(key, output_dict[key])
