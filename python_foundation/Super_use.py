#!/usr/bin/env python3
#-*- coding=utf-8 -*-
"""
#Author: Dang_h
#Creat Time:2019年02月28日 星期四 16时18分48秒
#File Name:Super_use.py
#Description:
"""

class Animal(object):
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, age):
        #super().__init__(name)          #继承中子类想使用父类的__init__中的属性，可以使用super()调用
        #写法2
        #super(Dog, self).__init__(name)
        #写法3
        Animal.__init__(self, name)
        self.age = age

dog = Dog('旺财', 2)
print(dog.name)
