#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Auth : Dora
@Date : 2022/4/26 13:05
"""
import os,csv
from time import sleep
# adb shell
# su
# procrank
memdata=[('Vss', 'Rss', 'Pss','Uss')]

result = os.popen("adb shell su -c 'procrank'").read()
print("result:",result)
for line in result.splitlines():
    # python 执行shell-多行命令-su,拿到值
    if "com.zego.goavatar" in line:
        print("line:{}-----", line)
        print("!212")
        line = '#'.join(line.split())
        print("line:{}-----", line)
        Vss = line.split("#")[1]
        Rss = line.split("#")[2]
        Pss = line.split("#")[3]
        Uss = line.split("#")[4]
        print("Uss:", Uss)
        memdata.append((Vss, Rss, Pss, Uss))

print("memdata:", memdata)
