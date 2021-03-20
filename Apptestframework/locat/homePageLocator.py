#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 16:42
# @Author : ZY
# @File : homePageLocator.py
# @Project : APP
from appium.webdriver.common.mobileby import By


class HomePageLocator:
    """
        首页元素
    """
    # 关闭新人福利
    downXinRenLocator = (By.ID, "com.youkagames.gameplatform:id/iv_cha")

    # 同意协议
    tongYiLocator = (By.ID, "com.youkagames.gameplatform:id/tv_positive")

    # 同意权限 两次
    tongYiQuanXianLocator = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")

    # 点击我的
    myLocator = (By.XPATH, "//*[contains(@text,'我的')]")
