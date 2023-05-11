​
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import base64
import time
import os
import random

from selenium import webdriver

import cv2 as cv
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as WAIT
from selenium.webdriver.common.action_chains import ActionChains

# 新建selenium浏览器对象，后面是geckodriver.exe下载后本地路径
from selenium.webdriver.common.by import By

browser = webdriver.ChromeOptions()

# 网站登陆页面
# 浏览器访问登录页面
class pagesign:
    driver = None

    def __init__(self, userName, password, pwd):
        if len(pwd) > 0:
            self.downloadpath = pwd

        download_dir = "f:"
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--safebrowsing-disable-download-protection') #关闭这种类型的文件可能会损害计算机…
        chrome_options.add_argument("--safebrowsing-disable-extension-blacklist")
        preferences = {"download.default_directory": download_dir,
                       "directory_upgrade": True,
                       "safebrowsing.enabled": True,
                       "download.prompt_for_download": False}
        chrome_options.add_experimental_option("prefs", preferences)

        self.driver = webdriver.Chrome(options=chrome_options, executable_path=r'chromedriver')

        self.driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': self.downloadpath}}
        command_result = self.driver.execute("send_command", params)

        self.driver.implicitly_wait(10)
        self.driver.get(self.paxurl)

        self.driver.find_element(By.ID, "userName").send_keys(userName)
        self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[2]/div/form/div[3]/div/div[1]/input").send_keys(
            password)

        self.wait = WAIT(self.driver, 5)

        if self.slide_verify():
            print('登陆成功')
            #self.save_cookie()
            #self.driver.close()
            self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[2]/div/form/div[5]/div/button").click()
        else:
            print('第1次登陆失败')
            for i in range(4):
                print('正在尝试第%d次登陆' % (i + 2))
                if self.slide_verify():
                    print('第%d次登陆成功' % (i + 2))
                    #self.save_cookie()
                    #self.driver.close()
                    self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[2]/div/form/div[5]/div/button").click()
                    return
                print('第%d次登陆失败' % (i + 2))
            print('登陆失败5次，停止登陆')
           # self.driver.close()

    def slide_verify(self):
        '''滑动验证'''
        js = f'''return document.getElementsByTagName("canvas")[{0}].toDataURL("image/png");'''
        base64str = self.driver.execute_script(js)
        page = base64str.split(',')[1]
        imagedata = base64.b64decode(page)

        with open(self.downloadpath + '\\' + "slider.png", "wb") as f:
            f.write(imagedata)

        js = f'''return document.getElementsByTagName("canvas")[{1}].toDataURL("image/png");'''
        base64str = self.driver.execute_script(js)
        page = base64str.split(',')[1]
        imagedata = base64.b64decode(page)

        with open(self.downloadpath + '\\' + "bg.png", "wb") as f:
            f.write(imagedata)

        slider_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="sliderMask"]')))

        distance = self.get_distance(self.downloadpath + '\\' + "slider.png", self.downloadpath + '\\' + "bg.png")
        print("distance=" + str(distance))
        tracks = self.get_tracks(distance)
        self.mouse_move(slider_button, tracks)
        try:
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="sliderContainer sliderContainer_success"]')))
        except:
            return False
        else:
            return True


    def mouse_move(self, slide, tracks):
        '''鼠标滑动'''

        # 鼠标点击滑块并按照不放
        ActionChains(self.driver).click_and_hold(slide).perform()
        # 按照轨迹进行滑动，
        for track in tracks:
            ActionChains(self.driver).move_by_offset(track, 0).perform()
        print("time sleep 1")
        time.sleep(0.5)
        print("after time sleep 1")
        ActionChains(self.driver).release().perform()
        print("mouse release")
        time.sleep(3)
        print("after sleep")
        return


    def get_distance(self, slider_img_path, bg_img_path):
        """获取滑块移动距离"""

        # 背景图片处理
        bg_img = cv.imread(bg_img_path, 0)  # 读入灰度图片
        bg_img = cv.GaussianBlur(bg_img, (5, 5), 0)  # 高斯模糊去噪
        bg_img = cv.Canny(bg_img, 100, 200)  # Canny算法进行边缘检测
        #cv.imshow('canny', bg_img)
        # 滑块做同样处理
        slider_img = cv.imread(slider_img_path, 0)
        slider_img = cv.GaussianBlur(slider_img, (5, 5), 0)
        slider_img = cv.Canny(slider_img, 100, 200)
        #cv.imshow('slider', slider_img)
        # 寻找最佳匹配
        res = cv.matchTemplate(bg_img, slider_img, cv.TM_CCOEFF_NORMED)

        # 最小值，最大值，并得到最小值, 最大值的索引
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        # 例如：(-0.05772797390818596, 0.30968162417411804, (0, 0), (196, 1))
        top_left = max_loc[0]  # 横坐标
        print("min_loc=", min_loc[0])
        print("max_loc=", max_loc[0])

        len = min_loc[0] + (max_loc[0]-min_loc[0])/2
        return len


    def get_tracks(self, distance):
        '''滑动轨迹 '''
        tracks = []
        v = 0
        t = 0.2  # 单位时间
        current = 0  # 滑块当前位移
        while current < distance:
            a = random.randint(1, 3)
            v0 = v  # 初速度
            track = v0 * t + 0.5 * a * (t ** 2)  # 单位时间（0.2s）的滑动距离
            tracks.append(round(track))  # 加入轨迹
            current += round(track)
            v = v0 + a * t
        return tracks


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = os.getcwd()
    sign = pagesign("1234", "gewrwfas", path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

​
