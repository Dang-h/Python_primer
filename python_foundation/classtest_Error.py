#!/usr/bin/env python3
#-*- coding=utf-8 -*-
"""
#Author: Dang_h
#Creat Time:2019年02月28日 星期四 11时07分56秒
#File Name:classtest.py
#Description:包含一个UserData类，该类可以保存用户id和名字，并且可以使用print按照一定格式直接打印输出;实现一个新类NewUser，继承UserData类，并提供新接口，get_name(),set_name()
"""

class UserData:
    user_info = {}
    def __init__(self, ID, Name):
        self.user_info[ID] = Name
        for key, value in self.user_info.items():
            self.key = key      #self 表示实例化的引用
            self.value = value
    def __repr__(self):
        return 'ID:{} Name:{}'.format(self.key, self.value)

class NewUser(UserData):
    def get_name(self):
        return self.user_info[ID] = Name
    def set_name(self, value):
        


if __name__ == '__main__':
    user1 = UserData(101, 'Jack')
    user2 = UserData(102, 'Louplus')
    print(user1)
    print(user2)
