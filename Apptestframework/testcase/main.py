#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/13 15:11
# @Author : ZY
# @File : main.py
# @Project : APP
import os
import pytest
import time
from common.timedDeleteOutput import TimedDeleteOutput

# 每三天清空output数据
TimedDeleteOutput().run()
# if __name__ == '__main__':
#
#     pytest.main()
#
#     # 生成allure报告
#     os.system('allure generate ../output/temp -o ../output/report --clean')


