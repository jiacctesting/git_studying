# import unittest
#
# class Test_assert(unittest.TestCase):
#     def test_01(self):
#         m=True
#         # self.assertEqual(m,True)
#         self.assertEqual(False,m,"login failed")
#
# if __name__ == "__main__":
#     unittest.main()

s = [1, 2, 3, 4, 5]
# 从指定索引1开始
for index, value in enumerate(s, 2):
    print('%s, %s' % (index, value))