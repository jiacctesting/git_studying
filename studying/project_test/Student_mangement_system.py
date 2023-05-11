# coding=utf-8
"""
学生管理系统
"""


class StudentModel:

    def __init__(self, name="", age=0, score=0, id=0):
        # 编号id,姓名 name,年龄 age,成绩 score
        self.id = id
        self.name = name
        self.age = age
        self.score = score


class StudentManagerController:
    # 类变量，用来创建id
    guid = 1000

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu):
        """
        添加学生
        :param stu: 学生信息
        :return:
        """
        self.generate_id(stu)
        self.__stu_list.append(stu)

    def generate_id(self, stu):
        StudentManagerController.guid += 1
        stu.id = StudentManagerController.guid

    def remove_student(self, id):
        """
        删除学生:根据编号移除学生信息
        :param value: 学生id
        :return:
        """
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True  # 表示移除成功
        return False  # 表示移除失败

    def update_student(self, stu_info):
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True  # 表示更新成功
        return False  # 表示更新失败

    def order_by_score(self):
        for i in range(len(self.__stu_list)):
            for j in range(i+1,len(self.__stu_list)):
                if self.__stu_list[i].score<self.__stu_list[j].score:
                    self.__stu_list[i],self.__stu_list[j]=self.__stu_list[j],self.__stu_list[i]



"""
测试代码
"""


# s01 = StudentModel("jia", 10, 88)
# s02 = StudentModel("jia2", 10, 99)
# s03 = StudentModel("jia3", 10, 100)
# s04 = StudentModel("hhhh", 10, 100,1003)
#
# a = StudentManagerController()
# a.add_student(s01)
# a.add_student(s02)
# a.add_student(s03)
# b=a.order_by_score()
# print(b)
#
# a.update_student(s04)
# for item in a.stu_list:
#     print(item.id,item.name,item.age,item.score)


class StudentManagerView:
    # manager = StudentManagerController()

    def __init__(self):
        self.manager = StudentManagerController()

    def __display_menu(self):
        print("1)添加学生信息")
        print("2)显示学生信息")
        print("3)删除学生信息")
        print("4)修改学生信息")
        print("5)按照成绩从高到低显示学生信息")

    def __select_menu_item(self):
        item = int(input("请选择"))
        if item == 1:
            self.__input_students()
        elif item == 2:
            self.__output_students()
        elif item == 3:
            self.__delete_student()
        elif item == 4:
            self.__modify_student()
        elif item == 5:
            self.__output_student_by_score()

    def __input_students(self):
        name = input("请输入名字")
        age = int(input("请输入年龄"))
        score = int(input("请输入分数"))
        stu_info = StudentModel(name, age, score)
        self.manager.add_student(stu_info)

    def __output_students(self):
        for item in self.manager.stu_list:
            print(item.id, item.name, item.age, item.score)

    def __delete_student(self):
        """
        根据id删除学生
        :return:
        """
        id = int(input("请输入要删除的学生id"))
        self.manager.remove_student(id)

        # for item in self.manager.stu_list:
        #     if id==item.id:
        #         self.manager.remove_student(id)

    def __modify_student(self):
        """
        修改学生信息
        :return:
        """
        stu = StudentModel()
        stu.id = int(input("请输入要修改的学生id"))
        stu.name = input("请输入新名字")
        stu.age = int(input("请输入新年龄"))
        stu.score = int(input("请输入新分数"))
        self.manager.update_student(stu)

        # for item in self.manager.stu_list:
        #     if id == item.id:
        #         item.name = input("请输入新名字")
        #         item.age = int(input("请输入新年龄"))
        #         item.score = int(input("请输入新分数"))
        #         stu_info_new = StudentModel(item.name, item.age, item.score)
        #     self.manager.update_student(stu_info_new)

    def __output_student_by_score(self):
        self.manager.order_by_score()
        for item in self.manager.stu_list:
            print(item.id,item.name,item.age,item.score)


    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu_item()


a = StudentManagerView()
a.main()
