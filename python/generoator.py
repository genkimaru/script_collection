# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 08:22:50 2018

@author: guan.c.wang

generator
"""


class Test():
    def __call__(self):
        return 'aaa'
    __slots__ = ('name' , 'age')

def gen1():
    i = 1
    while i < 5:
        print('---before yield')
        yield i*i
        print('---after yield')
        i = i + 1
        
t = Test()
#t.name = 'allen'
t.sex = 'male'
print(t.sex)