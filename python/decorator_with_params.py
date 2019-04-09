# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 13:25:06 2018

@author: guan.c.wang


"""

def decoraotr(func):
    def inner(*args , **kwargs  ):
        print('-----begin----')
        func(*args , **kwargs   )
        print('----end----')
        
    return inner


@decoraotr
def test(a , b , c  ):
    print('a = %d , b = %d , c = %c ' %(a , b , c ))
    
@decoraotr
def test2(a , b , c , d ):
    print('a = %d , b = %d , c = %c d = %d' %(a , b , c ,d ))
    
    
@decoraotr
def test3(a , b , c , d):
    print('a = %d , b = %d , c = %c ' %(a , b , c  ))
    for key in d.keys():
        print('key = ' + str(key) + ',  value = '+ str(d[key]) )

test(11, 22,33)
    
    
test2(11,22,33,44)

test3(11,22,33,{'k1' : 44 , 'k2' : 55})