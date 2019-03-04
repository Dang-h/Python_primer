#!/usr/bin/env python3
#-*- coding=utf-8 -*-
"""
#Author: Dang_h
#Creat Time:2019年03月02日 星期六 14时46分08秒
#File Name:classtest.py
#Description:使用符合property和setter来代替get_name和set_name；当设置对象名称超过3个字符，小于等于3个字符则不改变对象名称
"""

class UserData(object):
    def __init__(self, id, name):
        self.id = id
        self._name = name
    
class NewUser(UserData):
    @property           #property可以将一个方法变成一个属性使用；@property可以获得和修改对象的某一个属性；只有@property表示只读
    def name(self):
        return self._name

    @name.setter        #@setter表示可写
    def name(self, name):
        if len(name) > 3:
            self._name = name
        else:
            print('ERROR')

if __name__ == '__main__':
    user1 = NewUser(101, 'Jack')
    user1.name = 'Lou'
    user1.name = 'Jackie'
    user2 = NewUser(102, 'louplus')
    print(user1.name)
    print(user2.name)
