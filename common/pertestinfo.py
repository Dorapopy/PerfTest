#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Auth : Dora
@Date : 2022/4/26 15:43
"""
import os, csv, time, datetime
from time import sleep


# 正式可用


class PertestInfo():
    def __init__(self, appName, runtime, file_name):
        self.runtime = runtime  # 函数运行时长,单位：分钟
        self.alldata = [
            ('id', 'current_time', 'CPU[%](单核)', 'battery[%]', 'temperature[℃]',
             'Memory-Uss[MB]')]  # 'Memory-Vss[MB]', 'Memory-Rss[MB]','Memory-Pss[MB]',
        self.appName = appName  # 要测试的app
        self.current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        uuid_str = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + self.appName
        self.file_name = file_name

    def get_battery_temperature(self):
        # 获取电量和电池温度
        result = os.popen("adb shell dumpsys battery")  # .read()
        print(result)
        batterytemp = {'battery': '', 'temperature': ''}
        for line in result:
            print("line:{}-----", line)
            if "level" in line:
                batterytemp['battery'] = int(line.split(":")[1])
                print("batterytemp:{},type(batterytemp):{}".format(batterytemp, type(batterytemp)))

            if "temperature" in line:
                batterytemp['temperature'] = int(line.split(":")[1]) / 10
                print("batterytemp:{},type(batterytemp):{}".format(batterytemp, type(batterytemp)))
        print("batterytemp:", batterytemp)
        return batterytemp

    def get_CPU_dumpsys_cpuinfo(self):
        # 获取app占用的CPU信息 #废弃
        # 使用命令：adb shell dumpsys cpuinfo | findstr com.zego.goavatar
        result = os.popen("adb shell dumpsys cpuinfo | findstr " + self.appName).read()
        print("result:{},type(result):{}".format(result, type(result)))
        # CPUinfo = float(result.split("%")[0].lstrip())/8  # lstrip() 去掉字符串前的空格,/8：除以核数，求单核数据
        CPUinfo = result.split("%")[0].lstrip()  # lstrip() 去掉字符串前的空格
        print("CPUinfo:{},type(CPUinfo):{}".format(CPUinfo, type(CPUinfo)))
        return CPUinfo

    def get_CPU_top(self):
        # 获取app占用的CPU信息
        # 使用命令：adb shell top -n 1
        result = os.popen("adb shell top -n 1")  # .read()
        print("result:{},type(result):{}".format(result, type(result)))
        cpuinfo = 0
        if self.appName == 'com.zego.goavatar':
            for line in result.readlines():
                # print("line:{}-----", line)
                if "com.zego.goava" in line:
                    # print("line:{}-----", line)
                    line = '#'.join(line.split())
                    print("line:{}-----XXXXX", line)
                    cpuinfo = round(float(line.split("#")[-4]) / 8, 2)  # /8:单核CPU数值
        elif self.appName == 'im.zego.GoEnjoy':
            for line in result.readlines():
                # print("line:{}-----", line)
                if "im.zego.GoEnjoy" in line:
                    # print("line:{}-----", line)
                    line = '#'.join(line.split())
                    print("line:{}-----XXXXX", line)
                    cpuinfo = float(line.split("#")[-4]) / 8  # /8:单核CPU数值
        elif self.appName == 'com.vavaparty.app':
            for line in result.readlines():
                # print("line:{}-----", line)
                if "com.vavaparty" in line:
                    # print("line:{}-----", line)
                    line = '#'.join(line.split())
                    print("line:{}-----XXXXX", line)
                    cpuinfo = float(line.split("#")[-4]) / 8  # /8:单核CPU数值
        elif self.appName == 'com.zego.avatartest':
            for line in result.readlines():
                # print("line:{}-----", line)
                if "com.zego.avatar" in line:
                    # print("line:{}-----", line)
                    line = '#'.join(line.split())
                    print("line:{}-----XXXXX", line)
                    cpuinfo = float(line.split("#")[-4]) / 8  # /8:单核CPU数值

        return cpuinfo

    def get_memoryinfo(self):
        # 获取内存信息，使用Uss：进程独占内存
        result = os.popen("adb shell su -c 'procrank'").read()  # 需要手机已经root
        # print("result:", result)
        meminfo = {'Vss': '', 'Rss': '', 'Pss': '', 'Uss': ''}
        for line in result.splitlines():
            if self.appName in line:
                # print("line:{}-----", line)
                line = '#'.join(line.split())
                print("line:{}-----", line)
                meminfo['Vss'] = int(line.split("#")[1].rstrip('K')) / 1024  # rstrip('K'):去掉K，/1024换算成Mb
                meminfo['Rss'] = int(line.split("#")[2].rstrip('K')) / 1024
                meminfo['Pss'] = int(line.split("#")[3].rstrip('K')) / 1024
                meminfo['Uss'] = round(int(line.split("#")[4].rstrip('K')) / 1024, 2)  #round(a, 2) 将a通过round函数处理后赋值给a1，传入的2代表保留两位小数
                # print("Uss:", meminfo['Uss'])
        # print("meminfo:", meminfo)
        return meminfo

    def run(self):
        # 执行获取数据函数
        now = datetime.datetime.now()
        print("now:", now)
        Rtime = now + datetime.timedelta(minutes=self.runtime)  # 指定运行5min
        id = 1  # id：可以运行的次数
        while Rtime > datetime.datetime.now():
            # 指定时间跑
            batterytemp = self.get_battery_temperature()  # 获取电量和电池温度
            sleep(1)
            CPUinfo = self.get_CPU_top()  # 获取app占用的CPU信息
            sleep(1)
            meminfo = self.get_memoryinfo()
            sleep(1)
            self.alldata.append((
                str(id), str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())), str(CPUinfo),
                batterytemp['battery'], batterytemp['temperature'],
                meminfo['Uss']))  # meminfo['Vss'],meminfo['Rss'], meminfo['Pss'],
            id = id + 1
            sleep(5)
        # 保存数据
        with open('../data/%s' % self.file_name, 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerows(self.alldata)
            file.close()


if __name__ == '__main__':
    redmenote7 = PertestInfo(appName='com.zego.avatartest', runtime=5, file_name="avatartest_pertest12.csv")
    # redmenote7 = PertestInfo(appName='im.zego.GoEnjoy', runtime=3)
    redmenote7.run()

    # redmenote7.get_battery_temperature()
