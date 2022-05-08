#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2022/4/2412:55
# @Author   : Dora

import os, csv
from time import sleep

appName = "com.zego.goavatar"


class CPUdata():
    def __init__(self, count):
        self.count = count
        self.alldata = [('timestamp', 'CPU[%]')]

    def cpuinfo(self):
        result = os.popen("adb shell top -n 1")#.read()
        print("result:{},type(result):{}".format(result, type(result)))
        cpu1 = 0
        for line in result.readlines():
            #print("line:{}-----", line)
            if "com.zego.goavat+" in line:
                print("line:{}-----", line)
                line = '#'.join(line.split())
                print("line:{}-----XXXXX", line)
                cpu1 = float(line.split("#")[-4])/8  # /8:单核CPU数值
                print("cpu1:",cpu1)
        return cpu1

    def run(self):
        while self.count > 0:
            cpuinfo = self.cpuinfo()
            self.alldata.append((self.count, str(cpuinfo)))
            self.count = self.count - 1
            sleep(2)

    def savedata(self):
        with open('../data/cpustatus113.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerows(self.alldata)
            file.close()


if __name__ == '__main__':
    getcpu = CPUdata(count=1)
    getcpu.run()
    getcpu.savedata()
