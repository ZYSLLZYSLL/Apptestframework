#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 16:42
# @Author : ZY
# @File : myPageLocator.py
# @Project : APP
from appium.webdriver.common.mobileby import By


class MyPageLocator:
    """
        我的页面元素
    """
    # 点击立即登录
    loginLocator = (By.ID, "com.youkagames.gameplatform:id/tv_name")

    # 获取用户名
    userTextLocator = (By.ID, "com.youkagames.gameplatform:id/tv_name")


