#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2022/4/2411:26
# @Author   : Dora

import os, time, csv
from time import sleep

appName = "com.zego.goavatar"


# 控制类
class Controller_CPU():
    def __init__(self, count):

        self.count = count
        self.alldata = [('timestamp', 'cpustatus')]

    # 单次测试过程
    def testprocess(self):
        result = os.popen("adb shell dumpsys cpuinfo | findstr " + appName) #.read()
        print("result:",result)
        for line in result.readline():
            t = line.split("%")
            cpu_value = line.split("%")[0]
            print("t:{},cpu_value:{}".format(t,cpu_value))
            current_time = self.getCurrentTime()
            self.alldata.append((current_time, cpu_value))

    # 多次执行测试过程
    def run(self):
        while self.count > 0:
            self.testprocess()
            self.count = self.count - 1
            sleep(3)

    # 获取当前的时间戳
    def getCurrentTime(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        return current_time

    # 存储数据
    def SaveDataToCSV(self):

        with open('../data/cpustatus.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow(self.alldata)
            file.close()


if __name__ == '__main__':
    print("adb shell dumpsys cpuinfo | findstr " + appName)
    controller = Controller_CPU(count=5)
    controller.run()
    controller.SaveDataToCSV()
