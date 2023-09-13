import pytest

@pytest.fixture(autouse=True)
def login():
    print("=========login========")

@pytest.mark.run(order=6)
def test_func1():
    print("=====a=======")

@pytest.mark.run(order=1)
def test_func2():
    print("=====b=======")
import pytest


# class Test_Class3():
#     @pytest.mark.run(order=2)
#     def test_case1(self):
#         print("测试方法1")
#
#     @pytest.mark.run(order=1)
#     def test_case2(self):
#         print("测试方法2")
#
#     @pytest.mark.run(order=3)
#     def test_case3(self):
#         print("测试方法3")
#     @pytest.fixture(autouse=True)
#     def login(self):
#         print("=========login========")
#
#     @pytest.mark.run(order=6)
#     def test_func1(self):
#         print("=====a=======")
#
#     @pytest.mark.run(order=5)
#     def test_func2(self):
#         print("=====b=======")

if __name__ == '__main__':
    pytest.main(["-s","main.py"])