# coding=utf-8
"""
2048数据模型

"""


class DataController:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
class ListLocation:
    def __init__(self,r,c):
        self.r_index=r
        self.c_index=c
