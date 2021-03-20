#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 15:42
# @Author : ZY
# @File : conftest.py
# @Project : APP
import time

from appium import webdriver
import pytest
from pageObject.my import MyPage
from pageObject.home import HomePage
from pageObject.loginPage import LoginPage
from common.allPathSet import AllPathSet
from common.basePage import BasePage
from locat.homePageLocator import HomePageLocator as loc_h
from locat.loginPageLocator import LoginPageLocator as loc_l
from locat.myPageLocator import MyPageLocator as loc_m

import os

"""
    conftest夹具
"""


def baseDriver():
    # 构造参数
    desired_capabilities = AllPathSet.DEVICE_PATH
    # print(desired_capabilities)
    # 向服务端发送连接信息
    driver = webdriver.Remote(AllPathSet.APPIUM_HTTP_PATH, desired_capabilities)
    driver.implicitly_wait(10)
    return driver
    # driver.close_app()


driver = baseDriver()


@pytest.fixture(scope="class")
def login():
    # 1，进入首页
    BasePage(driver).click_element(loc_h.downXinRenLocator, "首页—关闭新人福利")
    BasePage(driver).click_element(loc_h.tongYiLocator, "首页-同意协议")
    BasePage(driver).click_element(loc_h.tongYiQuanXianLocator, "首页-同意电话权限")
    BasePage(driver).click_element(loc_h.tongYiQuanXianLocator, "首页-同意存储权限")
    # 2，进入我的页面
    BasePage(driver).click_element(loc_h.myLocator, "首页-点击我的")
    # 3，进入登录页面
    BasePage(driver).click_element(loc_m.loginLocator, "我的页面—点击立即登录")
    yield
    driver.close_app()
