#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Auth : Dora
@Date : 2022/4/26 20:36
"""
import csv,os

result = os.popen("adb shell top -n 1")  # .read()
print("result:{},type(result):{}".format(result, type(result)))
cpuinfo = 0
for line in result.readlines():
    print("line:{}-----", line)
    if "im.zego.GoEnjoy" in line:
        # print("line:{}-----", line)
        line = '#'.join(line.split())
        print("line:{}-----XXXXX", line)
        cpuinfo = float(line.split("#")[-4]) / 8  # /8:单核CPU数值
print("cpuinfo:",cpuinfo)