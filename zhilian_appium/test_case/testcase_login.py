import unittest
# from common.common_fun import Common_fun
from businessView.login import Login
from common.myunit import StartEnd
import logging
from common.desired_caps import appium_desired


class Login_Review(StartEnd):

    @unittest.skip("test")
    def test_wrong_acc(self):
        logging.info("test_wrong_acc")
        login_test = Login(self.driver)
        username = login_test.get_csv_data("../data/acc_pass.csv", 1)[0]
        password = login_test.get_csv_data("../data/acc_pass.csv", 1)[1]
        login_test.login_fun(username, password)
        self.assertTrue(login_test.login_fun(username, password))

    @unittest.skip("correct")
    def test_correct_acc(self):
        logging.info("test_correct_acc")
        login_test = Login(self.driver)
        username = login_test.get_csv_data("../data/acc_pass.csv", 2)[0]
        password = login_test.get_csv_data("../data/acc_pass.csv", 2)[1]
        self.assertTrue(login_test.login_fun(username, password))

    def test_correct_account(self):
        logging.info("test_correct_acc")
        # login_test = Login(appium_desired())
        login_test = Login(self.driver)
        username = login_test.get_csv_data("../data/acc_pass.csv", 2)[0]
        password = login_test.get_csv_data("../data/acc_pass.csv", 2)[1]
        m=login_test.login_fun(username, password)
        self.assertTrue(m.equals("True"))



if __name__ == "__main__":
    unittest.main()
