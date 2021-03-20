#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 9:40
# @Author : ZY
# @File : loginPage.py
# @Project : APP

# 登录页
import time

from appium import webdriver
from appium.webdriver.common.mobileby import By
from appium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.basePage import BasePage
from locat.loginPageLocator import LoginPageLocator as loc


# 隐形等待 智能等待 一般不单独使用 每个操作大概分配几秒的样子
# driver.implicitly_wait(10)


class LoginPage(BasePage):
    """
        登录页操作内容
    """

    # def __init__(self, driver: Remote):
    #     self.driver = driver

    def input_user(self, user):
        self.input_element(user, loc.userLocator, "登录页-输入账号")

    def input_password(self, password):
        self.input_element(password, loc.passwordLocator, "登录页-输入密码")

    def click_login_button(self):
        self.click_element(loc.loginButtonLocator, "登录页-点击登录")

    # toast  模糊匹配: //*[contains(@text,'部分内容')]
    def check_toast(self):
        return self.get_element_toast(loc.agreement_toastLocator, "登录页-toast文本")

    def get_input_user_text(self):
        return self.get_element_text(loc.userLocator, "登录页-输入汉字,英文，特殊字符")
