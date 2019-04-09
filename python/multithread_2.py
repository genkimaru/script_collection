# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:19:19 2018

@author: guan.c.wang
"""

import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='thread_1')
t2 = threading.Thread(target=loop, name='thread_2')
t.start()
t2.start()
t.join()
t2.join()
print('thread %s ended.' % threading.current_thread().name)