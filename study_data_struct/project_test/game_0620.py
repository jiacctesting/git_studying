#将0元素移到末尾
# list_merge=[2,0,2,0]
# list_merge=[0,0,2,0]
# list_merge=[2,2,2,2]
# list_merge=[2,2,2,0]
# list_merge=None
import random
from model_0620 import GameMovement

class GameCoreController:
    def __init__(self):
        self.__list_merge=None
        self.__map=[
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            # [4,8,16,2],
            # [8,4,8,16],
            # [2,16,32,2],
            # [16,8,4,8]
        ]
        self.__location_list=[]
    @property
    def map(self):
        return self.__map
    def __move_zero_element(self):
        """
        零元素移到末尾
        """
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i]==0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        """
        先去0，合并相邻的相同元素
        """
        self.__move_zero_element()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i]==self.__list_merge[i + 1]:
                self.__list_merge[i]+=self.__list_merge[i]
                self.__list_merge[i + 1]=0
                self.__move_zero_element()

    def move_to_left(self):
        """
        左移，从二维列表中每行内容交给list_merge
        """
        for line in self.__map:
            self.__list_merge=line
            self.__merge()

    def move_to_right(self):
        for line in self.__map:
            #从右向左取出数据形成新列表
            self.__list_merge=line[::-1]
            self.__merge()
            #从右向左接受合并后的数据
            line[::-1]=self.__list_merge

    def __square_matrix_transpose(self):
        for i in range(len(self.__map)-1):
            for j in range(i+1,len(self.__map)):
                self.__map[i][j],self.__map[j][i]=self.__map[j][i],self.__map[i][j]

    def move_to_up(self):
        self.__square_matrix_transpose()
        self.move_to_left()
        self.__square_matrix_transpose()

    def move_to_down(self):
        self.__square_matrix_transpose()
        self.move_to_right()
        self.__square_matrix_transpose()

    def get_new_number(self):
        self.__get_empty_location()
        if len(self.__location_list)==0:
            return
        loc=random.choice(self.__location_list)
        if random.randint(1,10)==1:
            self.__map[loc[0]][loc[1]]=4
        else:
            self.__map[loc[0]][loc[1]] = 2
        self.__location_list.remove(loc)

    def __get_empty_location(self):
        self.__location_list.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map)):
                if self.__map[r][c]==0:
                    self.__location_list.append((r,c))
        return self.__location_list

    def move(self,dir):
        if dir==GameMovement.UP:
            self.move_to_up()
        elif dir==GameMovement.DOWN:
            self.move_to_down()
        elif dir == GameMovement.LEFT:
            self.move_to_left()
        else:
            self.move_to_right()

    def verify_game_is_over(self):
        self.__get_empty_location()
        if len(self.__get_empty_location())==0 and self.__element_moveable()==False:
            return True
        else:
            return False
    def __element_moveable(self):
        for i in range(len(self.__map)-1):
            for j in range(len(self.__map)-1):
                if self.__map[i][j]==self.__map[i][j+1] or self.__map[i][j]==self.__map[i+1][j]:
                    return True
                else:
                    return False

if __name__=="__main__":
    controller=GameCoreController()
    # controller.__get_new_number()
    print(controller.map)

