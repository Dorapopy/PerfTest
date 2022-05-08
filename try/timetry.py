#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Auth : Dora
@Date : 2022/4/27 20:49
"""
import datetime
import time
now = datetime.datetime.now()
strnow =str(now)
print("now:",now,type(now),str(now))
print("strnow:",strnow)
runtime = now+datetime.timedelta(seconds=1)
print("newtime:",runtime)

while runtime > datetime.datetime.now():
    print("运行中")
print('end',datetime.datetime.now())
"""
tCurrent = time.time()
print("tCurrent:",tCurrent)
nw = tCurrent+3600*0.01
print("nw:",nw)

while nw > time.time():
    print("OK")
print("end")
"""