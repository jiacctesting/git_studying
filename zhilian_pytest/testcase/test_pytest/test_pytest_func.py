import pytest

class Test_Pytest:
    def setup(self):
        print("----setup----")

    def teardown(self):
        print("----teardown----")

    @pytest.mark.flaky(reruns=3,reruns_delay=2)
    def test_a(self):
        print("-----test_a-----")
        assert 1

    @pytest.mark.flaky(reruns=3,reruns_delay=2)
    def test_b(self):
        print("-----test_b-----")
        assert 0

if __name__ == '__main__':
    pytest.main(["-s","test_pytest_func.py"])