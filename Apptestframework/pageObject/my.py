#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 9:44
# @Author : ZY
# @File : my.py
# @Project : APP

from appium import webdriver
from appium.webdriver.common.mobileby import By
from appium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 日历
from locat.myPageLocator import MyPageLocator as loc
from common.basePage import BasePage


class MyPage(BasePage):
    """
        我的页面-操作内容
    """

    def click_li_ji_login_button(self):
        self.click_element(loc.loginLocator, "我的页面—点击立即登录")

    def get_user_text(self):
        return self.get_element_text(loc.userTextLocator, "我的页面-获取登录用户名")
