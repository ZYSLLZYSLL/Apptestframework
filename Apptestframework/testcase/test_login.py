#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 11:01
# @Author : ZY
# @File : test_login.py
# @Project : APP
import time

from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObject.my import MyPage
from pageObject.home import HomePage
from pageObject.loginPage import LoginPage
from common.basePage import BasePage
from testcase.conftest import baseDriver
from log_ri_zhi.logHandler import LogHandler
from locat.homePageLocator import HomePageLocator as loc_h
from locat.loginPageLocator import LoginPageLocator as loc_l
from locat.myPageLocator import MyPageLocator as loc_m
# 把driver传过来
from testcase.conftest import driver
# 把driver传过来
driver = driver


@pytest.mark.usefixtures('login')
class TestLogin:
    logger = LogHandler.logger

    # 验证手机号输入框不能输入汉字，字母，特殊字符，
    @pytest.mark.cs
    @pytest.mark.parametrize('title,user', [["汉字", "中国"], ["字母", 'abc'], ["特殊字符", 'rt(123);</ja']])
    def test_login_user_01(self, title, user):
        BasePage(driver).input_element(user, loc_l.userLocator, f"登录页-输入  {title}")
        # 断言输入框输不进去汉字，默认字符是 请输入手机号
        assert BasePage(driver).get_element_toast(loc_l.userLocator, "登录页-输入汉字,英文，特殊字符") == "请输入手机号"

    # 验证：手机号输入框能输入数字
    @pytest.mark.parametrize('jg,user', [['1234', '1234'], ['12345678901', '1234567890123'],
                                         ['12345678901', '12345678901']])
    def test_login_user_02(self, jg, user):
        BasePage(driver).input_element(user, loc_l.userLocator, f"登录页-输入数字账号为：  {user}")
        assert BasePage(driver).get_element_text(loc_l.userLocator, "登录页-账号输入框能输入数字") == jg

    # 验证：密码输入框不能输入汉字
    def test_login_password_03(self):
        BasePage(driver).input_element('中国', loc_l.passwordLocator, "登录页-密码框输入汉字")
        assert BasePage(driver).get_element_text(loc_l.passwordLocator, "登录页-密码框输入汉字") == "请输入密码"

    # 验证：密码输入框能输入字母，特殊字符，数字
    def test_login_password_04(self):
        BasePage(driver).input_element('1234abc@#', loc_l.passwordLocator, "登录页-密码框输入字母，特殊字符，数字")
        assert BasePage(driver).get_element_text(loc_l.passwordLocator, "登录页-密码框输入汉字") == "•••••••••"

    # 验证：账号/密码错误不能登录
    @pytest.mark.parametrize('user,password,', [["1523993803", "bowen123456"], ["15239938038", "bowen12345"],
                                                ["1523993803", "bowen12345"]])
    def test_login_password_05(self, user, password):
        BasePage(driver).input_element(user, loc_l.userLocator, "登录页-账号/密码错误不能登录-输入账号")
        BasePage(driver).input_element(user, loc_l.passwordLocator, "登录页-账号/密码错误不能登录-输入账号")
        BasePage(driver).click_element(loc_l.loginButtonLocator, "登录页-点击登录")
        assert BasePage(driver).get_element_toast(loc_l.agreement_toastLocator, "登录页-账号/密码错误不能登录toast") == "账号密码不正确"

    # 验证：账号密码都为空/账号为空，密码正确不能登录
    @pytest.mark.parametrize('user,password,', [["", ""], ["", "bowen123456"]])
    def test_login_password_06(self, user, password):
        BasePage(driver).input_element(user, loc_l.userLocator, "登录页-账号/密码错误不能登录-输入账号")
        BasePage(driver).input_element(password, loc_l.passwordLocator, "登录页-账号/密码错误不能登录-输入账号")
        BasePage(driver).click_element(loc_l.loginButtonLocator, "登录页-点击登录")
        assert BasePage(driver).get_element_toast(loc_l.userNoneLocator, "登录页-账号/密码错误不能登录toast") == "请输入手机号"

    # 验证：输入手机号，密码为空不能登录
    @pytest.mark.parametrize('user,password,', [["15239938038", ""]])
    def test_login_password_07(self, user, password):
        BasePage(driver).input_element(user, loc_l.userLocator, "登录页-输入账号")
        BasePage(driver).input_element(password, loc_l.passwordLocator, '登录页-密码为空')
        BasePage(driver).click_element(loc_l.loginButtonLocator, "登录页-点击登录")
        assert BasePage(driver).get_element_toast(loc_l.passwordNoneLocator, "登录页-输入账号，密码为空不能登录") == "请输入密码"

    # 验证：第三方登录选择QQ页面可以跳转
    def test_login_password_08(self):
        BasePage(driver).click_element(loc_l.loginQQLocator, '登录页-选择第三方登录-QQ')  # 543 1453
        assert BasePage(driver).get_element_text(loc_l.loginQQLocator_jg, '登录页-选择第三方登录-QQ') == "QQ授权登录"

    # 验证：第三方登录选择微信页面可以跳转
    def test_login_password_09(self):
        BasePage(driver).click_element(loc_l.loginQQLocator_Quxiao, '登录页-第三方-退出微信第三方')
        BasePage(driver).click_element(loc_l.loginWechatLocator, '登录页-选择第三方登录-微信')
        assert BasePage(driver).get_element_text(loc_l.loginWechatLocator_jg, '登录页-选择第三方登录-微信') == "绑定手机号"

    # 验证：第三方登录选择微博页面可以跳转
    def test_login_password_10(self):
        BasePage(driver).click_element(loc_l.loginWechatLocator_Quxiao, '登录页-第三方-退出微信第三方')
        BasePage(driver).click_element(loc_l.loginWeiBoLocator, '登录页-选择第三方登录-微博')
        assert BasePage(driver).get_element_text(loc_l.loginWeiBoLocator_jg, '登录页-选择第三方登录-QQ') == "微博登录"

    # 验证：登录页能点开相应协议
    def test_login_password_11(self):
        BasePage(driver).click_element(loc_l.loginWeiBoLocator_Quxiao, '登录页-第三方-退出微博第三方')
        # BasePage(driver).click_element(loc_l.t1Locator, '登录页-选择用户协议')
        # BasePage(driver).screenshort("登录页-选择用户协议")
        # BasePage(driver).click_element(loc_l.t_Locator_quxiao, '登录页-退出用户协议')
        # time.sleep(0.5)
        # BasePage(driver).click_element(loc_l.t2Locator, '登录页-选择隐私协议')
        # BasePage(driver).screenshort("登录页-选择隐私协议")
        # BasePage(driver).click_element(loc_l.t_Locator_quxiao, '登录页-退出用户协议')
        # time.sleep(0.5)
        # BasePage(driver).click_element(loc_l.t3Locator, '登录页-选择平台服务协议')
        # BasePage(driver).screenshort("登录页-选择平台服务协议")
        # BasePage(driver).click_element(loc_l.t_Locator_quxiao, '登录页-退出平台服务协议')

    # 正常登录,正确的账号，正确的密码
    @pytest.mark.parametrize('user,password', [["15239938038", "bowen123456"]])
    def test_login_sucess(self, user, password):
        BasePage(driver).input_element(user, loc_l.userLocator, "登录页-输入账号")
        BasePage(driver).input_element(password, loc_l.passwordLocator, "登录页-输入密码")
        BasePage(driver).click_element(loc_l.loginButtonLocator, "登录页-点击登录")
        # 5，断言获取用户名和预期结果是否相同
        assert BasePage(driver).get_element_text(loc_m.userTextLocator, "我的页面-获取登录用户名") == "ZYSLL"
