from selenium import webdriver
from selenium.webdriver.common.by import By

wd=webdriver.Chrome
wd.get("https:www.baidu.com")

element=wd.find_element(By.ID,"kw")
element.send_keys("测试\n")