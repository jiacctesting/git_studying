from appium.webdriver.common.appiumby import AppiumBy
from common_fun import Common
from baseView import BaseView
from appium_desired import appium_desired
from baseView import BaseView
import base64
import time
import os
import random
import sqlite3


from selenium import webdriver

import cv2 as cv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as WAIT
from selenium.webdriver.common.action_chains import ActionChains


class Login(Common):
    account_ele = (AppiumBy.ID, "com.zhaopin.social:id/et_account")
    password_ele = (AppiumBy.ID, "com.zhaopin.social:id/et_pwd")
    login_button_ele = (AppiumBy.ID, "com.zhaopin.social:id/btn_login")

    def login_fun(self, account, password):
        self.click_agree()
        self.click_c_identity()
        self.select_login_style()

        account_input = self.driver.find_element(*self.account_ele)
        password_input = self.driver.find_element(*self.password_ele)
        login_button = self.driver.find_element(*self.login_button_ele)
        account_input.send_keys(account)
        password_input.send_keys(password)
        login_button.click()
    def get_sereen_size(self):
        x=self.driver.get_window_size()["width"]
        y=self.driver.get_window_size()["height"]
        l=(x,y)
        return l

    def swipe_up(self):
        logging.info("==========上滑===========")
        l=self.get_sereen_size()
        x1=int(l[0]*0.5)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.5)
        y2=int(l[0]*0.1)




if __name__ == "__main__":
    driver = appium_desired()
    com = Login(driver)
    com.login_fun("15911156312", "YESUSHIZHU123")
    com.swipe_up()
    ele = (AppiumBy.ID, "android.widget.LinearLayout")





