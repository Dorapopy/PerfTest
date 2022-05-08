#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Auth : Dora
@Date : 2022/4/26 14:18
"""
import os, csv
from time import sleep

# 采用Uss


class meminfo_procrank():
    def __init__(self, count):
        self.alldata = [('id', 'Vss', 'Rss', 'Pss', 'Uss')]
        self.count = count

    def get_meminfo_procrank(self):
        result = os.popen("adb shell su -c 'procrank'").read()
        print("result:", result)
        meminfo = {'Vss': '', 'Rss': '', 'Pss': '', 'Uss': ''}
        for line in result.splitlines():
            if "com.zego.goavatar" in line:
                print("line:{}-----", line)
                line = '#'.join(line.split())
                print("line:{}-----", line)
                meminfo['Vss'] = line.split("#")[1]
                meminfo['Rss'] = line.split("#")[2]
                meminfo['Pss'] = line.split("#")[3]
                meminfo['Uss'] = line.split("#")[4]
                print("Uss:", meminfo['Uss'])
        return meminfo
        # print("memdata:", self.alldata)

    def run(self):
        while self.count > 0:
            meminfo = self.get_meminfo_procrank()
            self.alldata.append((self.count, meminfo['Vss'], meminfo['Rss'], meminfo['Pss'], meminfo['Uss']))
            self.count = self.count - 1
            sleep(2)

    def savedata(self):
        with open('../data/meminfo4pernote7sec1.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerows(self.alldata)
            file.close()


if __name__ == '__main__':
    memprocrank = meminfo_procrank(count=10)
    memprocrank.run()
    memprocrank.savedata()
