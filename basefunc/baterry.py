#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Auth : Dora
@Date : 2022/4/25 11:38
"""
import os, csv
from time import sleep

class getBattery():
    def __init__(self,count):
        self.count = count
        self.alldata = [('timestamp', 'batterydata','temperature')]

    def batteryinfo(self):

        # os.popen("adb shell dumpsys battery set status 1")    # 设置非充电模式
        # 获取电量
        result = os.popen("adb shell dumpsys battery")  # .read()
        print(result)
        batteryinfo = {'battery':'','temperature':''}
        for line in result:
            print("line:{}-----", line)
            if "level" in line:
                batteryinfo['battery'] = line.split(":")[1]
                print("!212")
                print("power:{},type(power):{}".format(batteryinfo, type(batteryinfo)))
                # self.alldata.append(("level", power))
                # print("self.alldata:{},type(self.alldata):{}".format(self.alldata, type(self.alldata)))
            if "temperature" in line:
                batteryinfo['temperature'] = line.split(":")[1]
                print("batteryinfo:{},type(batteryinfo):{}".format(batteryinfo, type(batteryinfo)))

        return batteryinfo

    def savedata(self):
        with open('../data/batterystatus.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerows(self.alldata)
            file.close()

    def run(self):
        while self.count > 0:
            powerinfo = self.batteryinfo()
            self.alldata.append((self.count, powerinfo['battery'],powerinfo['temperature']))
            self.count = self.count - 1
            sleep(2)


if __name__ == '__main__':
    batteryinfo=getBattery(count=8)
    batteryinfo.run()
    batteryinfo.savedata()