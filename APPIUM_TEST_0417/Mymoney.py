from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

# from appium.common.exceptions import

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['appPackage'] = 'com.mymoney'
desired_caps['appActivity'] = '.biz.splash.SplashScreenActivity'
desired_caps['noRest'] = 'True'
desired_caps["automationName"] = "UiAutomator2"

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
driver.implicitly_wait(5)

driver.find_element(AppiumBy.XPATH, ('//*[@text="同意"]')).click()
print("找元素")
contexts = driver.contexts
print(contexts)
print(driver.page_source)
# WebDriverWait(driver,5).until(lambda x:x.find_element(AppiumBy.XPATH,('//*[@text="初始化中..." and @index="1"]')))
# WebDriverWait(driver,2).until(lambda x:x.find_element(AppiumBy.XPATH,('//*[@text="欢迎你"]')))
# print(driver.page_source)

# TouchAction(driver).press(x=263,y=545).wait(1000).move_to(x=538,y=547).wait(1000)\
#         .move_to(x=843,y=881).wait(1000)\
#         .move_to(x=821,y=1157).wait(1000)\
#         .release().perform()


WebDriverWait(driver, 15).until(lambda x: x.find_element(AppiumBy.XPATH, ("//*[@text='选账本']")))
# print(driver.page_source)
# WebDriverWait(driver,5).until(lambda x:x.find_element(AppiumBy.ID,"com.mymoney:id/select_template_btn"))
# print("找到了")
# sleep(5)
driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button").click()
# sleep(1000)
driver.find_element(AppiumBy.XPATH, ("//*[@text='跳过']")).click()
# sleep(1000)

# WebDriverWait(driver,8).until(lambda x:x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'textContains("标准账本")'))
def get_screen_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()["height"]
    return x, y


l = get_screen_size()
print(l)
WebDriverWait(driver,20).until_not(lambda x:x.find_element(AppiumBy.XPATH, ('//*[@text="创建中"]')))

# TouchAction(driver).press(x=900, y=900).wait(100).release().perform()
driver.find_element(AppiumBy.XPATH, ('//*[@text="我的"]')).click()

def swipe_up():
    l=get_screen_size()
    x1=int(l[0]*0.1)
    y1=int(l[1]*0.9)
    x2=int(l[0]*0.1)
    y2=int(l[1]*0.1)
    driver.swipe(x1,y1,x2,y2)

for i in range(2):
    swipe_up()
    sleep(1)

driver.find_element(AppiumBy.XPATH, ('//*[@text="设置"]')).click()
driver.find_element(AppiumBy.XPATH, ('//*[@text="密码保护"]')).click()
print("进入密码保护选择页面")
sleep(2)
driver.find_element(AppiumBy.XPATH, ('//*[@class="android.widget.Switch"]')).click()
# driver.find_element(AppiumBy.ID,"com.mymoney:id/right_switch").click()

driver.find_element(AppiumBy.XPATH, ('//*[@text="手势密码"]')).click()


for i in range(2):
    TouchAction(driver).perform().press(x=263,y=545).wait(1000).move_to(x=538,y=547).wait(1000)\
        .move_to(x=843,y=881).wait(1000)\
        .move_to(x=821,y=1157).wait(1000)\
        .release().perform()
#     sleep(2000)


