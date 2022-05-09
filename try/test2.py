#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Auth : Dora
@Date : 2022/4/26 18:07
"""

import uiautomator2 as u2
import os,time

t = '273376K'

r = t.rstrip('K')
n = int(r)
print(r,(type(r)))
print(n,(type(n)))

device = u2.connect('6214062a')    # 红米note7，连接wifi:zegolab_c
print(device.info)
current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
print("用例开始执行时间：", current_time)
device.app_stop_all()
device.app_start("com.zego.goavatar")
