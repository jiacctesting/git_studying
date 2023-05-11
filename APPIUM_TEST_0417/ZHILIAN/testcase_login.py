import unittest
from appium_desired import appium_desired
from login import Login
from time import sleep
import logging

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info("===========setup==========")
        self.driver=appium_desired()

    def tearDown(self):
        logging.info("===========teardown==========")
        sleep(2)
        self.driver.close_app()



class Test_login(StartEnd):
    def test_null(self):
        com=Login(self.driver)
        com.login_fun("","")

    def test_only_account(self):
        com = Login(self.driver)
        com.login_fun("1896789898", "")

if __name__=="__main__":
    unittest.main()
