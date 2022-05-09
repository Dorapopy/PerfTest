#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2022/5/822:12
# @Author   : Dora

import datetime, time, csv
from time import sleep
from common.pertestinfo import PertestInfo


class ComFunc:
    def __init__(self):
        self.current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        self.appName = 'com.zego.goavatar'
        self.alldata = [
            ('id', 'current_time', 'CPU[%](单核)', 'battery[%]', 'temperature[℃]',
             'Memory-Uss[MB]')]

    def sleep_wait_data(self):
        # 等待数据稳定
        return sleep(60)

    def sleep_wait_cooldown(self):
        # 等待手机降温
        return sleep(10)

    def com_run_perfinfo(self,runtage = True):
        # 跑全功能UI自动化时，顺便收集性能数据的运行方法
        # 执行获取数据函数
        self.runtage = runtage
        Per_file_name = self.current_time + '.csv'  # 性能数据文件
        pertest = PertestInfo(self.appName, runtime="", file_name=Per_file_name)  # 实例化性能测试对象

        now = datetime.datetime.now()
        print("now:", now)
        # Rtime = now + datetime.timedelta(minutes=self.runtime)  # 指定运行5min
        id = 1  # id：可以运行的次数
        while self.runtage:
            # 指定时间跑
            batterytemp = pertest.get_battery_temperature()  # 获取电量和电池温度
            sleep(1)
            CPUinfo = pertest.get_CPU_top()  # 获取app占用的CPU信息
            sleep(1)
            meminfo = pertest.get_memoryinfo()
            sleep(1)
            self.alldata.append((
                str(id), str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())), str(CPUinfo),
                batterytemp['battery'], batterytemp['temperature'],
                meminfo['Uss']))  # meminfo['Vss'],meminfo['Rss'], meminfo['Pss'],
            id = id + 1
            sleep(5)
        # 保存数据
        with open('../data/%s' % Per_file_name, 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerows(self.alldata)
            file.close()
