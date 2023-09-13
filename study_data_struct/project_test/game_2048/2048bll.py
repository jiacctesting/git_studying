# coding=utf-8
import random

from model import *
from model import *


class GameConcroller:
    def __init__(self):
        self.__list_target = None
        self.__map = [
            [2, 8, 4, 2],
            [8, 4, 2, 8],
            [4, 8, 16, 4],
            [2, 4, 0, 16]
        ]
        self.location_list = []

    @property
    def map(self):
        return self.__map

    def __move_zero_toend(self):
        for i in range(-1, -len(self.__list_target) - 1, -1):
            if self.__list_target[i] == 0:
                del self.__list_target[i]
                self.__list_target.append(0)

    def __merge(self):
        self.__move_zero_toend()
        for i in range(len(self.__list_target) - 1):
            if self.__list_target[i] == self.__list_target[i + 1]:
                self.__list_target[i] = self.__list_target[i] + self.__list_target[i + 1]
                del self.__list_target[i + 1]
                self.__list_target.append(0)

    def __move_to_left(self):
        for line in self.__map:
            self.__list_target = line
            self.__merge()

    def __move_to_right(self):
        for line in self.__map:
            self.__list_target = line[::-1]
            self.__merge()
            line[:] = self.__list_target[::-1]

    def __reverse_line_and_row(self):
        for i in range(len(self.__map)):
            for j in range(i, len(self.__map)):
                self.__map[i][j], self.__map[j][i] = self.__map[j][i], self.__map[i][j]

    def __move_to_up(self):
        self.__reverse_line_and_row()
        self.__move_to_left()
        self.__reverse_line_and_row()

    def __move_to_down(self):
        self.__reverse_line_and_row()
        self.__move_to_right()
        self.__reverse_line_and_row()

    def move(self, dir):
        if dir == DataController.UP:
            self.__move_to_up()
        elif dir == DataController.DOWN:
            self.__move_to_down()
        elif dir == DataController.LEFT:
            self.__move_to_left()
        elif dir == DataController.RIGHT:
            self.__move_to_right()

    def generate_new_number(self):
        location_empty_list = self.get_empty_list()
        if len(location_empty_list) == 0:
            return
        adding_location = random.choice(location_empty_list)
        self.__map[adding_location.r_index][adding_location.c_index] = 4 if random.randint(1, 10) == 1 else 2

    def get_empty_list(self):
        self.location_list.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    self.location_list.append(ListLocation(r, c))
        return self.location_list

    def judgement_game_over(self):
        list_empty_list = self.get_empty_list()
        list_element_issame = self.judgement_element_moveable()
        if len(list_empty_list) == 0 and list_element_issame == False:
            print("游戏结束")
        else:
            print("游戏继续")

    def judgement_element_moveable(self):
        for r in range(len(self.__map) - 1):
            for c in range(len(self.__map) - 1):
                if self.__map[r][c] == self.__map[r][c + 1] or self.__map[r][c] == self.__map[r + 1][c]:
                    return True
                else:
                    return False


# -----------------测试代码---------------------
if __name__ == "__main__":
    controller = GameConcroller()
    # controller.move_to_left()
    # controller.move_to_right()
    # print(controller.map)
    # controller.move(DataController.DOWN)
    # print(controller.map)
    # controller.generate_new_number()
    # controller.generate_new_number()
    controller.judgement_game_over()
    controller.move(2)
    print(controller.map)
