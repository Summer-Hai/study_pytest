from appium import webdriver
from appium.webdriver.webdriver import WebDriver

class Base():

    _driver = None

    def __init__(self,driver:WebDriver):

        if self._driver == None:
            caps = {}
            caps["platformName"] = "Android"
            # caps["platformVersion"] = "5.1.1"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.xueqiu.android"
            # caps["chromedriverExecutable"] = "E:/test/driver/chromedriver.exe"
            caps["appActivity"] = ".login.controller.LoginWxAuthActivity"
            caps['noReset'] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(10)

        else:
            self._driver = driver