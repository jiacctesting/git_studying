import gettext

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import logging
import logging.config



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'HD1900'
desired_caps['platformVersion'] = '9'
desired_caps['appPackage'] = 'tv.danmaku.bili'
desired_caps['appActivity'] = '.MainActivityV2'
desired_caps['noRest'] = 'True'
desired_caps['unicodeKeyboard'] = 'True'#输入为中文时要有这个设置
desired_caps['restKeyboard'] = 'True'#输入为中文时要有这个设置
desired_caps['automationName'] = 'uiautomator2'#用来捕捉toast

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
el1 = driver.find_element(AppiumBy.ID,"tv.danmaku.bili:id/agree")
el1.click()
TouchAction(driver).press(x=415, y=146).move_to(x=480, y=146).release().perform()

TouchAction(driver).press(x=113, y=146).move_to(x=357, y=148).release().perform()

TouchAction(driver).press(x=411, y=146).move_to(x=494, y=144).release().perform()

el2 = driver.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[@content-desc=\"登录，按钮\"]/android.widget.FrameLayout/android.widget.ImageView")
el2.click()

# el1 = driver.find_element(AppiumBy.ID,"tv.danmaku.bili:id/button")
# el1.click()
# el2 = driver.find_element(AppiumBy.ID,"tv.danmaku.bili:id/phone_number")
# el2.send_keys("15911156312")
# el3 = driver.find_element(AppiumBy.ID,"tv.danmaku.bili:id/get_code")
# el3.click()
# el4 = driver.find_element(AppiumBy.ID,"tv.danmaku.bili:id/get_code")
# el4.click()
# el5 = driver.find_element(AppiumBy.ID,"tv.danmaku.bili:id/code")
# el5.send_keys("208497")
# el6 = driver.find_element(AppiumBy.ID,"tv.danmaku.bili:id/button_positive")
# el6.click()

# logging.basicConfig(level=logging.INFO,
#                     filename="run.log",format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,('textMatches("^同意.*")')).click()
# contexts=driver.contexts
# for i in contexts:
#     logging.info("contexts:"+ i) # 判断首页信息是否显示正常了
# m=[1,2,3,4]
# for j in m:
#     logging.debug("contexts:"+ str(j))
#
# WebDriverWait(driver,30).until(lambda x:x.find_element(AppiumBy.XPATH,'//*[@class="android.widget.ImageView" and @index=0]'))
#
# driver.find_element(AppiumBy.ID,"tv.danmaku.bili:id/search_text").click()
# x = driver.get_window_size()["width"]
# y = driver.get_window_size()["height"]
# logging.info("对屏幕操作")
# #对屏幕进行放大
# def zoom():
#     a1=TouchAction(driver)
#     a2=TouchAction(driver)
#     pinch_action=MultiAction(driver)
#
#
#     a1.press(x=x*0.2,y=y*0.2).wait(100).move_to(x=x*0.1,y=y*0.1).wait(100).release()
#     a2.press(x=x*0.4,y=y*0.4).wait(100).move_to(x=x*0.6,y=y*0.6).wait(100).release()
#     pinch_action.add(a1,a2)
#     pinch_action.perform()
# for i in range(2):
#     zoom()
#
#
#





# 定义获取手机屏幕的函数
# def get_screen_size():
#     x=driver.get_window_size()["width"]
#     y=driver.get_window_size()["height"]
#     return x,y
# l=get_screen_size()
# print(l)
# # TouchAction(driver).press(x=284,y=147).wait(1000).move_to(x=141,y=145).wait(1000).release().perform()
# TouchAction(driver).press(x=284,y=147).wait(1000).release().perform()


# #根据比例来调整滑动的位置
# def swipe_down():
#     l=get_screen_size()
#     x1=int(l[0]*0.5)
#     y1=int(l[1]*0.5)
#     x2=int(l[0]*0.5)
#     y2=int(l[1]*0.9)
#     driver.swipe(x1,y1,x2,y2,500)
#
# for i in range(2):
#     swipe_down()
#     sleep(2)







# driver.find_element(AppiumBy.XPATH,("//*[@class='android.widget.TextView' and @text='我的']")).click()
# contexts=driver.contexts
# print(contexts)
# driver.find_element(AppiumBy.XPATH,("//*[@class='android.widget.TextView' and @text='邀好友赚红包']")).click()
# print(driver.page_source)
#
# contexts=driver.contexts
# print(contexts)
# driver.switch_to.context(WEBVIEW_com.android.browser)
# WebDriverWait(driver,30).until_not(lambda x:x.find_element(AppiumBy.XPATH,('//*[@text="正在加载" and @index=1]')))
# WebDriverWait(driver,30).until_not(lambda x:x.find_element(AppiumBy.XPATH,('//*[@text="正在加载" and @index=1]')))
# driver.find_element(AppiumBy.XPATH,("//*[@class='android.widget.ImageButton' ]")).click()
# print(driver.page_source)

# sleep(2)

# print(driver.page_source)
# contexts=driver.contexts
# print(contexts)

# driver.save_screenshot("login.png")
# driver.get_screenshot_as_file("./image/loginerror.png")
# WebDriverWait(driver,30).until(lambda x:x.find_element(AppiumBy.XPATH,'//*[@class="android.widget.ImageView" and @index=0]'))
# driver.find_element(AppiumBy.XPATH,'//*[@class="android.widget.ImageView" and @index=0]').click()
# # print(driver.page_source)
# # WebDriverWait(driver,30).until_not(lambda x:x.find_element(AppiumBy.XPATH,'//*[@class="android.widget.ImageView" and @index=0]'))
# WebDriverWait(driver,30).until(lambda x:x.find_element(AppiumBy.XPATH,'//*[@class="android.widget.ImageView" and @index=0]'))
# # print(driver.page_source)
# WebDriverWait(driver,20).until_not(lambda x:x.find_element(AppiumBy.XPATH,('//*[@text="正在加载" and @index=1]')))
# # print(driver.page_source)
# driver.find_element(AppiumBy.XPATH,("//*[@text='请输入手机号码']")).send_keys('45445')
# print(driver.page_source)
# driver.find_element(AppiumBy.XPATH,("//*[@text='获取验证码']")).click()
# error_msg=driver.find_element(AppiumBy.XPATH,('//*[@text="手机号格式错误"]'))
# print(error_msg.text)
# phone_error_msg=WebDriverWait(driver,5).until(lambda x:x.find_element(AppiumBy.XPATH,('//*[@text="手机号格式错误"]')))
# print(phone_error_msg.text)











# WebDriverWait(driver,20).untilnot(lambda x:x.find_element(AppiumBy.XPATH,('//*[@class="android.widget.FrameLayout" and @index=0]')))
# print(driver.page_source)


# desired_caps = {
#   'platformName': 'Android', # 被测手机是安卓
#   'platformVersion': '9', # 手机安卓版本
#   'deviceName': 'emulator-5554', # 设备名，安卓手机可以随意填写
#   'appPackage': 'tv.danmaku.bili', # 启动APP Package名称
#   'appActivity': '.ui.splash.SplashActivity', # 启动Activity名称
#   'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
#   'resetKeyboard': True, # 执行完程序恢复原来输入法
#   'noReset': True,       # 不要重置App
#   'newCommandTimeout': 6000,
#   'automationName' : 'UiAutomator2'
#   # 'app': r'd:\apk\bili.apk',
# }



# driver.implicitly_wait(5)
# driver.find_element(by=By.ID,value="tv.danmaku.bili:id/agree").click()
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,('textMatches("^同意.*")')).click()
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,('resourceId("tv.danmaku.bili:id/agree")')).click()
# driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,('className("android.widget.TextView")'))[4].click()
# ele=driver.find_elements(AppiumBy.CLASS_NAME,"android.widget.TextView")
# # root_ele=driver.find_element(AppiumBy.ID,"tv.danmaku.bili:id/container")
# # a=root_ele.find_element(AppiumBy.CLASS_NAME,"android.widget.TextView")
#
# print(ele[4].text)
# ele[4].click()
# driver.implicitly_wait(30)

# driver.find_element(by=By.ID,value="tv.danmaku.bili:id/close").click()

# driver.find_element("By.id",'tv.danmaku.bili:id/agree').click()
# def check_cover_button():
#     try:
#         cover_button=driver.find_element(by=By.ID,value="tv.danmaku.bili:id/close")
#     except :
#         driver.implicitly_wait(5)
#
#         print('No cover button')
#     else:
#         driver.implicitly_wait(5)
#
#         cover_button.click()
# check_cover_button()
# ele_card=(AppiumBy.CLASS_NAME,'android.widget.ImageView')
# print('------------------------------')
# driver.find_element(AppiumBy.CLASS_NAME,'android.widget.ImageView').click()
# driver.implicitly_wait(30)
# WebDriverWait(driver,30).until(lambda x:x.find_element(AppiumBy.CLASS_NAME,'android.widget.TextView'))
# a=driver.find_elements(AppiumBy.CLASS_NAME,'android.widget.TextView')
# for i in a:
#     print(i.text)
# driver.find_element(AppiumBy.CLASS_NAME,'android.widget.TextView').click()
# driver.find_element(AppiumBy.CLASS_NAME,'android.widget.TextView').click()
# driver.find_element_by_id("tv.danmaku.bili:id/agree").click()

# driver.find_element(AppiumBy.ID,'tv.danmaku.bili:id/publish_remote_iv').click()
# driver.find_element(AppiumBy.ID,'tv.danmaku.bili:id/image').click()