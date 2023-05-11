import logging.config
import time

import yaml
from appium import webdriver
import logging
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException



desired_caps={}
desired_caps["platformName"]="Android"
desired_caps["platformVersion"]=9
desired_caps["appPackage"]="com.zhaopin.social"
desired_caps["appActivity"]=".SplashActivity"
desired_caps["NoRest"]="True"
desired_caps["deviceName"]="emulator-5554"
desired_caps['automationName'] = 'UiAutomator2'
logging.info("=========打开APP==========")
driver=webdriver.Remote("http://www.localhost:4723/wd/hub",desired_caps)
driver.implicitly_wait(10)

agree_button_ele = (AppiumBy.ID, "com.zhaopin.social:id/mAgreePrivacyUpdate")
identity_ele = (AppiumBy.ID, "com.zhaopin.social:id/rl_click_c_identity")
login_style_ele = (AppiumBy.ID, "com.zhaopin.social:id/tv_switch_over")
driver.find_element(*agree_button_ele).click()
driver.find_element(*identity_ele).click()
driver.find_element(*login_style_ele).click()
time.sleep(2)

account_ele = (AppiumBy.ID, "com.zhaopin.social:id/et_account")
password_ele = (AppiumBy.ID, "com.zhaopin.social:id/et_pwd")
login_button_ele = (AppiumBy.ID, "com.zhaopin.social:id/btn_login")
account=driver.find_element(*account_ele)
account.send_keys("15911156312")
password=driver.find_element(*password_ele)
password.send_keys("YESUSHIZHU123")
#点击登录
driver.find_element(*login_button_ele).click()

dialog_consent = (AppiumBy.ID, "com.zhaopin.social:id/tv_privacy_policy_dialog_consent")
driver.find_element(*dialog_consent).click()
# 设备权限申请：同意按钮
tv_right = (AppiumBy.ID, "com.zhaopin.social:id/tv_right")
driver.find_element(*tv_right).click()


def get_sereen_size():
    x = driver.get_window_size()["width"]
    y = driver.get_window_size()["height"]
    l = (x, y)
    return l


def swipe_up():
    logging.info("==========上滑===========")
    l = get_sereen_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.5)
    y2 = int(l[0] * 0.1)
    # driver.swipe(x1)
    driver.swipe(x1, y1, x2, y2, 500)
try:
    element=WebDriverWait(driver,30).until(lambda x:x.find_elements(AppiumBy.CLASS_NAME,"android.widget.LinearLayout"))
    swipe_up()

    for item in driver.find_elements(AppiumBy.CLASS_NAME,"android.widget.LinearLayout"):
        item.click()
        driver.find_element(AppiumBy.ID,"com.zhaopin.social:id/tv_deliver_or_chat").click()
        driver.find_element(AppiumBy.ID,"com.zhaopin.social:id/iv_close").click()
        driver.find_element(AppiumBy.ID,"com.zhaopin.social:id/LeftButton_view").click()
except NoSuchElementException:
    swipe_up()
    pass

for i in range(30):
    try:
        element=WebDriverWait(driver,30).until(lambda x:x.find_elements(AppiumBy.CLASS_NAME,"android.widget.LinearLayout"))
        for item in driver.find_elements(AppiumBy.CLASS_NAME,"android.widget.LinearLayout"):
            item.click()
            driver.find_element(AppiumBy.ID,"com.zhaopin.social:id/tv_deliver_or_chat").click()
            driver.find_element(AppiumBy.ID,"com.zhaopin.social:id/iv_close").click()
            driver.find_element(AppiumBy.ID,"com.zhaopin.social:id/LeftButton_view").click()
    except NoSuchElementException:
        swipe_up()
        pass

