# coding=UTF-8
"""
封装
"""
import time

# class Enemy:
#     def __init__(self, name, hp, atk):
#         self.name = name
#         self.hp = hp
#         self.atk = atk
#
#     @property
#     def hp(self):
#         return self.__hp
#
#     @hp.setter
#     def hp(self, value):
#         if 10 < value < 50:
#             self.__hp = value
#         else:
#             raise ValueError("hp值不对")
#
#
# enemy01 = Enemy("灭霸", 11, 100)
# print(enemy01.__dict__)
"""
体会封装思想：小明在招商银行取钱
"""

# class XM:
#     def __init__(self, name):
#         self.name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     def xm_quqian(self, money_value):
#         money_value.quqian()
#
#
# class QQ:
#     def quqian(money_value):
#         print("取钱", money_value)
#
#
# xm = XM("小明")
# qq = QQ.quqian(50)
#
# print(xm, qq)
"""
类的外部添加实例变量
"""
# class Student:
#     def __init__(self,name):
#         self.name=name
# s01=Student("wj")
# s01.nmae="无极"
# print(s01.__dict__)

"""
练习题
"""

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def teach(self, other, xingwei):
#         print(self.name, "教", other.name, xingwei)
#
#     def working(self, value):
#         print(self.name, "上班挣了", value)
# zwj=Person("张无忌")
# zm=Person("赵敏")
# zwj.teach(zm,"九阳神功")
# zm.teach(zwj,"化妆")
# zwj.working(1000)
# zm.working(100)
# class Player:
#     def __init__(self, name, hp, atk):
#         self.name = name
#         self.hp = hp
#         self.atk = atk
#
#     def attack(self, other):
#         # 玩家攻击
#         print("玩家攻击敌人")
#         print("玩家得分")
#         other.damage(50)
#
#     def damage(self, value):
#         # 玩家受伤
#         self.hp -= value
#         print("玩家掉血、碎屏")
#         if self.hp <= 0:
#             self.died()
#
#     def died(self):
#         print("游戏结束")
#
#
# class Enemy:
#     def __init__(self, name, hp, atk):
#         self.name = name
#         self.hp = hp
#         self.atk = atk
#
#     def damage(self, value):
#         self.hp -= value
#         print("敌人掉血")
#         if self.hp <= 0:
#             self.died()
#
#     def died(self):
#         print("敌人死亡")
#
#     def attack(self, other):
#         print("敌人攻击玩家")
#         print("玩家失分")
#         other.damage(20)
#
# play01=Player("玩家一号",100,200)
# enemy01=Enemy("敌人一号",100,200)
# play01.attack(enemy01)
# play01.attack(enemy01)
# enemy01.attack(play01)
# enemy01.attack(play01)
# enemy01.attack(play01)
# enemy01.attack(play01)
# enemy01.attack(play01)
"""
继承
"""
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def say(self):
#         print("叫")
# class Dog(Animal):
#     def __init__(self,name,run):
#         super().__init__(name)
#         self.run=run
#     def bite(self):
#         print("咬人")
# dog1=Dog("gou",10)
# dog1.say()
# class World:
#     def __init__(self,name):
#         self.name=name
#     def damage(self,aspect):
#         pass
# class Grenade:
#     def explorion_result(self,result):
#         print(result)
#
# class Person(World):
#     # def __init__(self,name):
#     #     super
#     def damage(self,aspect):
#         result="影响了",self.name,aspect
#         return result
#
# class Others(World):
#     def damage(self,aspect):
#         result = "影响了", self.name, aspect
#         return result
# a=Grenade()
# b=Person("玩家")
# a.explorion_result(b.damage("生命"))
# c=Others("房子")
# a.explorion_result(c.damage("炸毁"))
"""
工资管理
"""

# class Employee_Management:
#     def __init__(self):
#         self.emlpoyees=[]
#     def add_employee(self,value):
#         self.emlpoyees.append(value)
#     def show_salary(self):
#         for item in self.emlpoyees:
#             result=item.calculate_salary()
#             print(item,"工资是",result)

# class Employee:
#     def calculate_salary(self):
#         pass
#
# class Developer(Employee):
#     def __init__(self,basic_salary,bonus):
#         self.basic_salary=basic_salary
#         self.bonus=bonus
#     def calculate_salary(self):
#         salary=self.basic_salary+self.bonus
#         return salary
#
# dev01=Developer(1000,500)
# employees=Employee_Management()
# employees.add_employee(dev01)
# employees.show_salary()
"""
内置可重写函数
"""
# class Enemy:
#     def __init__(self, name, hp, atk):
#         self.name = name
#         self.hp = hp
#         self.atk = atk
#
#     def __str__(self):
#         return "敌人的名字是%s，血量是%d，攻击力是%d。" % (self.name, self.hp, self.atk)
#
#     def __repr__(self):
#         return "Enemy('%s', %d, %d)" % (self.name, self.hp, self.atk)
#         # return "Enemy(self.name, self.hp, self.atk)"
#
#
# e01 = Enemy("hh", 100, 50)
# # print(e01)
# e02 = eval(repr(e01))
# print(e02.name)


"""
运算符重载
"""
# class Vector1:
#     def __init__(self,i):
#         self.i=i
#     def __str__(self):
#         return str(self.i)
#     def __add__(self, other):
#         return Vector1(self.i+other)
#     def __sub__(self, other):
#         return Vector1(self.i-other)
# v1=Vector1(10)
# print(v1-1)

"""
游戏项目
"""
import time

# print(time.time())
# print(time.localtime())
# a=time.localtime()
# print(time.mktime(a))
# print(time.struct_time)
# class Show_Dayof_Week:
#     def __init__(self, str_date):
#         self.str_date = str_date
#
#     def show_turple_date(self):
#         re= time.strptime("self.str_date", "%y/%m/%d")
#         return re


# def show_day(self):
#     date = self.show_turple_date()
#     a = date[6]
#     print(self.str_date, "是这周的第%d天" %a)


# day01 = "2023年1月8日"


# struct_time = time.strptime("30 Nov 00", "%d %b %y")
# print ("returned tuple: %s " % struct_time)
# a="2023 Jan 1"
# re=time.strptime(a,"%y %m %d")
# print(re)

# a=time.time()
# print(a)
# print(time.localtime())
# a=time.localtime()
# b=time.strftime("%y-%m-%d",a)
# print(b)
# print(time.strptime(b,"%y-%m-%d"))
# print(time.strptime("23-01-08","%y-%m-%d"))
# def day_of_life(year,month,day):
#     now_time_stamp=time.time()
#     birthday_time_turple=time.strptime("%d-%d-%d"%(year,month,day),"%y-%m-%d")
#     birthday_time_stamp=time.mktime(birthday_time_turple)
#     result_rescond=now_time_stamp-birthday_time_stamp
#     return result_rescond/60/60/24/365
# a=day_of_life(93,8,4)
# print(a)
# class Atkerror(Exception):
#     def __init__(self,message,line,id):
#         self.message=message
#         self.line=line
#         self.id=id
#
# class Enemy:
#     def __init__(self,atk):
#         self.atk=atk
#
#     @property
#     def atk(self):
#         return self.__atk
#     @atk.setter
#     def atk(self,value):
#         if 0<value<100:
#             self.__atk=value
#         else:
#             raise Atkerror("攻击力不在范围内",313,1001)
# e01=Enemy(100)

# def get_Score():
#         while True:
#             try:
#                 str_value=input("请输入分数")
#                 value=int(str_value)
#
#             except ValueError:
#                 print("需要输入数字")
#                 continue
#             if 0<value<100:
#                 score=value
#                 return score
#             else:
#                 print("成绩不在范围内")
#
#
# re=get_Score()
# print("成绩是",re)
"""
获取成绩
"""
# def get_Score():
#     while True:
#         try:
#             str_value = input("请输入分数")
#             value = int(str_value)
#             if 0 < value < 100:
#                 score = value
#         finally:
#             print("出错也执行")
#
#
# re = get_Score()
# print("成绩是", re)
"""
迭代器原理
"""
# a=("铁扇公主","铁锤公主","牛魔王")
# iteration=a.__iter__()
# while True:
#     try:
#         item=iteration.__next__()
#         print(item)
#     except StopIteration:
#         break
# b={"铁扇公主a":101,"铁锤公主":102,"牛魔王":103}
# iteration=b.__iter__()
# while True:
#     try:
#         item=iteration.__next__()
#         print(item)
#     except StopIteration:
#         break
#
# iteration=b.values().__iter__()
# while True:
#     try:
#         item=iteration.__next__()
#         print(item)
#     except StopIteration:
#         break
"""
自己做迭代器
"""

# class Graphics:
#     def __init__(self,name):
#         self.name=name
#
#
# class GraphicManagement:
#     def __init__(self):
#         self.__graphics = []
#         self.__index = 0
#
#
#     def add_graphics(self, graphic):
#         self.__graphics.append(graphic)
#
#     def __iter__(self):
#         # return GraphicIterator(self.__graphics)
#         # if self.__index > len(self.__graphics) :
#         #         raise StopIteration
#         while self.__index < len(self.__graphics):
#             temp = self.__graphics[self.__index]
#             yield temp
#             self.__index += 1
#
#
#
# # class GraphicIterator:
# #     def __init__(self,target):
# #         self.__target = target
# #         self.__index = 0
# #
# #     def __next__(self):
# #         if self.__index > len(self.__target) - 1:
# #             raise StopIteration
# #         temp = self.__target[self.__index]
# #         self.__index += 1
# #         return temp
#
# management = GraphicManagement()
# management.add_graphics("三角形")
# management.add_graphics("长方形")
# management.add_graphics("圆形")

# for item in management:
#     print(item)
# iteration = management.__iter__()
# while True:
#     try:
#         item = iteration.__next__()
#         print(item)
#     except:
#         break
"""
定义MyRange类
"""


# class MyRange:
#     def __init__(self, value):
#         self.value = value
#
#     def __iter__(self):
#         return MyRangeIterator(self.value)
#
#
# class MyRangeIterator:
#     def __init__(self,target):
#         self.index = -1
#         self.target=target
#
#     def __next__(self):
#         while True:
#             self.index += 1
#             if self.index < self.target:
#                 re = self.index
#                 return re
#             else:
#                 continue
#
#
#
# a = MyRange(5)
# for item in a:
#     print(item)
# iterator = a.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#     except Exception:
#         break

# list01=[1,2,33,22,55,44,1222,48]
# for item in list01:
#     if item%2==0:
#         print(item)
# def get_evennumber(value):
#     index=0
#     while index<len(value):
#         if value[index]%2==0:
#             yield  value[index]
#             index+=1
#         else:
#             index+=1
#             continue
#
# a=get_evennumber(list01)
# for item in a:
#     print(item)


# def my_enumerate(value):
#     index=0
#     for index in range(len(value)):
#         yield (index,value[index])
#         index+=1
# list01=[1,4,2,7,9,22,0]
# a=my_enumerate(list01)
# print(a)
# for item in my_enumerate(list01):
#     print(item)


# def my_zip(value01,value02):
#     index=0
#     while True:
#         if index<len(value01) and index<len(value02):
#             yield value01[index],value02[index]
#             index+=1
# list01=["孙悟空","猪八戒"]
# list02=[1001,1002,1003]
# for a,b in my_zip(list01,list02):
#     print(a,b)
# list01=[1,2,7,4,9,22,56,3,456]
# def get_result():
#         for item in list01:
#             if item%2==0:
#                 yield item
# target=(item for item in list01 if item%2==0)
# for a in target:
#     print(a)
# print("--------")
# target=(item for item in list01 if item>10)
# for a in target:
#     print(a)

"""
listhelper功能
"""

class Listhelper:

    @staticmethod
    def get_all_result(target, condition):
        """
        通用的查找列表助手
        :param target: 需要查找的类
        :param condition: 需要查找的条件
        :return: 生成器类型，输出结果需要用for语句
        """
        for item in target:
            if condition(item):
                yield item

    @staticmethod
    def get_single_result(target, condition):
        """
                通用的查找列表助手
                :param target: 需要查找的类
                :param condition: 需要查找的条件
                :return: 直接返回需要查找的元素，输出结果直接用print
        """
        for item in target:
            if condition(item):
                return item

    @staticmethod
    def get_sum(target, condition):
        """
        求和
        :param target:
        :param condition:
        :return: 所求值的和
        """
        sum = 0
        for item in target:
            sum += condition(item)
        return sum

    @staticmethod
    def get_search_value(target, condition):
        """
                筛选某个属性的值
                :param target:目标列表
                :param condition:
                :return: 生成器格式，返回所求格式的数据
        """
        for item in target:
            yield condition(item)

    @staticmethod
    def get_search_max(target, condition):
        """
            获取最大值
                :param target:
                :param condition:
                :return: 生成器格式，返回所求格式的数据
        """
        max_value = target[0]
        for i in range(len(target)):
            if condition(max_value)< condition(target[i]):
                max_value = target[i]
        return max_value
    @staticmethod
    def order_by(target, condition):
        """
            升序排列
                :param target:目标列表
                :param condition:排列逻辑
                :return: 无需返回，列表已自动更新
        """
        for i in range(len(target)-1):
            for j in range(i+1,len(target)):
                if condition(target[i])> condition(target[j]):
                    target[i],target[j]=target[j],target[i]


class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def __str__(self):
        return "%s--%d--%d" % (self.name, self.hp, self.atk)


"""测试"""


def get_sum(target):
    sum = 0
    for item in target:
        sum += item.hp
    return sum


# a = Listhelper()
# list01 = [
#     Enemy("张无忌", 80, 1000),
#     Enemy("赵敏", 100, 900),
#     Enemy("周芷若", 50, 1500),
# ]
# # m=get_sum(list01)
# # print(m)
# result = a.get_all_result(list01, lambda item: item.hp > 0)
# list_result = list(result)
#
# for item in list_result:
#     print(item)
# print("---------")
# result = a.get_single_result(list01, lambda item: item.hp > 0)
# print(result)
# print("---------------")
# result = a.get_all_result(list01, lambda item: item.hp)
# list_result = list(result)
#
# for item in list_result:
#     print(item)
# print("---------------")
# m = a.get_sum(list01, lambda item: item.hp)
# print(m)
# m = a.get_search_value(list01, lambda item: (item.hp, item.atk))
# for item in m:
#     print(item)
# m = a.get_search_max(list01, lambda item: item.atk)
# print(m)
# print("---------------")
# m = a.order_by(list01, lambda a: a.atk)
#
# n=([1,1,1],[2,2],[3,3,3,3,])
# result=max(n,key=lambda item:len(item))
# print(result)
# class Enemy:
#     def __init__(self, name, hp, atk):
#         self.name = name
#         self.hp = hp
#         self.atk = atk
#
#     def __str__(self):
#         return "%s--%d--%d" % (self.name, self.hp, self.atk)
# list01 = [
#     Enemy("张无忌", 80, 1000),
#     Enemy("赵敏", 100, 900),
#     Enemy("周芷若", 50, 1500),
# ]
#
# result=filter(lambda item:(item.hp,item.name,item.atk), list01)
# for item in result:
#     print(item)
# result=map(lambda item:(item.hp,item.name,item.atk), list01)
# for item in result:
#     print(item)
# result=map(lambda item:(item.hp>0 and item.atk>90), list01)
# for item in result:
#     print(item)
#
# result=sorted(list01,key=lambda item:item.atk,reverse=True )
# for item in result:
#     print(item)
# def verify_account(func):
#     def wrapper(*args,**kwargs):
#         print("验证账号功能")
#         func(*args,**kwargs)
#     return wrapper
# @verify_account
# def deposit(money):
#     print("存%d钱"%money)
# @verify_account
# def withdraw(login,id):
#     print("取钱了",login,id)
#
# deposit(1000)
# withdraw("123","abc")
# a=[1,2,3,4]
# b=a[::-1]
# print(b)
# import random
# list01=[2,2,2,4]
# a=random.choice(list01)
# print(a)
a={}
a["m"]=1
print(a)
a=dict("abcd","hhhh")
print(a)