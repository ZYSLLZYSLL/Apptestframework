#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/13 19:27
# @Author : ZY
# @File : timedDeleteOutput.py
# @Project : APP
import os
import time
from common.allPathSet import AllPathSet

"""
    每三天清除一次output文件里面的内容
"""


class TimedDeleteOutput:
    t = time.time()

    def writeTime(self):
        """
        把时间写入文件
        :return:
        """
        with open("../common/t.txt", "w", encoding='utf-8') as f:
            f.write(str(self.t))

    def removeMkdir(self, filename):
        """
        执行删除和创建文件夹来达成清空文件夹的目的
        :param filename: 要清空的文件夹名字
        :return:
        """
        time.sleep(0.01)
        os.popen(f'rd /s/q {AllPathSet.REMOVE_MKDIR}\{filename}')
        time.sleep(0.01)
        os.popen(f'mkdir {AllPathSet.REMOVE_MKDIR}\{filename}')

    def run(self):
        """
        判断时间是否超过三天，超过就清空文件夹
        :return:
        """
        if os.path.exists("../common/t.txt"):
            with open("../common/t.txt", "r", encoding='utf-8') as f:
                current = float(f.read())  # 文件里的时间
                jingGuotime = float(self.t) - current  # 和文件夹里面时间相比过了多久（秒）

                shengyu_time = (3 * 86400) - jingGuotime  # 剩余总秒数

                d = int(shengyu_time // 86400)
                h = int((3 - d) * 86400 - jingGuotime) // 3600
                f = int(((3 - d) * 86400 - h * 3600) - jingGuotime) // 60
                s = int(60 - (jingGuotime - (jingGuotime // 60 * 60)))

                print(f"剩余{d}天{h}个小时{f}分钟{s}秒后清除output文件内容")

                if jingGuotime > (3 * 86400):  # 时间
                    dir_list = os.listdir("../output")  # 遍历output下文件
                    for i in dir_list[0:-1]:
                        self.removeMkdir(i)

                    self.writeTime()
        else:
            self.writeTime()
