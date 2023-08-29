# try:
#
# except Exception as e:
#     print(e)
    # print(fd.read())

# fd=open("test.py","r")
# print(fd.read(3))
# print(fd.readline(6))
# print(fd.readlines(6))
import json
# f=open("test_0209.json",encoding="utf-8")
# print(f.read())
# result=json.load(f)
# print(result.get("name"))
# f.close()
# print(json.load(f).get("name"))
# my_list=[(1,2,3),("哈哈哈","好好好")]
# with open("test_0209.json","a+",encoding="utf-8") as b:
#     json.dump(my_list,b,ensure_ascii=False,indent=2)
# f = open("test_0623")

# try:
#     f=open("test_0623")
# except FileNotFoundError as e:
#     print(e)
# f=open("test_0209.json","a+",encoding="utf-8")
# l=["哈哈哈哈哈哈哈","哦哦哦哦哦哦","啊啊啊啊啊啊啊啊啊"]
# for item in l:
# #     f.write(item)
# #     f.write("\n")
# # f.writelines(l)
# class Person:
#     def __init__(self,name):
#         self.name=name
#
# class Student(Person):
#     def __init__(self,name):
#         super().__init__(name)
#
#     def speaking(self):
#         print("speaking")
#
# s01=Student("hhh")
# # print(s01.__dict__)
# # s01.speaking()
# """
# 装饰器
# """
# def verify_permission(fun):
#     def wrapper(*args,**kwargs):
#         print("权限验证")
#         fun(*args,**kwargs)
#     return wrapper
#
# @verify_permission
# def login(account):
#     print(account,"登陆啦")

# login(123)

from random import randint
# p=["偶数" if randint(10,100)%2==0 else "奇数" for _ in range(10)]
# print(p)
list=[]
for i in range(10):
    if randint(10,100)%2==0:
        list.append("偶数")
    else:
        list.append("奇数")
# print(list)
