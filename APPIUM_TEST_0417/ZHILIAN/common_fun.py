import appium_desired
from baseView import BaseView
from appium_desired import appium_desired
import logging
from appium.webdriver import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class Common(BaseView):
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

if __name__ == "__main__":
    driver = appium_desired()
    com = Common(driver)
    com.click_agree()
    com.click_c_identity()
    com.select_login_style()
    # print(driver.page_source)
