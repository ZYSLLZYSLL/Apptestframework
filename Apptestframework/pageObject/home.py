#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 9:46
# @Author : ZY
# @File : home.py
# @Project : APP

from appium import webdriver
from appium.webdriver.common.mobileby import By
from appium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locat.homePageLocator import HomePageLocator as loc
from common.basePage import BasePage


# 我的

class HomePage(BasePage):
    """
        首页-操作内容
    """

    def click_down_xin_ren(self):
        self.click_element(loc.downXinRenLocator, "首页—关闭新人福利")

    def click_tong_yi(self):
        self.click_element(loc.tongYiLocator, "首页-同意协议")

    def click_quan_xian(self):
        self.click_element(loc.tongYiQuanXianLocator, "首页-同意电话权限")
        self.click_element(loc.tongYiQuanXianLocator, "首页-同意存储权限")

    def click_my(self):
        self.click_element(loc.myLocator, "首页-点击我的")
