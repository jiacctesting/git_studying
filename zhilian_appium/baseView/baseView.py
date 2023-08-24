import logging
import os.path
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from common.desired_caps import appium_desired
from appium.webdriver.common.touch_action import TouchAction
from time import sleep



class BaseView:
    def __init__(self,driver_value):
        self.driver=driver_value

    def find_element(self, *args):
        try:
            element = WebDriverWait(self.driver, 20).until(lambda x:x.find_element(*args))
        except  NoSuchElementException:
            raise ValueError('找不到元素：')
        return element

    def click(self, *element_value):
        """
        点击元素
        :param selector: 元素，可以是元素对象、元素定位器，或者是元素文本
        """
        element=self.find_element(*element_value)
        element.click()





if __name__=="__main__":
    driver=appium_desired()
    com=BaseView(driver)






