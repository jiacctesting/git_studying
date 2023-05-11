import yaml
from appium import webdriver

file_name=open("desired_caps.yaml","r")
# data=yaml.load(file_name,Loader=yaml.FullLoader)
data=yaml.load(file_name,Loader=yaml.CLoader)
# data=yaml.safe_load(file_name)
# print(data["platformName"])
# print(data["children"])
desired_caps={}
desired_caps["platformName"]=data["platformName"]
desired_caps["deviceName"]=data["deviceName"]
desired_caps["platformVersion"]=data["platformVersion"]
desired_caps["appPackage"]=data["appPackage"]
desired_caps["appActivity"]=data["appActivity"]
desired_caps["noRest"]=data["noRest"]

# driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
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

desired_caps_yaml=yaml.dump(desired_caps)
print(desired_caps_yaml)