import logging
import os.path
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
from common.desired_caps import appium_desired
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from businessView.baseView import BaseView
import csv



class Common_fun(BaseView):
    agree_button_ele = (AppiumBy.ID, "com.zhaopin.social:id/mAgreePrivacyUpdate")
    identity_ele = (AppiumBy.ID, "com.zhaopin.social:id/rl_click_c_identity")
    login_style_ele = (AppiumBy.ID, "com.zhaopin.social:id/tv_switch_over")

    def click_agree(self):
        logging.info("======click agree button=======")

        agree_button = self.driver.find_element(*self.agree_button_ele)
        agree_button.click()

    def click_c_identity(self):
        logging.info("========select identity========")
        identity_select = self.driver.find_element(*self.identity_ele)
        identity_select.click()

    def select_login_style(self):

        logging.info("=======select login style=======")
        login_select = self.driver.find_element(*self.login_style_ele)
        login_select.click()

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
        return self.driver.swipe(x1,y1,x2,y2,500)
    def swipe_down(self):
        logging.info("==========下滑===========")
        l=self.get_sereen_size()
        x1=int(l[0]*0.5)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.5)
        y2=int(l[0]*0.9)
        return self.driver.swipe(x1,y1,x2,y2,500)
    def swipe_left(self):
        logging.info("==========左滑===========")
        l=self.get_sereen_size()
        x1=int(l[0]*0.5)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.1)
        y2=int(l[0]*0.5)
        return self.driver.swipe(x1,y1,x2,y2,500)
    def swipe_right(self):
        logging.info("==========右滑===========")
        l=self.get_sereen_size()
        x1=int(l[0]*0.5)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.9)
        y2=int(l[0]*0.5)
        return self.driver.swipe(x1,y1,x2,y2,500)

    def gettime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getscreenshot(self,module):
        time=self.gettime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)
        logging.info('==========get %s screenshots==============' %(module))
        self.driver.get_screenshot_as_file(image_file)

    def get_csv_data(self,csv_file,line):
        logging.info("===========get csv data=========")
        with open(csv_file,encoding="utf-8-sig") as file:
            reader=csv.reader(file)
            for index,row in enumerate(reader,1):
                if index==line:
                    return row








if __name__=="__main__":
    # driver=appium_desired()
    # com=Common_fun(driver)
    # com.getscreenshot("打开APP")
    # com.click_agree()
    # com.click_c_identity()
    # com.getscreenshot("身份选择")
    # com.select_login_style()
    com=Common_fun(1)
    print(com.get_csv_data("../data/acc_pass.csv",3))









