#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Auth : Dora
@Date : 2022/5/9 11:52
"""

import datetime, time, csv, pytest,random,os
import uiautomator2 as u2
from time import sleep
from common.pertestinfo import PertestInfo
from common.comfunc import ComFunc


class TestUI:
    def setup_class(self):
        self.deviceIP = '192.168.5.206'
        self.device = u2.connect(self.deviceIP + ':5555')
        self.appName = 'com.zego.goavatar'
        self.current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        self.runtime = 1  # 指定函数运行时长，单位：分钟
        self.phone = '红米note7'  # '一加8T'
        self.genderId = 'com.zego.goavatar:id/switch_gender_change'
        print("用例开始执行时间：", self.current_time)
        self.runtage = True
        pertest = ComFunc().com_run_perfinfo(runtage = self.runtage)

    def setup_method(self):
        # 类中每个函数执行前运行
        print("用例开始执行时间：", self.current_time)
        # 关闭所有app
        self.device.app_stop_all()
        sleep(2)
        # 启动测试的app
        self.device.app_start(self.appName)
        sleep(2)
        self.device(text='捏脸').click()
        sleep(2)
        self.device(resourceId=self.genderId).click()  # 使用默认形象进行性能测试

    def teardown_method(self):
        # 关闭所有app
        self.device.app_stop_all()

    def teardown_class(self):
        print("所有用例执行结束时间：", self.current_time)
        self.runtage = False

    def test_avatar_homepage(self):
        sleep(1)
        i = 0
        j = 1
        while i < 3:
            # while i < 3:
            # sleep(1)  # 固定切换的间隔时间
            t = random.randint(20, 2000) / 1000  # 间隔任意时间
            sleep(t)
            self.device.press("home")
            sleep(10)
            # os.system('adb shell am force-stop com.zego.goavatar')  # 杀进程
            process = (os.popen('adb shell ps | findstr com.zego.goavatar')).read()  # 查看app进程
            print("执行第{}次，切前后台间隔{}s".format(j, t))
            assert process  # 断言：进程还在（demo没crash）
            self.device.app_start(self.appName)  # 启动app
            # os.system("adb shell am start -n com.zego.goavatar/com.zego.goavatar.view.KneadFaceActivity")   # abd 启动activitiy
            i = i + 1
            j = j + 1

