#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2022/4/2412:55
# @Author   : Dora

import os, csv
from time import sleep

appName = "com.zego.goavatar"


class CPUdata():
    def __init__(self,count):
        self.count = count
        self.alldata = [('timestamp', 'CPU[%]')]

    def cpuinfo(self):
        result = os.popen("adb shell dumpsys cpuinfo | findstr " + appName).read()
        print("result:{},type(result):{}".format(result, type(result)))
        r = result.split("%")[0].lstrip()  # lstrip() 去掉字符串前的空格
        print("r:{},type(r):{}".format(r, type(r)))
        # n = r + "%
        # print("n:{},type(n):{}".format(n, type(n)))
        """
        m = int(r) / 100
        print(m, type(m))
        """
        return r

    def run(self):
        while self.count>0:
            cpuinfo=self.cpuinfo()
            self.alldata.append((self.count,cpuinfo))
            self.count = self.count -1
            sleep(2)

    def savedata(self):
        with open('../data/cpustatus.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerows(self.alldata)
            file.close()



if __name__ == '__main__':
    getcpu = CPUdata(count=5)
    getcpu.run()
    getcpu.savedata()


