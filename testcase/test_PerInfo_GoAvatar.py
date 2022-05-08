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


class TestAvatarPerf:
    def setup_class(self):
        self.deviceIP = '192.168.5.206'  # 红米note7
        # self.deviceIP = '192.168.5.204'
        self.device = u2.connect(self.deviceIP + ':5555')
        self.appName = 'com.zego.goavatar'
        self.current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        self.runtime = 30  # 指定函数运行时长，单位：分钟
        self.phone = '红米note7'  # '一加8T'

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
        sleep(3)

    def teardown_method(self):
        print("用例执行结束时间：", self.current_time)
        # 关闭所有app
        self.device.app_stop_all()
        sleep(5)  # 等待10分钟降温

    def teardown_class(self):
        print("所有用例执行结束时间：", self.current_time)

    def test_avatar_homepage_1person(self):
        # Goavatar:在首页1个人，测试30次，收集数据
        print("《《《GoAvatar测试场景1：在首页1个人，测试30次，收集数据》》》")
        sleep(2)  # 等待120S，app稳定再收集数据
        # 实例化性能测试对象
        Per_file_name = self.phone + '-avatar_homepage_1person-' + self.current_time + '.csv'  # 性能数据文件
        self.AvatarPerf = PertestInfo(self.appName, runtime=self.runtime, file_name=Per_file_name)
        # 获取数据并保存数据
        self.AvatarPerf.run()

    def test_avatar_room_4person(self):
        print("《《《GoAvatar测试场景1：在房间4个人，测试30次，收集数据》》》")
        self.device(text='房间').click()  # 进入房间（会自动添加4个人）
        sleep(2)  # 等待数据稳定
        # 实例化性能测试对象
        Per_file_name = self.phone + '-avatar_room_4person-' + self.current_time + '.csv'  # 性能数据文件
        self.AvatarPerf = PertestInfo(self.appName, runtime=self.runtime, file_name=Per_file_name)
        # 获取数据并保存数据
        self.AvatarPerf.run()

    def test_avatar_room_1person(self):
        print("《《《GoAvatar测试场景1：在房间1个人，测试30次，收集数据》》》")
        self.device(text='房间').click()  # 进入房间（会自动添加4个人）
        sleep(2)
        m = 0
        while m < 3:
            self.device(text='踢出用户').click()  # 依次踢出3个用户
            sleep(0.1)
            m = m + 1
        sleep(2)  # 等待数据稳定
        # 实例化性能测试对象
        Per_file_name = self.phone + '-avatar_room_1person-' + self.current_time + '.csv'  # 性能数据文件
        self.AvatarPerf = PertestInfo(self.appName, runtime=self.runtime, file_name=Per_file_name)
        # 获取数据并保存数据
        self.AvatarPerf.run()

    def test_avatar_room_0person(self):
        print("《《《GoAvatar测试场景1：在房间1个人，测试30次，收集数据》》》")
        self.device(text='房间').click()  # 进入房间（会自动添加4个人）
        sleep(2)
        m = 0
        while m < 4:
            self.device(text='踢出用户').click()  # 依次踢出3个用户
            sleep(0.1)
            m = m + 1
        sleep(2)  # 等待数据稳定
        # 实例化性能测试对象
        Per_file_name = self.phone + '-avatar_room_0person-' + self.current_time + '.csv'  # 性能数据文件
        self.AvatarPerf = PertestInfo(self.appName, runtime=self.runtime, file_name=Per_file_name)
        # 获取数据并保存数据
        self.AvatarPerf.run()


if __name__ == '__main__':
    # a=TestAvatarPerf()
    # a.test_avatar_homepage_1person()
    pytest.main(["s"])
    # pytest testcase/test_GoAvatarUI.py -s -q --alluredir=./report --clean-alluredir    # 执行用例
    # allure serve ./report     # 查看报告
