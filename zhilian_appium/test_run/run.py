import sys
from BSTestRunner import BSTestRunner
import unittest
import time, logging

path = r"C:\Users\Lenovo\PycharmProjects\zhilian_appium"
sys.path.append(path)


# import sys
# import os
# curPath=os.path.abspath(os.path.dirname(__file__))
# rootPath=os.path.split(curPath)[0]
# sys.path.append(rootPath)


test_dir = '../test_case'
report_dir = '../reports'

discover = unittest.defaultTestLoader.discover(test_dir, pattern="testcase_login.py")

now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir + "/ " + now + " test report.html"
with open(report_name, "wb") as f:
    runner = BSTestRunner(stream=f, title="zhilian report", description="ZHILIAN")
    logging.info("start run test case")
    runner.run(discover)
