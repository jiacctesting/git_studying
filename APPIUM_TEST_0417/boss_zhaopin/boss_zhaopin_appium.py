from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy

desired_caps={}
desired_caps["platformName"]="Android"
desired_caps["platformVersion"]="9"
desired_caps["appPackage"]="com.hpbr.bosszhipin"
desired_caps["appActivity"]=".module.launcher.WelcomeActivity"
desired_caps["NoRest"]="Android"
desired_caps["deviceName"]="HD1900"
desired_caps["automationName"]="UiAutomator2"

driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
driver.implicitly_wait(10)
#点击同意按钮
driver.find_element(AppiumBy.ID,"com.hpbr.bosszhipin:id/tv_positive").click()
#点击我要应聘
driver.find_element(AppiumBy.ID,"com.hpbr.bosszhipin:id/btn_enter_geek").click()
#输入账号
driver.find_element(AppiumBy.ID,"com.hpbr.bosszhipin:id/et_phone").send_keys("15911156312")
#点击下一步
driver.find_element(AppiumBy.ID,"com.hpbr.bosszhipin:id/btn_confirm").click()
#点击同意
driver.find_element(AppiumBy.ID,"com.hpbr.bosszhipin:id/tv_positive").click()

