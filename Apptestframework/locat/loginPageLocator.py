#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 16:37
# @Author : ZY
# @File : loginPageLocator.py
# @Project : APP
from appium.webdriver.common.mobileby import By


class LoginPageLocator:
    """
        登录页元素
    """
    # 输入账号
    userLocator = (By.ID, "com.youkagames.gameplatform:id/phoneNum")

    # 输入密码
    passwordLocator = (By.ID, "com.youkagames.gameplatform:id/password")

    # 点击登录
    loginButtonLocator = (By.ID, "com.youkagames.gameplatform:id/login")

    # toast
    agreement_toastLocator = (By.XPATH, "//*[contains(@text,'账号密码不正确')]")

    # 账号密码都为空时/账号为空，密码填写 的toast
    userNoneLocator = (By.XPATH, "//*[contains(@text,'请输入手机号')]")

    # 账号填写，密码为空 的toast
    passwordNoneLocator = (By.XPATH, "//*[contains(@text,'请输入密码')]")

    # 第三方登录-微信
    loginWechatLocator = (By.ID, "com.youkagames.gameplatform:id/wechat_login_id")
    # 验证结果
    loginWechatLocator_jg = (By.XPATH, "//*[contains(@text,'绑定手机号')]")
    # 取消
    loginWechatLocator_Quxiao = (By.ID, "com.youkagames.gameplatform:id/iv_left")

    # 第三方登录-QQ
    loginQQLocator = (By.ID, "com.youkagames.gameplatform:id/qq_login_id")
    # 验证结果
    loginQQLocator_jg = (By.XPATH, "//*[contains(@text,'QQ授权登录')]")
    # 取消
    loginQQLocator_Quxiao = (By.ID, "com.tencent.mobileqq:id/ivTitleBtnRightText")

    # 第三方登录-微博
    loginWeiBoLocator = (By.ID, "com.youkagames.gameplatform:id/sina_login_id")
    # 验证结果
    loginWeiBoLocator_jg = (By.XPATH, "//*[contains(@text,'微博登录')]")
    # 取消
    loginWeiBoLocator_Quxiao = (By.ID, "com.sina.weibo:id/titleBack")

    t1Locator = (By.XPATH, "//*[contains(@text,'用户协议')]")
    t_Locator_quxiao = (By.ID, "com.youkagames.gameplatform:id/left_layout")
    t2Locator = (By.XPATH, "//*[contains(@text,'隐私协议')]")
    t3Locator = (By.XPATH, "//*[contains(@text,'平台服务协议')]")
