#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Auth : Dora
@Date : 2022/4/27 17:07
"""
import uiautomator2 as u2
from time import sleep
deviceIP = '192.168.5.206'
device = u2.connect(deviceIP + ':5555')
print("《《《GoEnjoy测试场景1：房主在房间1个人，测试30次，收集数据》》》")
device(text='在线KTV').click()  # 进创建房间页
sleep(1)
device(text='创建房间').click()  # 创建房间
sleep(1)
device(resourceId='im.zego.GoEnjoy:id/et_room_name').send_keys('测试中他人勿进')
sleep(1)
device.press('back')
sleep(1)
device(text='创建房间').click()  # 确认创建房间
sleep(120)  # 创建房间，并等待加载出房主头像，等待数据稳定