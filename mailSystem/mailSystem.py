# -*- coding: utf-8 -*-
# @Python Version : Python3.6.5 x86_64
# @CreateTime     : 2021/6/11  14:20
# @Author         : liyc@hsmap.cn
# @File           : mailSystem.py
# @Software       : PyCharm 2019.3
# @UpdateTime     : 
# @Describe       : 邮件通知模块封装

import json
import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr


class MailSystem(object):
    def __init__(self, platform="TencentMailEnterprise"):
        self.SYSTEM_STATUS = False
        self.lam_format_addr = lambda name, addr: formataddr((Header(name, 'utf-8').encode(), addr))
        self.platform = platform
        self.readConfig()
        self.connectSMTP()

    def readConfig(self):
        configPath = "./mailSystem/my.config"
        if not os.path.exists(configPath):
            return False
        f = open(configPath, "r")
        config = json.load(f)
        self.account = config.get(self.platform, {}).get("mailAccount", None)
        self.password = config.get(self.platform, {}).get("password", None)
        self.smtp_server = config.get(self.platform, {}).get("smtp_server", None)
        self.port = config.get(self.platform, {}).get("port", None)
        if self.password and self.account:
            print(">>>>>>>>MAIL SYSTEM INITIAL SUCCESS<<<<<<<<")
            self.SYSTEM_STATUS = True
        else:
            print(">>>>>>>>MAIL SYSTEM INITIAL FAILED<<<<<<<<")

    def connectSMTP(self):
        if not self.SYSTEM_STATUS:
            return None
        try:
            self.server = smtplib.SMTP_SSL(self.smtp_server, self.port)
            self.server.login(self.account, self.password)
            # self.server.set_debuglevel(1)  # DEBUG开关
            print(">>>>>>>>SMTP SEVER CONNECT SUCCESS<<<<<<<<")
        except:
            print(">>>>>>>>SMTP SEVER CONNECT FAILED<<<<<<<<")
            self.SYSTEM_STATUS = False

    def createMail(self, title, content):
        self.msg = MIMEText(content, 'html', 'utf-8')
        self.msg['Subject'] = Header(title, 'utf-8').encode()

    def addSendInfo(self, yourName, recipientName, recipientAddress):
        self.recipientAddress = recipientAddress
        self.msg['From'] = self.lam_format_addr(yourName, self.account)
        self.msg['To'] = self.lam_format_addr(recipientName, recipientAddress)

    def sendMail(self):
        try:
            self.server.sendmail(self.account, [self.recipientAddress], self.msg.as_string())
            print(f">>>>>>>>SEND MAIL TO {self.recipientAddress} SUCCESS<<<<<<<<")
        except:
            print(">>>>>>>>SEND MAIL FAILED<<<<<<<<")

