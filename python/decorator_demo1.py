# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 12:50:30 2018

@author: guan.c.wang
"""

def makeBold(func):
    def inner():
        return '<b>'+func()+'</b>'
    return inner

def makeItalic(func):
    def inner():
        return '<i>'+func()+'</i>'
    return inner


@makeItalic
@makeBold
def writeHtml():
    return '<a>abc</a>'


print(writeHtml())
