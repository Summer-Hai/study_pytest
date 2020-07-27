from appium import webdriver
device_caps={}
device_caps['platformName']='Android'
device_caps['platformVersion']='5.1.1'
device_caps['deviceName']='127.0.0.1:62001'
device_caps['appPackage']='io.appium.android.apis'
device_caps['appActivity']='.ApiDemos'
driver = webdriver.Remote('http://localhost:4723/wd/hub',device_caps)

