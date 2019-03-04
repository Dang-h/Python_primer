#!/usr/bin/env python3
#-*- coding=utf-8 -*-
"""
#Author: Dang_h
#Creat Time:2019年02月28日 星期四 15时38分16秒
#File Name:animal.py
#Description:
"""

class Animal(object):            #定义一个父类,共同属性，有名字，会叫
    def __init__(self, name):           #初始化设置名字
        self._name = name
    def get_name(self):         #获取名字，私有属性不可直接访问，因此设置该方法获取属性值       
        return self._name
    def set_name(self, value):          #设置私有属性值
        self._name = value
    def make_sound(self):
        pass

#Dog和Cat继承了父类get_name和make_sound方法；重写父类指的是在子类中定义和父类同名的方法
class Dog(Animal):          #继承父类Aimal
    def make_sound(self):           #重写父类的make_sound
        print(self.get_name() + 'is making sound wang wang wang...')

class Cat(Animal):
    def make_sound(self):
        print(self.get_name() + 'is making sound miao miao miao...')

animals = [Dog('旺财'), Cat('Kitty'), Dog('Laifu'), Cat('Betty')]   #多态的实现

for animal in animals:  #同一方法对不同对象产生结果
    animal.make_sound()

dog = Dog('旺财')
cat = Cat('Kitty')
dog.make_sound()
cat.make_sound()
