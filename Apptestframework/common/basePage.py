#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 11:35
# @Author : ZY
# @File : basePage.py
# @Project : APP
from appium import webdriver
from appium.webdriver.common.mobileby import By
from appium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from log_ri_zhi.logHandler import LogHandler
from common.allPathSet import AllPathSet
import time

"""
    公共类，写公共方法
"""


class BasePage:
    logger = LogHandler.logger

    def __init__(self, driver: Remote):
        self.driver = driver

    def get_element_object(self, loc, info):
        """
        定位元素
        :param loc: 例子：(By.ID, "com.tal.kaoyan:id/tip_commit")
        :param info: 例子：功能模块，描述功能（红包页面）
        :return: 定位到的元素
        """
        try:
            m = self.driver.find_element(*loc)
            self.logger.info(f"{info}下的{loc}元素找到了")
            return m
        except Exception as e:
            self.logger.info(f"{info}下的{loc}元素没找到，原因是{e}")
            raise

    # 显性等待
    def wait(self, loc, info, timeout=25):
        """
        显性等待，失败截图
        :param loc: 例子：(By.ID, "com.tal.kaoyan:id/tip_commit")
        :param info: 例子：功能模块，描述功能（红包页面）
        :param timeout: 最大显性等待时间，默认25秒
        :return: 无
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(loc))
        except:
            self.logger.info(f"{info}下的{loc}元素等待失败")
            # 失败截图
            self.screenshort(info)
            raise

    def click_element(self, loc, info, timeout=25):
        """
        点击，失败截图
        :param loc: 例子：(By.ID, "com.tal.kaoyan:id/tip_commit")
        :param info: 例子：功能模块，描述功能（红包页面）
        :param timeout: 最大显性等待时间，默认25秒
        :return: 无
        """
        try:
            self.wait(loc, info, timeout)
            self.get_element_object(loc, info).click()
            self.logger.info(f"{info}下的{loc}元素点击成功")
        except Exception as e:
            self.logger.info(f"{info}下的{loc}元素点击失败")
            # 失败截图
            self.screenshort(info)
            raise

    def input_element(self, msg, loc, info, timeout=25):
        """
        输入内容，失败截图
        :param msg: 输入的内容
        :param loc: 例子：(By.ID, "com.tal.kaoyan:id/tip_commit")
        :param info: 例子：功能模块，描述功能（红包页面）
        :param timeout: 最大显性等待时间，默认25秒
        :return: 无
        """
        try:
            self.wait(loc, info, timeout)
            self.get_element_object(loc, info).send_keys(msg)
            self.logger.info(f"{info}下的{loc}元素输入{msg}成功")
        except Exception as e:
            self.logger.info(f"{info}下的{loc}元素输入{msg}失败")
            # 失败截图
            self.screenshort(info)
            raise

    def get_element_text(self, loc, info, timeout=25):
        """
        获取文本，包括toast
        :param loc: 例子：(By.ID, "com.tal.kaoyan:id/tip_commit")
        :param info: 例子：功能模块，描述功能（红包页面）
        :param timeout: 最大显性等待时间，默认25秒
        :return: 无
        """
        try:
            self.wait(loc, info, timeout)
            t = self.get_element_object(loc, info).text
            self.logger.info(f"获取{info}下的{loc}元素文本  {t}成功")
            return t
        except Exception as e:
            self.logger.info(f"获取{info}下的{loc}元素文本失败")
            # 失败截图
            self.screenshort(info)
            raise

    def get_element_toast(self, loc, info, timeout=25):
        """
        获取文本，包括toast
        :param loc: 例子：(By.ID, "com.tal.kaoyan:id/tip_commit")
        :param info: 例子：功能模块，描述功能（红包页面）
        :param timeout: 最大显性等待时间，默认25秒
        :return: 无
        """
        try:
            # self.wait(loc, info, timeout)
            t = self.get_element_object(loc, info).text
            self.logger.info(f"获取{info}下的{loc}元素文本{t}点成功")
            return t
        except Exception as e:
            self.logger.info(f"获取{info}下的{loc}元素文本失败")
            # 失败截图
            self.screenshort(info)
            raise

    def screenshort(self, info):
        """
        截图和时间
        :param info: 例子：功能模块，描述功能（红包页面）
        :return: 无
        """
        self.driver.save_screenshot(AllPathSet.SCREENSHORT_Path(info))

    # 根据坐标点击
    def zuobiao(self, xz, yz):
        try:
            WebDriverWait(self.driver, 10).until(self.driver.tap(([(xz, yz)])))
        except:
            pass
