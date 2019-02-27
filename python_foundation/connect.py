#!/usr/bin/env python3
#-*- coding=utf-8 -*-
"""
#Author: Dang_h
#Creat Time:2019年02月27日 星期三 23时00分28秒
#File Name:connect.py
#Description:
"""

def connect(ipaddress, ports):
    print("IP:", ipaddress)
    print("Port:", ports)
    ipaddress = '10.120.12.1'
    ports.append(8000)

if __name__ == '__main__':
    ipaddress = '192.168.1.1'
    ports = [22,23,24]
    print('Before connect:')
    print('IP:', ipaddress)
    print('Port:', ports)
    print('-------------')
    print('In Connect')
    connect(ipaddress, ports)
    print('After connect:')
    print('IP:', ipaddress)
    print('Port:', ports)
