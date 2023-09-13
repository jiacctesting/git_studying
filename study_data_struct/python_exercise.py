# file_input=input("input file location:")
# f=open(file_input,"rb")
# f_new=open("file_copy","wb")
# for line in f:
#     f_new.write(line)
    # if not line:
    #     break
# f=open("test_0607.py","rb")
# f.read()
# print(f.readline(50))
# print(f.readline(50))
# print(f.readline())
# print(f.readlines())
# f.readline()
# import datetime
# f=open("test_0607.py","r+")
# print(f.fileno())
# f.close()
# f=open("test_0607.py","r+")
# print(f.fileno())
#
# f.read(5)
# print(f.tell())
# f.seek(3,0)
# print(f.tell())
# while True:
#     f.write(datetime.time.strftime())
#
# f.close()
# import time
# print(time.ctime())

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def print_stu_info(self):
        print("学生姓名是：%s，年龄是%s" %(self.name,self.age))

stu_list=[
    Student("明玉", 30),
    Student("苏大强",55),
    Student("明成",33)
]
def find04():
    max_age=0
    stu_max=0
    for stu in stu_list:
        if stu.age>max_age:
            max_age=stu.age
            stu_max=stu
    return stu_max
# re=find04()
# re.print_stu_info()
# def find03():
#     count=0
#     for stu in stu_list:
#         if True:
#             stu.age=0
# find03()
# for item in stu_list:
#     item.print_stu_info()
# def find03():
#     count=0
#     for stu in stu_list:
#         if stu.age>=33:
#             count+=1
#     return count
# re=find03()
# print(re)
# def find_name():
#     for stu in stu_list:
#         if stu.name=="苏大强":
#             stu.print_stu_info()
# find_name()
# stu_30=[]
# def find02():
#     for stu in stu_list:
#         if stu.age==30:
#             stu_30.append(stu)
# find02()
# for item in stu_30:
#     print(item.name)
# while True:
#     name=input("请输入学生姓名：")
#     if not name:
#         break
#     age=input("请输入年龄：")
#     stu=Student(name,age)
#     stu_list.append(stu)
# for stu in stu_list:
#     stu.print_stu_info()
# print("第一个学生信息是：")
# stu_list[0].print_stu_info()
"""
类变量
静态方法
"""
# class Student:
#     count=0
#     def __init__(self,name):
#         self.name=name
#         Student.count+=1
#     @classmethod
#     def count_times(cls):
#         return cls.count
#
# Student("yi")
# Student("er")
# re=Student.count_times()
# print(re)



"""
封装属性

"""
# class Student:
#     __slots__ = ("name","__age")
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def get_age(self):
#         return self.__age
#     def set_age(self,value):
#         self.__age=value
#     age=property(get_age,set_age)
#
# s01=Student("学生1",10)
# s01.age=20
# # print(s01.__dict__)
# print(s01.age)



# class Student:
#     # __slots__ = ("name","__age")
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#     @property
#     def age(self):
#         return self.__age
#     # def set_age(self,value):
#     #     self.__age=value
#     # age=property(get_age,set_age)
#
# s01=Student("学生1",10)
# # s01.age=20
# print(s01.__dict__)
# print(s01.age)


"""
练习：
玩家(攻击力)攻击敌人（血量），敌人受伤掉血，还可能死亡（掉装备。加分）
敌人(攻击力)攻击玩家（血量），玩家受伤掉血碎屏，还可能死亡（游戏结束）
"""
# class Player:
#     def __init__(self,hp,atk):
#         self.hp=hp
#         self.atk=atk
#
#     def attack(self,other):
#         """
#         :param other: 传入敌人对象
#         """
#         print("玩家攻击敌人")
#         other.damage(self)
#
#     def damage(self,other):
#         print("玩家受伤掉血碎屏")
#         self.hp-=other.atk
#         if self.hp==0:
#             self.__death()
#
#     def __death(self):
#         print("玩家死亡")
#         print("游戏结束")
#
#
# class Enemy:
#     def __init__(self,hp,atk):
#         self.hp=hp
#         self.atk=atk
#     def damage(self,other):
#         """
#         :param value: 传入玩家对象
#         """
#         print("敌人受伤")
#         self.hp-=other.atk
#         if self.hp==0:
#             self.__death()
#
#     def __death(self):
#         print("敌人死亡")
#         print("敌人掉装备")
#         print("玩家加分")
#
#     def attack(self,other):
#         print("敌人打玩家")
#         self.hp-=other.atk
#         other.damage(self)
#
# p01=Player(50,20)
# e01=Enemy(60,25)
# # p01.attack(e01)
# # p01.attack(e01)
# # p01.attack(e01)
# e01.attack(p01)
# e01.attack(p01)
# # e01.attack(p01)

""""
类成员
实例、类、静态
"""
# class Bank:
#     count=0
#     def __init__(self,name):
#         self.name=name
#         Bank.count+=1
#
#     @classmethod
#     def count_sum(cls):
#         print(Bank.count)
#
# b01=Bank("1")
# b02=Bank("2")
# print(Bank.count)
# Bank.count_sum()

"""
学生管理系统
"""
class StudentModel:
    # id=1  设置上类变量会导致只要创建学生就增加id值，但是可能是不同的类调用，并不是所有的类都需要按照同一个顺序增加id值
    def __init__(self,name="",age=0,score=0,id=0):#设置上默认值，之后创建可以不填某个字段的信息
        self.id=id
        self.name=name
        self.age=age
        self.score=score

class StudentManagerController:
    """
    学生管理控制器
    """
    __id=100
    def __init__(self):
        self.__stu_list=[]


    # def get_stu_list(self):
    #     return self.__stu_list  写成属性更好，可以直接调用属性而不是方法
    @property
    def stu_list(self):
        """
        学生属性
        """
        return self.__stu_list

    def add_student(self,stu_info):
        """
        添加学生
        :param stu_info: 学生信息，不需要填写id值,填写也不影响
        """
        stu_info.id =self.__generate_id()
        self.__stu_list.append(stu_info)

    def __generate_id(self):
        """
        id生成器，每次id值增加1
        :return:
        """
        StudentManagerController.__id += 1
        return StudentManagerController.__id
    def remove_student(self,id):
        """
        根据id值删除学生
        :param id:
        """
        for item in self.__stu_list:
            if item.id==id:
                self.__stu_list.remove(item)
                return True#给外界一个反应
        return False

    def update_student(self, stu_info):
        """
        根据id值修改学生信息
        :param id:
        """
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name=stu_info.name
                item.age=stu_info.age
                item.score=stu_info.score
                return True  # 给外界一个反应
        return False
class StudentManagerView:
    def __init__(self):
        self.__manager=StudentManagerController()
    def __display_menu(self):
        print("1)添加学生信息")
        print("2)显示学生信息")
        print("3)删除学生信息")
        print("4)修改学生信息")
        print("5)按照成绩显示学生信息")
    def __select_menu_item(self):
        item=int(input("请选择"))
        if item==1:
            self.__input_students()
        elif item==2:
            self.__output_students(self.__manager.stu_list)
        elif item==3:
            self.__delete_student()
        elif item==4:
            self.__modify_student()
        else:
            pass
    def __input_students(self):
        name=input("请输入学生姓名")
        age=int(input("请输入学生年龄"))
        score=int(input("请输入学生分数"))
        stu=StudentModel(name,age,score)
        self.__manager.add_student(stu)
    def __output_students(self,list_output):
        for item in list_output:
            print("学生信息如下",item.id,item.name,item.age,item.score)
    def __delete_student(self):
        id=int(input("请输入要删除的学生id"))
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")
    def __modify_student(self):
        stu=StudentModel()
        stu.id=int(input("请输入需要修改的id"))
        stu.name=input("请输入需要修改的name")
        stu.age=int(input("请输入需要修改的age"))
        stu.score=int(input("请输入需要修改的score"))

        self.__manager.update_student(stu)

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu_item()

# s_management=StudentManagerView()
# s_management.main()
# s01=StudentModel("xuesheng1",5,100,1)
# s02=StudentModel("xuesheng2",5,100)
# s03=StudentModel("xuesheng3",5,100)
# StudentModel()
# s_set=StudentManagerController()
# s_set.add_student(s01)
# s_set.add_student(s02)
# s_set.add_student(s03)
# for item in  s_set.stu_list:#调用的是属性，不需要加括号
#     print(item.name,item.id)
# # s_set.remove_student(102)
# s_set.update_student(s03)
# for item in  s_set.stu_list:#调用的是属性，不需要加括号
#     print(item.name,item.id)
"""
继承
"""
class Animal:
    def shout(self):
        print("shout")
class Bird(Animal):
    def fly(self):
        print("fly")
class Dog(Animal):
    def run(self):
        print("run")
# b01=Bird()
# a01=Animal()
# print(isinstance(b01 ,Animal))
# print(issubclass(Bird ,Animal))
class Car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed

class ElectricCar(Car):
    def __init__(self,brand,speed,battery_capacity,charging_power):
        super().__init__(brand,speed)
        self.battery_capacity=battery_capacity
        self.charging_power=charging_power
e01=ElectricCar(1,2,3,4)
# print(e01.brand)
"""
体会封装继承多态
"""
class GraphMangement:
    def __init__(self):
        self.list=[]
    def add_graph(self,graph):
        self.list.append(graph)
    def calculate_area(self):
        for item in self.list:
            if not isinstance(item,Area):
                raise ValueError

            area=item.area_method()
            print("面积是%d"%area)
class Area:
    def area_method(self,*args):
        raise ValueError

class Square(Area):
    def __init__(self,length):
        self.length=length
    def area_method(self):
        area=self.length**2
        return area

class Rectangle(Area):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area_method(self):
        area=self.length*self.width
        return area
# m=GraphMangement()
# s01=Square(5)
# r01=Rectangle(10,6)
# m.add_graph(s01)
# m.add_graph(r01)
# m.calculate_area()

"""
内置可重写函数
"""
class Enemy:
    def __init__(self,hp,atk):
        self.hp=hp
        self.atk=atk
    def __str__(self):
        return "敌人的血量是%d,攻击力是%d"%(self.hp,self.atk)
    def __repr__(self):
        return "Enemy(%d,%d)"%(self.hp,self.atk)

# d01=Enemy(20,100)
# d03=Enemy(20,100)
# print(d01)
# d02=eval(repr(d01))
# d04=eval(repr(d03))
# print(d02)
# print(d04)
# d02.hp=500
# print(d01.__dict__)
# print(d02.__dict__)

"""
运算符重载
"""
class Vector:
    def __init__(self,x):
        self.x=x
    def __add__(self, other):
        return self.x+other
# v01=Vector(1)
# v2=v01+1
# print(v2)

"""
技能项目
"""
class SkillEffect:
    def damage(self):
        pass
class DecreaseEffect(SkillEffect):
    def damage(self):
        print("减弱能力")
class DisinessEffect(SkillEffect):
    def damage(self):
        print("眩晕")
class SkillGenerate:
    def __init__(self,name):
        self.name=name
        self.__list_skill=self.__get_confrigurate_file()
        self.__class_skill=self.generate_skill()

    def __get_confrigurate_file(self):
        return {"xlsbz":[DecreaseEffect()],"jybgz":[DisinessEffect()],"jzz":[DecreaseEffect(),DisinessEffect()]}

    def generate_skill(self):
        list=[]
        for item in self.__list_skill[self.name]:
            list.append(eval("item"))
        return list
    def damage_effect(self):
        for item in self.__class_skill:
            item.damage()
# file01={"xlsbz":[DecreaseEffect()],"jybgz":[DisinessEffect()],"jzz":[DecreaseEffect(),DisinessEffect()]}
# a=SkillGenerate("xlsbz")
# a.damage_effect()
# print("------------")
# a=SkillGenerate("jybgz")
# a.damage_effect()
#
# print("------------------")
# a=SkillGenerate("jzz")
# a.damage_effect()
import time
# print(time.time())#输出当前时间的时间戳
#时间戳到时间元组
# print(time.localtime())#输出当前的时间元组
# print(time.localtime(1686969406))#输出当前的时间元组
#时间元组到时间戳
# print(time.mktime(time.localtime()))
#时间元组到str
# print(time.strftime("%y-%m-%d %H:%M:%S",time.localtime()))
#str到时间元组
# print(time.strptime("23-06-17 10:49:20","%y-%m-%d %H:%M:%S"))
def get_xingqi(date_value):
    tuple_time=time.strptime(date_value,"%y-%m-%d %H:%M:%S")
    date=tuple_time.tm_wday
    if date==1:
        print("这天是星期一")
    elif date==2:
        print("这天是星期二")
    elif date == 3:
        print("这天是星期三")
    elif date==4:
        print("这天是星期四")
    elif date==5:
        print("这天是星期五")
    elif date==6:
        print("这天是星期六")
    else:
        print("这天是星期日")
# get_xingqi("23-06-18 12:41:50")

def get_days(date_value):
    tuple_time=time.strptime(date_value,"%y-%m-%d")
    stamp_tiime=time.mktime(tuple_time)
    stamp_time_now=time.time()
    total_days=(stamp_time_now-stamp_tiime)//(60*60*24)
    print(total_days)
# get_days("93-09-20")
# get_days("23-06-15")
def get_score():
    while True:
        try:
            score=int(input("请输入成绩"))
            if score not in range(101):
                continue
        except :
            print("成绩不正确")
        else:
            return score
# print(get_score())
"""
自定义异常类
"""
class AtkError(Exception):
    def __init__(self,message,code_line,value,number):
        self.message=message
        self.code_line=code_line
        self.value=value
        self.number=number
class EnemyTest:
    def __init__(self,atk):
        self.atk=atk

    @property
    def atk(self):
        return self.__atk
    @atk.setter
    def atk(self,value):
        if 10<value<100:
            self.__atk=value

        else:
            raise AtkError("值不在范围内",578,value,1001)
# try:
    # EnemyTest(50)
# except AtkError as e:
    # print(e.message)

"""
迭代器原理
"""
# iteror=("铁扇公主","铁锤公主").__iter__()
# while True:
#     try:
#         item=iteror.__next__()
#         # print(item)
#     except StopIteration:
#         break
"""
迭代器
"""
class Skill:
    pass
class SkillManger:
    def __init__(self):
        self.__skills=[]
    def add(self,value):
        self.__skills.append(value)
# manger=SkillManger()
# manger.add(Skill())
# manger.add(Skill())
# manger.add(Skill())
# for item in manger._SkillManger__skills:
#     print(item)
"""
迭代器
"""
class GraphMangement:
    def __init__(self):
        self.list=[]
    def add_graph(self,graph):
        self.list.append(graph)
    def calculate_area(self):
        for item in self.list:
            if not isinstance(item,Area):
                raise ValueError
            area=item.area_method()
            print("面积是%d"%area)
    def __iter__(self):
        return GraphMangerIterator(self.list)
class GraphMangerIterator:
    def __init__(self,target):
        self.target=target
        self.index=-1
    def __next__(self):
        if self.index>=len(self.target)-1:
            raise StopIteration
        self.index+=1
        temp=self.target[self.index]
        return temp

class Area:
    def area_method(self,*args):
        raise ValueError

class Square(Area):
    def __init__(self,length):
        self.length=length
    def area_method(self):
        area=self.length**2
        return area

class Rectangle(Area):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area_method(self):
        area=self.length*self.width
        return area
m=GraphMangement()
s01=Square(5)
r01=Rectangle(10,6)
m.add_graph(s01)
m.add_graph(r01)
# for item in m:
#     print(item)

"""
迭代器---->yield
"""
class GraphMangement:
    def __init__(self):
        self.list=[]
    def add_graph(self,graph):
        self.list.append(graph)
    def calculate_area(self):
        for item in self.list:
            if not isinstance(item,Area):
                raise ValueError
            area=item.area_method()
            print("面积是%d"%area)
    def __iter__(self):
        # return GraphMangerIterator(self.list)
        number=0
        while number<len(self.list):
            yield  self.list[number]
            number+=1
# class GraphMangerIterator:
#     def __init__(self,target):
#         self.target=target
#         self.index=-1
#     def __next__(self):
#         if self.index>=len(self.target)-1:
#             raise StopIteration
#         self.index+=1
#         temp=self.target[self.index]
#         return temp

class Area:
    def area_method(self,*args):
        raise ValueError

class Square(Area):
    def __init__(self,length):
        self.length=length
    def area_method(self):
        area=self.length**2
        return area

class Rectangle(Area):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area_method(self):
        area=self.length*self.width
        return area
m=GraphMangement()
s01=Square(5)
r01=Rectangle(10,6)
m.add_graph(s01)
m.add_graph(r01)
# for item in m:
#     print(item)
"""
生成器原理
"""
def mylist(value):
    number=0
    while number<len(value):
        if value[number]%2==0:
            yield value[number]
        number+=1
# for item in mylist([3,2,9,888,6,90,5,7]):
#     print(item)

"""
直接调用生成器
"""
class GraphMangement:
    def __init__(self):
        self.list=[]
    def add_graph(self,graph):
        self.list.append(graph)
    def calculate_area(self):
        for item in self.list:
            if not isinstance(item,Area):
                raise ValueError
            area=item.area_method()
            print("面积是%d"%area)


# class GraphMangerIterator:
#     def __init__(self,target):
#         self.target=target
#         self.index=-1
#     def __next__(self):
#         if self.index>=len(self.target)-1:
#             raise StopIteration
#         self.index+=1
#         temp=self.target[self.index]
#         return temp

class Area:
    def area_method(self,*args):
        raise ValueError

class Square(Area):
    def __init__(self,length):
        self.length=length
    def area_method(self):
        area=self.length**2
        return area

class Rectangle(Area):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area_method(self):
        area=self.length*self.width
        return area
m=GraphMangement()
s01=Square(5)
r01=Rectangle(10,6)
m.add_graph(s01)
m.add_graph(r01)
def mygenerator(value):
    for item in value:
        yield item
# for item in mygenerator(m):
#     print(item)
# print(min(1,2,5,0))
def my_zip(list01,list02):
    for index in range(min(len(list01),len(list02))):
        yield list01[index],list02[index]
# print(my_zip(["孙悟空","猪八戒"],[1,2,3]))
# for item in my_zip(["孙悟空","猪八戒"],[1,2,3]):
#     print(item)

list05=[1,2,"111",True,3.2,10,"Str"]
# re=(item for item in list05 if type(item)==str)
# for item in re:
#     print(item)
def get_data(func_condition):
    for item in list05:
        if func_condition(item):
            yield item
def get_even(item):
    return type(item)==int and item%2==0
def get_big_10(item):
    return  type(item)==int and item>10
# for item in get_data(get_even):
#     print(item)

# re=get_data(lambda item:type(item)==int and item%2==0)
# count=0
# for item in re:
#     count+=1
# print(count)
# list05=[1,2,"111",True,3.2,10,"Str"]
# tuple01=([1,1,1],[2,2],[5,4,5,6,6])
# re=max(tuple01,key=lambda item:len(item))
# print(re)
# list07=[1,2,10,0,9]
# re=max(list07)
# print(re)

"""
外部嵌套作用域
"""
# def fun01():
#     a=1
#     def fun02():
#         b=2
#         print(a)
#     fun02()
# fun01()

list08=[1,2,3,4,5]
# for i in range(-1,-len(list08)-1,-1):
# for i in range(-1,-len(list08)-1,-1):
#     print(list08[i])
def veriy_account(func):
    def wrapper(*args,**kwargs):
        print("验证账号")
        return func(*args,**kwargs)
    return wrapper
@veriy_account
def deposit(money):
    print("存钱啦",money)

@veriy_account
def withdraw(login_id,pwd):
    print("%d %d存钱啦"%(login_id,pwd))
#
# deposit(1000)
# withdraw(123,123)

import time
def calculate_time(func):
    def wrapper(*args,**kwargs):
        time_begin=time.time()
        func(*args,**kwargs)
        time_end=time.time()
        print(time_end-time_begin)
    return wrapper

@calculate_time
def fun01():
    time.sleep(2)
    print("结束了")

# fun01()

"""
装饰器
"""
def verify_permission(fun):
    def wrapper(*args,**kwargs):
        print("权限验证")
        fun(*args,**kwargs)
    return wrapper

@verify_permission
def login(account):
    print(account,"登陆啦")

# login(123)

class Enemy_list:
    def __init__(self,name,hp,atk):
        self.name=name
        self.hp=hp
        self.atk=atk

    def __str__(self):
        return "敌人姓名是%s,血量%d,攻击力%d"%(self.name,self.hp,self.atk)
e_list=[
    Enemy_list("灭霸",50,100),
    Enemy_list("张无忌",100,300),
    Enemy_list("赵敏",0,0),
    Enemy_list("周芷若",10,80),
    ]

#找出血量大于50的
#找出攻击力大于200的
#找出血量为0的
# def find01():
#     for item in e_list:
#         if item.hp>50:
#             yield item
# for item in find01():
#     print(item)
def find_condition(item):
    return item.hp>50
class List_helper:
    @staticmethod
    def find(fun):
        for item in e_list:
            if fun(item):
                yield item

# for item in List_helper.find(lambda x:x.hp>50):
#     print(item)
# for item in List_helper.find(find_condition):
#     print(item)
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
#     f.write(item)
#     f.write("\n")
# f.writelines(l)
class Person:
    def __init__(self,name):
        self.name=name

class Student(Person):
    def __init__(self,name):
        super().__init__(name)

    def speaking(self):
        print("speaking")

s01=Student("hhh")
# print(s01.__dict__)
# s01.speaking()
"""
装饰器
"""
def verify_permission(fun):
    def wrapper(*args,**kwargs):
        print("权限验证")
        fun(*args,**kwargs)
    return wrapper

@verify_permission
def login(account):
    print(account,"登陆啦")

# login(123)

import time
# print(time.strftime("%Y-%m-%d %H-%M-%S"))
# print(time.strptime("23-06-17 10:49:20","%y-%m-%d %H:%M:%S"))

import os
# print(os.path.dirname(__file__))

class Person01:
    def __init__(self,name):
        self.name=name

# class Student(Person01):
    # def __init__(self,driver):
        # super().__init__()
        # self.driver=driver

# m=int(input("请输入数字"))
# assert 10<m,"值太小了"
# m=-1
# if m:
#     print("T")
# else:
#     print("F")

import random
# m=random.randint(1,6)
# print(m)
n,tuple,once=1000,0,0
while n>0:
    re=[random.randint(1,6) for item in range(3)]
    if all(item==6 for item in re):
        tuple+=1
    if any(item==6 for item in re):
        once+=1
    n-=1
# print("三次都是6",tuple)
# print("至少有一个6",once)
# color=input("请输入颜色")
# match color:
#     case "red":
#         m="红色"
#     case "yellow":
#         m="黄色"
#     case _:
#         m="绿色"
# print("输入的颜色是",m)
# from datetime import datetime
# # print(datetime.today().weekday())
# # print(datetime.today())
# match datetime.today().weekday():
#     case 0:
#         re="星期一"
#     case _:
#         re="非周一"
# print(re)
# a=eval(input("x,y"))
# match a:
#     case 0,0:
#         print("原点")
#     case x,0:
#         print("X轴")
#     case (x,y):
#         print("其他")
# alist=[int(x) for x in input().split()]
# print(alist)
# a_dict={"Tom":55,"Jason":60,"Alice":100}
# v=60
# if any(a_dict[found:=s]==v for s in a_dict):
#     print(found)

# def sum():
#     b=a
#     a=1+2
#     print(b)
# a=5
# sum()
# print(a)
# b_list=[[0]*2 for i in range(10)]
# print(b_list)
# a,b,c=1,2,3
# print(f"{a=},{b=},{c=}")

# a="True"
# b="False"
# print(a and b)
# print(a or b)

# dict={}
# result=open(r"C:\Users\Lenovo\Desktop\test2.txt","a",encoding="utf-8")
# with open(r"C:\Users\Lenovo\Desktop\test.txt",encoding="utf-8") as f:
#     content=f.readlines()
#     for i in range(len(content)):
#         if content[i]=="1\n":
#             a=content[i-1].split("  ")[0]
#             result.write(a)
#
#             b=content[i-1].split("  ")[1]
#
#             result.write(b)
# dict={}
# with open(r"C:\Users\Lenovo\Desktop\test.txt",encoding="utf-8") as f:
#     content=f.readlines()
#     for i in range(len(content)):
#        key=content[i].split("  ")[0]
#        dict[key]=content[i].split("  ")[1].split("\n")[0]
#     print(dict)
    # for i in content:
    #     print(i)
# a="你好".encode()
# print(a)
# print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode())
# dict={}
# result=open(r"C:\Users\Lenovo\Desktop\test2.txt","ab+")
#
# with open(r"C:\Users\Lenovo\Desktop\test.txt","ab+") as f:
#     content=f.readlines()
#     print(f.tell())
#     f.seek(3,1)
#     f.write("\nttttttttwqwq".encode())
#     result.writelines(content)
# class Teacher:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class ChineseTeacher(Teacher):
#     def __init__(self,name,age,score):
#
#         super().__init__(name,age)
#         self.score=score
#     def __str__(self):
#         return "姓名是%s,年龄是%d"%(self.name,self.age)
# m=ChineseTeacher("hh",10,100)
# print(m)
# # Teacher()
# list01=[1,2,"weew",False]
# def find01():
#     for item in list01:
#         if type(item)==str:
#             yield item
# m=find01()
# for item in m :
#     print(item)
#
# m=(item for item in list01 if type(item)==str )
import os
def get_path():
    print(os.path.abspath(__name__))
    print(os.path.abspath(__file__))
if __name__ == '__main__':
    m=get_path()
