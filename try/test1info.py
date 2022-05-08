#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Auth : Dora
@Date : 2022/4/25 11:38
"""
import os, csv


# 看进程在运行过程中占用了多少内存应该看RES的值而不是VIRT的值。

class getMemory():
    def __init__(self, count):
        self.alldata = [('id', 'VIRT(VSS)', 'RES(RSS)', 'SHR')]

    # 读取数据文件
    def get_read_data(self):
        os.popen('adb shell top -n 20 > E:\pythonProject\PerfTest\data\meminfo.txt')    # 查看内存，刷新20次（-n）
        with open("../data/memory.txt", 'r') as meminfo:
            content = meminfo.readlines()
            meminfo.close()
        return content

    # 分析数据
    def analysedata(self):
        content = self.get_read_data()
        i = 1
        for line in content:
            if "com.zego.goavat+" in line:
                line = '#'.join(line.split())
                line = line.rstrip('#')
                print("line:", line)

                PID = line.split('#')[0]
                print("PID:", PID)
                VIRT = line.split('#')[4]
                print("VIRT:", VIRT)

                RES = line.split('#')[5]
                print("RES:", RES)
                SHR = line.split('#')[6]
                print("SHR:", SHR)
                self.alldata.append((str(i), VIRT, RES, SHR))
                i = i + 1

    def batteryinfo(self):

        # os.popen("adb shell dumpsys battery set status 1")    # 设置非充电模式
        # 获取电量
        result = os.popen("adb shell dumpsys battery")  # .read()
        print(result)
        power = ''
        for line in result:
            print("line:{}-----", line)
            if "level" in line:
                power = line.split(":")[1]
                print("!212")
                print("power:{},type(power):{}".format(power, type(power)))

        return power

    def savadata(self):
        with open('../data/meminfo.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerows(self.alldata)
            file.close()




if __name__ == '__main__':
    meminfo = getMemory(count=6)
    # meminfo.readfile()
    meminfo.analysedata()
    meminfo.savadata()

    # print("t:{},type(t):{}".format(t,type(t)))
