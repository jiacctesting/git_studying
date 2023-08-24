import logging.config
import yaml
from appium import webdriver
import logging
import sys

path = r"C:\Users\Lenovo\PycharmProjects\zhilian_appium"
sys.path.append(path)

CON_LOG = "../config/log.conf"
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

def appium_desired():
    with open("../config/zhilian_caps.yaml", "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    desired_caps = {}
    desired_caps["platformName"] = data["platformName"]
    desired_caps["platformVersion"] = data["platformVersion"]
    desired_caps["appPackage"] = data["appPackage"]
    desired_caps["appActivity"] = data["appActivity"]
    desired_caps["NoRest"] = data["NoRest"]
    desired_caps["deviceName"] = data["deviceName"]
    desired_caps["automationName"] = data["automationName"]

    logging.info("=========打开APP==========")
    # driver = webdriver.Remote("http://www.localhost:4723/wd/hub", desired_caps)
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    driver.implicitly_wait(10)
    return driver


if __name__ == "__main__":
    # dir=os.path.dirname(os.path.dirname(__file__))
    # print(dir)
    appium_desired()
