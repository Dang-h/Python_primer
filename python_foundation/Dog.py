#!/usr/bin/env python3
#-*- coding=utf-8 -*-
"""
#Author: Dang_h
#Creat Time:2019年02月28日 星期四 10时42分16秒
#File Name:Dog.py
#Description:
"""

class Dog(object):
    def __init__(self, name):    #__init__方法的第一个参数self表示创建的实例对象本身
        self._name = name       #一个下划线表示外部调用者不应该直接调用这个属性，但是可以调用到；双下划线表示外部不能直接调用
    def get_name(self):
        return self._name
    def set_name(self, value):
        slef._name = value
    def bark(self):
        print(self.get_name() + 'is making sound wang waang wang...')

class Cat(object):
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name = value
    def mew(self):
        print(self.get_name() + 'is making sound miao miao miao...')

dog = Dog('旺财')
cat = Cat('Kitty')
dog.bark()
cat.mew()
