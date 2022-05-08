#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Auth : Dora
@Date : 2022/4/25 11:38
"""
import os, csv
from time import sleep


# 看进程在运行过程中占用了多少内存应该看RES的值而不是VIRT的值。

class getMemory():
    def __init__(self):
        self.alldata = [('id', 'VIRT(VSS)', 'RES(RSS)', 'SHR')]

    # 读取数据文件
    def get_read_data(self):
        os.popen('adb shell top -n 10 > E:\pythonProject\PerfTest\data\meminfo1.txt')  # 查看内存，刷新20次（-n）
        sleep(40)
        with open("../data/meminfo1.txt", 'r') as meminfo:
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
        print("alldata:", self.alldata)

    def savedata(self):
        with open('../data/meminfo4pernote7.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerows(self.alldata)
            file.close()


if __name__ == '__main__':
    meminfo = getMemory()
    # meminfo.readfile()
    meminfo.analysedata()
    meminfo.savedata()

    # print("t:{},type(t):{}".format(t,type(t)))
