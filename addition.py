from enum import Enum


class Point:
    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Point):
            return __value.x == self.x and __value.y == self.y
        return False

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value


class GameStatus(Enum):
    RUN = 0
    STOP = 1


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
