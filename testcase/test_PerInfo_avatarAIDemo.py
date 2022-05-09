#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Auth : Dora
@Date : 2022/4/27 18:49
"""

import csv, os, time, pytest
from time import sleep
import uiautomator2 as u2

from common.pertestinfo import PertestInfo


class TestAvatarPerf:
    def setup_class(self):
        self.deviceIP = '192.168.5.206'  # 红米note7
        # self.deviceIP = '192.168.5.204'
        self.device = u2.connect(self.deviceIP + ':5555')
        self.appName = 'com.zego.avatartest'
        self.current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        self.runtime = 3  # 取数据组数
        self.phone = '红米note7'  # '一加8T'
        self.Per_file_name = self.phone + "_goAvatar_" + self.current_time + '.csv'  # 性能数据文件
        print("用例开始执行时间：", self.current_time)
        print("setup_class:所有用例执行之前运行：清除日志缓存,开始录入logcat日志，再启动GoAvatar")
        os.popen("adb logcat -c")  # 清理缓存日志
        sleep(2)
        # 输出 adb logcat 日志
        # os.popen("adb logcat > E:\pythonProject\GoAvatarUIAutoTest\logs\log0322.txt")  # 打印手机端日志
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

    def test_avatarAI_AI0Cam0(self):
        # AvatarAIDemo:AI：关闭；表情推理：关闭 =》静默壳子
        print("《《《AvatarAIDemo:AI：关闭；表情推理：关闭 =》静默壳子》》》")
        self.device(text='AI开关').click()  # 关闭AI，进入demo表情推理默认关
        sleep(120)  # 等待120S，app稳定再收集数据
        # 获取数据并保存数据
        self.AvatarPerf.run()

    def test_avatarAI_AI0Cam1(self):
        # AvatarAIDemo:AI：关闭；表情推理：开启 =》摄像头
        print("《《《AvatarAIDemo：AI：关闭；表情推理：开启 =》摄像头》》》")
        self.device(text='AI开关').click()  # 关闭AI
        sleep(1)
        self.device(text='启动表情推理').click()  # 启动表情推理
        sleep(120)  # 等待120S，app稳定再收集数据
        # 获取数据并保存数据
        self.AvatarPerf.run()

    def test_avatarAI_AI1Cam1(self):
        # AvatarAIDemo:AI：关闭；表情推理：开启 =》摄像头
        print("《《《AvatarAIDemo：AI：开启；表情推理：开启 =》AI推理+摄像头》》》")
        self.device(text='启动表情推理').click()  # 启动表情推理，（AI推理默认开启）
        sleep(120)  # 等待120S，app稳定再收集数据
        # 获取数据并保存数据
        self.AvatarPerf.run()


if __name__ == '__main__':
    # a=TestAvatarPerf()
    # a.test_avatar_homepage_1person()
    pytest.main(["s"])
    # pytest testcase/test_GoAvatarUI.py -s -q --alluredir=./report --clean-alluredir    # 执行用例
    # allure serve ./report     # 查看报告
