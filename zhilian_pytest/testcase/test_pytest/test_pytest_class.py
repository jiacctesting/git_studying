import pytest

class Test_Pytest:
    def setup_class(self):
        print("----setup_class----")

    def teardown_class(self):
        print("----teardown_class----")

    def test_a(self):
        print("-----test_a-----")
        assert 1==1

    def test_b(self):
        print("-----test_b-----")
        assert 0==1

if __name__ == '__main__':
    pytest.main(["-vs","test_pytest_class.py"])