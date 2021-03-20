#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/13 13:57
# @Author : ZY
# @File : yamlData.py
# @Project : APP
import yaml


# 读
def readYaml(path):
    # "desired_capabilities.yml"
    with open(path, "r", encoding='utf-8') as f:
        return yaml.load(f, Loader=yaml.FullLoader)

# 写
def writeYaml(path, content):
    with open(path, 'w', encoding="utf-8") as f:
        yaml.dump(content, f, allow_unicode=True)

