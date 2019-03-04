#!/usr/bin/env python3
#-*- coding=utf-8 -*-
"""
#Author: Dang_h
#Creat Time:2019年02月28日 星期四 16时28分13秒
#File Name:mixin.py
#Description:多继承，一个子类可以继承多个父类，因此这个子类拥有所有的父类属性，可以调用父类中的方法。Mixin设计思想：保持继承的单一性原则，一个子类只继承一个主要的类，其他功能拆分出来，单独的一个功能命名为一个类Minxin.
"""

class A:
    def __init__(self):
        self.name = 'xiaoming'
    def testA(self):
        print('----testA----')

class B:
    def __init__(self):
        self.age = 8
    def testB(self):
        print('----testB----')

class Person(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
    def testPerson(self):
        print('----testPerson----')

person = Person()
print(person.name)
print(person.age)
person.testA()
person.testB()
person.testPerson()
