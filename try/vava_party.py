#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Auth : Dora
@Date : 2022/4/21 15:13
"""
import uiautomator2 as u2
import os, pytest
from time import sleep

appName = 'com.vavaparty.app'
# deviceName = '6d3e6245' # 一加8T
deviceName = 'RFCNC07D6BX'  # 三星S20
# deviceName = 'R5CN90T6TFM'  # 三星A7160
# deviceName = '88Y0219926039431' # 华为mate30

partyXpath = "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.vavaparty.app:id/recyclerView']/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]"
partyHostXpath="//android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.View[1]"
device = u2.connect(deviceName)
exitBottonId = 'com.vavaparty.app:id/actionQuit'  # 退出派对


def inoutParty():
    device.app_stop_all()
    device.app_start(appName)
    sleep(5)
    j = 1
    i = 0
    while i < 10000:
        sleep(2)
        device(text="测试中他人勿进").click()  # 进入派对
        sleep(5)
        device.xpath(partyHostXpath).click()
        sleep(2)
        # [480,1050][600,1068]   [438,486][642,584]
        device.click(430,600)
        sleep(2)
        device(resourceId=exitBottonId).click()
        sleep(5)
        device(text="离开派对").click()
        process = (os.popen('adb shell ps | findstr com.vavaparty.app')).read()
        print("执行第{}次".format(j))
        assert process  # 断言：VAVA进程是否还活着（没有crash）
        i = i + 1
        j = j + 1

def makeParty():
    device.app_stop_all()
    device.app_start(appName)
    sleep(5)
    j = 1
    i = 0
    while i < 10000:
        sleep(2)
        device(text="发起一场派对")



if __name__ == '__main__':
    # device = u2.connect(deviceName)
    # device.xpath(partyXpath).click()
    # device(text="测试中他人勿进").click()  # 进入派对

    inoutParty()
