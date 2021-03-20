#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/13 10:03
# @Author : ZY
# @File : 1.py
# @Project : APP
from dataDriver.excelData import ReadExcel, WriteExcel
from dataDriver.yamlData import writeYaml
from dataDriver.yamlData import readYaml

a = [["15239938038", "bowen123456"], ["15239938038", "bowen12345"]]
b = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "4LWSPFMBPV85EMPR",
    "appPackage": "com.youkagames.gameplatform",
    "appActivity": "com.youkagames.gameplatform.activity.SplashActivity",
    "noReset": "False"
}

# writeYaml('a.yml', a)
print(readYaml('a.yml'))

# a = [[1, 2], ["王"]]
# WriteExcel("a.xlsx", "博文", "a").set_all_rows([[1, 2], ["王"]])

# ReadExcel("a.xlsx").get_all_rows("Sheet1", 0)
# WriteExcel()
