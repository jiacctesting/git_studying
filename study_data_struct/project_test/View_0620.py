from model_0620 import GameMovement
from game_0620 import GameCoreController
from model_0620 import GameMovement
import os
class View:
    def __init__(self):
        self.__controller=GameCoreController()
    def main(self):
        self.__start()
        self.update()
    def draw_map(self):
        # os.system("clear")
        for line in self.__controller.map:
            print(line)
            print(end="")

    def __start(self):
        self.__controller.get_new_number()
        self.__controller.get_new_number()
        self.draw_map()

    def update(self):
        while True:
            self.movement()
            self.__controller.get_new_number()
            self.draw_map()
            if self.__controller.verify_game_is_over():
                print("游戏结束")
                break

    def movement(self):
        dir = input("请输入需要移动的方向：WSAD")
        dir_dict = {
            "W": GameMovement.UP,
            "S": GameMovement.DOWN,
            "A": GameMovement.LEFT,
            "D": GameMovement.RIGHT
        }
        if dir in dir_dict:
            self.__controller.move(dir_dict[dir])


if __name__=="__main__":
    m=View()
    m.main()
