#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/13 11:44
# @Author : ZY
# @File : sengMail.py
# @Project : APP
import yagmail
from dataDriver.yamlData import readYaml


def send_mail():
    s = readYaml("seng.yml")

    yag = yagmail.SMTP(user=s['sendEmailUser'], host="smtp.163.com", password=s['sendPassword'])
    contents = []
    contents.extend(s['contents'])
    # contents.append(s['fileName'])
    # contents.append(yagmail.inline(s["attachment"]))
    yag.send(s['acceptEmailUser'], s['title'], contents)



send_mail()
