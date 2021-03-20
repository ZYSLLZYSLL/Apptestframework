#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 15:23
# @Author : ZY
# @File : logHandler.py
# @Project : APP

import logging
from common.allPathSet import AllPathSet


class LogHandler():
    """
    日志，输出到文件，输出到控制台
    """
    # 日志存放路径
    filenamePath = AllPathSet.LOG_FILE_PATH
    # 创建一个logging对象，收集日志
    logger = logging.getLogger(__name__)
    # 设置日志等级
    logger.setLevel(level=logging.INFO)
    # 设置文件处理器
    __fhandler = logging.FileHandler(filename=filenamePath, encoding='utf-8')
    # 设置控制台处理器
    __shander = logging.StreamHandler()
    # 设置格式化
    # __format = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    __format = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    # 设置文件处理格式化
    __fhandler.setFormatter(__format)
    # 设置控制台处理格式化
    __shander.setFormatter(__format)
    # 添加处理器
    logger.addHandler(__fhandler)
    logger.addHandler(__shander)
