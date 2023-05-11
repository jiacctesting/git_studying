from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from appium_desired import appium_desired
import logging
class BaseView:
    def __init__(self,driver_value):
        self.driver=driver_value

    def find_element(self, *args):

        return self.driver.find_element(*args)

    def find_elements(self, *args):

        return self.driver.find_elements(*args)

    def click(self):
        """
        点击元素
        :param selector: 元素，可以是元素对象、元素定位器，或者是元素文本
        """
        logging.info("click")
        return self.driver.click()

    # agree_button_ele = (AppiumBy.ID, "com.zhaopin.social:id/mAgreePrivacyUpdat")
    # identity_ele = (AppiumBy.ID, "com.zhaopin.social:id/rl_click_c_identity")
    # login_style_ele = (AppiumBy.ID, "com.zhaopin.social:id/tv_switch_over")
    #
    # def click_agree(self):
    #     # logging.info("======click agree button=======")
    #     agree_button = self.find_element(*self.agree_button_ele)
    #     agree_button.click()
if __name__=="__main__":
    driver=appium_desired()
    com=BaseView(driver)
    agree_button_ele = (AppiumBy.ID, "com.zhaopin.social:id/mAgreePrivacyUpdat")
    com.click(*agree_button_ele)
    def find_element(self, *args):
        try:
            element = WebDriverWait(self.driver, 20).until(lambda x:x.find_element(*args))
        except  NoSuchElementException:
            raise ValueError('找不到元素：')
        return element





