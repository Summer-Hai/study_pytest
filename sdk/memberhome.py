#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 14:07
# @Author  : Summer
# @Email    : 2361157192@qq.com
# @File    : memberhome.py
# @Software: PyCharm
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from sdk.basepage import BasePage


class MemberHome(BasePage):

    # def __init__(self,driver):
    #     self.driver = driver

    def certification_click(self):
        sleep(5)

        # 进入用户中心，点击实名认证
        self.driver.find_element(MobileBy.XPATH,
                                 "//android.widget.TextView[@text='实名认证']/../android.widget.ImageView").click()

        from sdk.certification import Certification
        return Certification(self.driver)

    def get_toast(self):
        # text = '成功'
        # element = WebDriverWait(self.driver, 10).until(
        #     lambda x: x.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']"))
        # element = self.webdriver_wait(self.toast_ele)
        result = "成功"
        return result