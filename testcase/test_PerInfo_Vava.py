#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Auth : Dora
@Date : 2022/5/9 18:08
"""

import csv, os, time, pytest
from time import sleep
import uiautomator2 as u2

from common.pertestinfo import PertestInfo
from common.comfunc import ComFunc

partyXpath = "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.vavaparty.app:id/recyclerView']/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]"
partyHostXpath="//android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.View[1]"
# device = u2.connect(deviceName)
exitBottonId = 'com.vavaparty.app:id/actionQuit'  # 退出派对

class TestVavaPerf:
    def setup_class(self):
        self.deviceIP = '192.168.5.206'  # 红米note7
        # self.deviceIP = '192.168.1.106'
        self.device = u2.connect(self.deviceIP + ':5555')
        self.appName = 'com.vavaparty.app'
        self.current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        self.runtime = 20  # 指定函数运行时长，单位：分钟
        self.phone = '红米note7'  # '一加8T'
        self.mineId = 'XXXX'   # 个人中心Id
        print("用例开始执行时间：", self.current_time)
        print("setup_class:所有用例执行之前运行：清除日志缓存,开始录入logcat日志，再启动GoAvatar")
        os.popen("adb logcat -c")  # 清理缓存日志
        sleep(2)
        # 输出 adb logcat 日志
        # os.popen("adb logcat > E:\pythonProject\GoAvatarUIAutoTest\logs\log0322.txt")  # 打印手机端日志
        log_file_name = '%s.txt' % self.current_time
        # print("localtime:", time.localtime())
        os.popen("adb logcat > ../log/%s" % log_file_name)  # 打印日志，日志文件根据时间命名

    def setup_method(self):
        # 类中每个函数执行前运行
        print("用例开始执行时间：", self.current_time)
        # 关闭所有app
        self.device.app_stop_all()
        sleep(2)
        # 启动测试的app
        self.device.app_start(self.appName)
        sleep(2)

    def teardown_method(self):
        print("用例执行结束时间：", self.current_time)
        # 关闭所有app
        self.device.app_stop_all()
        ComFunc().sleep_wait_cooldown()  # 等待10分钟降温

    def teardown_class(self):
        print("所有用例执行结束时间：", self.current_time)

    def test_vava_room_6person(self):
        # Vava:在房间6个人，测试20min，收集数据
        print("《《《Vava测试场景1：在房间6个人，测试20min，收集数据》》》")
        self.device(text="测试中他人勿进").click()  # 进入派对
        ComFunc().sleep_wait_data()  # 等待60S，app稳定再收集数据
        Per_file_name = self.phone + '-Vava_房间6个人-' + self.current_time + '.csv'  # 性能数据文件
        self.AvatarPerf = PertestInfo(self.appName, runtime=self.runtime, file_name=Per_file_name) # 实例化性能测试对象
        # 获取数据并保存数据
        self.AvatarPerf.run()

    def test_vava_makeface(self):
        print("《《《Vava测试场景2：在捏脸页面，测试20min，收集数据》》》")
        self.device(resourceId=self.mineId).click()  # 进入个人中心
        sleep(2)
        self.device(text="修改我的化身").click()  # 进入捏脸页面
        sleep(10)   # 等待捏脸新娘关系出现
        ComFunc().sleep_wait_data()  # 等待数据稳定
        # 实例化性能测试对象
        Per_file_name = self.phone + '-Vava_在捏脸页面-' + self.current_time + '.csv'  # 性能数据文件
        self.AvatarPerf = PertestInfo(self.appName, runtime=self.runtime, file_name=Per_file_name)
        # 获取数据并保存数据
        self.AvatarPerf.run()


if __name__ == '__main__':
    # a=TestAvatarPerf()
    # a.test_avatar_homepage_1person()
    pytest.main(["test_PerInfo_Vava.py"])
    # pytest testcase/test_GoAvatarUI.py -s -q --alluredir=./report --clean-alluredir    # 执行用例
    # allure serve ./report     # 查看报告
