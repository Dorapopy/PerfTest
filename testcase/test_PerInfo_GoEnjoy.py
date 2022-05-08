#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Auth : Dora
@Date : 2022/4/26 16:30
"""
import csv, os, time, pytest
from time import sleep
import uiautomator2 as u2

from testcase.pertestinfo import PertestInfo


class TestAvatarPerf():
    def setup_class(self):
        self.deviceIP = '192.168.5.206'  # 红米note7
        # self.deviceIP = '192.168.5.204'
        self.device = u2.connect(self.deviceIP + ':5555')
        self.appName = 'im.zego.GoEnjoy'
        self.current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        self.runtime = 3  # 取数据组数
        self.phone = '红米note7'  # '红米note7'
        self.Per_file_name = self.phone + "_GoEnjoy_" + self.current_time + '.csv'  # 性能数据文件
        print("用例开始执行时间：", self.current_time)
        print("setup_class:所有用例执行之前运行：清除日志缓存,开始录入logcat日志，再启动GoEnjoy")
        os.popen("adb logcat -c")  # 清理缓存日志
        sleep(2)
        # 输出 adb logcat 日志
        # os.popen("adb logcat > E:\pythonProject\GoEnjoyUIAutoTest\logs\log0322.txt")  # 打印手机端日志
        log_file_name = '%s.txt' % self.current_time
        # print("localtime:", time.localtime())
        os.popen("adb logcat > ../log/%s" % log_file_name)  # 打印日志，日志文件根据时间命名
        # 实例化性能测试对象
        self.AvatarPerf = PertestInfo(self.appName, runtime=self.runtime, file_name=self.Per_file_name)

    def setup_method(self):
        # 类中每个函数执行前运行
        print("用例开始执行时间：", self.current_time)
        # 关闭所有app
        self.device.app_stop_all()
        sleep(2)
        # 启动测试的app
        self.device.app_start(self.appName)
        sleep(3)

    def teardown_method(self):
        print("用例执行结束时间：", self.current_time)

    def teardown_class(self):
        print("所有用例执行结束时间：", self.current_time)

    def test_avatar_room_1person(self):
        print("《《《GoEnjoy测试场景1：房主在房间1个人，测试30次，收集数据》》》")
        self.device(text='在线KTV').click()  # 进创建房间页
        sleep(1)
        self.device(text='创建房间').click()  # 创建房间
        sleep(1)
        self.device(resourceId='im.zego.GoEnjoy:id/et_room_name').send_keys('测试中他人勿进')  # 给房间命名为：测试中他人勿进
        sleep(1)
        self.device.press('back')
        sleep(1)
        self.device()
        self.device(text='创建房间').click()  # 确认创建房间
        sleep(120)  # 创建房间，并等待加载出房主头像，等待数据稳定

        # 获取数据并保存数据
        self.AvatarPerf.run()

    def test_avatar_room_4person(self):
        print("《《《GoEnjoy测试场景1：在房间4个人：1个房主加3个线上观众，测试30次，收集数据》》》")
        self.device(text='在线KTV').click()  # 进创建房间页
        sleep(1)
        self.device(text='创建房间').click()  # 创建房间
        sleep(1)
        self.device(resourceId='im.zego.GoEnjoy:id/et_room_name').send_keys('测试中他人勿进')  # 给房间命名为：测试中他人勿进
        sleep(1)
        self.device.press('back')
        sleep(1)
        self.device(text='创建房间').click()  # 确认创建房间
        sleep(240)  # 创建房间，并等待加载出房主头像，3个观众进入房间，等待数据稳定
        # 获取数据并保存数据
        self.AvatarPerf.run()

    def test_avatar_room_6person(self):
        print("《《《GoEnjoy测试场景1：在房间6个人：1个房主加5个线上观众，测试30次，收集数据》》》")
        self.device(text='在线KTV').click()  # 进创建房间页
        sleep(1)
        self.device(text='创建房间').click()  # 创建房间
        sleep(1)
        self.device(resourceId='im.zego.GoEnjoy:id/et_room_name').send_keys('测试中他人勿进')  # 给房间命名为：测试中他人勿进
        sleep(1)
        self.device.press('back')
        sleep(1)
        self.device(text='创建房间').click()  # 确认创建房间
        sleep(3600)  # 创建房间，并等待加载出房主头像，5个观众进入房间，等待数据稳定
        # 获取数据并保存数据
        self.AvatarPerf.run()


if __name__ == '__main__':
    # a=TestAvatarPerf()
    # a.test_avatar_homepage_1person()
    pytest.main(["s"])
    # pytest testcase/test_GoEnjoyUI.py -s -q --alluredir=./report --clean-alluredir    # 执行用例
    # allure serve ./report     # 查看报告
