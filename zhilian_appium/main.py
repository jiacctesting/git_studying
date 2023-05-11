import gettext

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import logging
import logging.config
from selenium.webdriver.support import expected_conditions as EC




desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '9', # 手机安卓版本
  'deviceName': 'emulator-5554', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.zhaopin.social', # 启动APP Package名称
  'appActivity': '.SplashActivity', # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
  # 'app': r'd:\apk\bili.apk',
}


class BaseView:
    def __init__(self,driver_value):
        self.driver=driver_value

    def find_element(self,*args):

        try:
            print("==========")
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(*args))
        except :
            raise ValueError('找不到元素：')
        return element




