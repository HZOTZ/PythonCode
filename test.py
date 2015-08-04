#!/usr/bin/env python
#-*-coding:utf-8-*-

import Queue
# import requests
import threading
import time
import random
class Mythread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self._name = name
    def run(self):
        while True:
            if self._name.qsize()>0:    #判断队列非空
                job = self._name.get()  #从队列中取出一条任务
                self.process(job)   #执行该任务
            else :
                break
    def process(self,job):
        print job,' Run'
        time.sleep(random.random()*3)
        print job,' Stop'
q = Queue.Queue(0)  #建立一个队列，0表示不限制队列的长度（无限长）,Queue()先进先出
num = 6 #线程数6
job = num * 5   #总的任务数30
# 创建队列,所有任务的集合
for i in range(job):
    q.put(i)
# 队列长度输出
print q.qsize()
# 从队列中取元素加入到线程中,设置线程
for x in range(num):
    Mythread(q).start() #start函数是Mythread的父类threading.Thread中继承的
while True:
    if q.qsize()<=0:
        print 'Down'
        break
    else :
        time.sleep(0.01)