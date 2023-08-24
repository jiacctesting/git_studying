#encoding=utf-8
import logging
import time

from appium.webdriver.common.appiumby import AppiumBy
from common.common_fun import Common_fun
# from businessView.baseView import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException


class Login(Common_fun):
    account_ele = (AppiumBy.ID, "com.zhaopin.social:id/et_account")
    password_ele = (AppiumBy.ID, "com.zhaopin.social:id/et_pwd")
    login_button_ele = (AppiumBy.ID, "com.zhaopin.social:id/btn_login")
    dialog_consent = (AppiumBy.ID, "com.zhaopin.social:id/tv_privacy_policy_dialog_consent")

    # 设备权限申请：同意按钮
    tv_right = (AppiumBy.ID, "com.zhaopin.social:id/tv_right")


    rank_tab = (AppiumBy.ID, "com.zhaopin.social:id/rank_tab")

    # 我的tab 按钮
    tabLottieView = (AppiumBy.ID, "com.zhaopin.social:id/tabItemLayout")
    ic_settings = (AppiumBy.ID, "com.zhaopin.social:id/ic_settings")
    logout = (AppiumBy.ID, "com.zhaopin.social:id/button1")

    def login_fun(self, account, password):
        self.click_agree()
        self.click_c_identity()
        self.select_login_style()
        time.sleep(2)


        account_input = self.driver.find_element(*self.account_ele)
        password_input = self.driver.find_element(*self.password_ele)
        login_button = self.driver.find_element(*self.login_button_ele)
        account_input.send_keys(account)
        password_input.send_keys(password)
        login_button.click()
        try:
            self.click(*self.dialog_consent)
            self.click(*self.tv_right)
        except NoSuchElementException:
            logging.error("login failed")
            return False
        else:
            if self.check_login_status():
                return True
            else:
                return False

    def check_login_status(self):
        logging.info("====check login status======")
        try:
            # self.click(*self.tabLottieView)
            # self.click(*self.ic_settings)
            # self.click(*self.logout)
            self.click(*self.rank_tab)
        except NoSuchElementException:
            logging.error("login failed")
            self.getscreenshot("login failed")
            return False
        else:
            logging.info("login success")
            self.getscreenshot("login success")
            return True


if __name__ == "__main__":
    driver = appium_desired()
    com = Login(driver)
    com.login_fun("15911156312", "111155")
    
