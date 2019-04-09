# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:34:32 2018

@author: guan.c.wang
"""

import threading 
import time


lock = threading.Lock()
def run_lock():    
        lock.acquire()
   #     print('-----------%s'%threading.current_thread().name)
        try:
            print('-----------%s -----%s '% ( threading.current_thread().name , balance))
            changeit()
        finally:
            
            lock.release()
    




balance = 0
def changeit():
    global balance
    balance = balance + 1
    balance = balance - 1

if __name__ == '__main__':
    t1 = threading.Thread(target=run_lock, name='thread_1' , )
    t2 = threading.Thread(target=run_lock, name='thread_2' , )
    t1.start()
    t2.start()
    time.sleep(3)
    print(balance)