import logging
import time
import unittest
from common.desired_caps import appium_desired


# from common.common_fun import Common_fun

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info("======start up=======")
        self.driver = appium_desired()

    def tearDown(self):
        logging.info("======tear down=======")
        time.sleep(3)
        self.driver.close_app()
