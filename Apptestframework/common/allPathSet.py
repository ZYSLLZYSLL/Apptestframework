#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/13 14:10
# @Author : ZY
# @File : allPathSet.py
# @Project : APP
# 所有配置路径
import time
from dataDriver.yamlData import readYaml


class AllPathSet:
    # 时间戳中不能有冒号
    __t = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()).split("-")
    __t2 = __t[2].split(" ")
    __s = f"{__t[0]}年{__t[1]}月{__t2[0]}日{__t2[1]}时{__t[3]}分{__t[4]}秒"
    __logname = f"{__t[0]}年{__t[1]}月{__t2[0]}日"

    @classmethod
    def SCREENSHORT_Path(cls, info):
        # 截图路径
        path = f"../output/images/{info}+{cls.__s}.png"
        return path

    # 日志路径
    LOG_FILE_PATH = f"../output/log/{__logname}.log"

    # 设备路径，构造参数
    DEVICE_PATH = readYaml("../common/desired_capabilities.yml")["device3"]

    # appium的http地址
    APPIUM_HTTP_PATH = 'http://127.0.0.1:4723/wd/hub'

    # APK_PATH = "../app/com.tal.kaoyan_3.8.1_liqucn.com.apk"
    # common/timedDeleteOutput里面的删除和创建文件夹路径

    # 三天自动清除路径
    REMOVE_MKDIR = r"..\output"
