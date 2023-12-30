from addition import Direction, Point
from random import choice
import numpy as np


class Field:
    def __init__(self, side) -> None:
        self.side = side
        self.cells = np.zeros((side, side))


class Food:
    def __init__(self) -> None:
        self.__position = Point(0, 0)
        self.color = (255, 0, 0)

    @property
    def position(self):
        return self.__position

    def apply_random_coordinates(self, side):
        self.__position = Point(choice(range(side)), choice(range(side)))


class Snake:
    def __init__(self, field_side) -> None:
        self.color = (0, 255, 0)
        self._reset()

    def _reset(self):
        self.tail = [Point(10, 10)]
        self.x, self.y = self.tail[0].x, self.tail[0].y
        self.direction = None

    def _move_tail(self):
        # Copy old tail to move it cell by cell
        old_tail = self.tail.copy()

        # Moving all the cells excluding snake's head
        for i in range(1, len(self.tail)):
            self.tail[i] = old_tail[i-1]


    def grow(self, cell: Point):

        # Append new cell depending on snake direction
        match self.direction:
            case Direction.UP | Direction.DOWN:
                self.tail.insert(len(self.tail), (cell.x, self.tail[0].y))
            case Direction.LEFT | Direction.RIGHT:
                self.tail.insert(len(self.tail), (self.tail[0].x, cell.y))

        # Set new cell as head
        self.x, self.y = self.tail[0].x, self.tail[0].y

    def move(self, side):

        # Check if snake's outside the game field and game over it if so
        if self.y < 0:
            self.y = side-1
        elif self.y > side-1:
            self.y = 0
        elif self.x < 0:
            self.x = side-1
        elif self.x > side-1:
            self.x = 0
        else:
            # Move head depending on snake's direction
            match self.direction:
                case Direction.UP:
                    self.y -= 1
                case Direction.DOWN:
                    self.y += 1
                case Direction.LEFT:
                    self.x -= 1
                case Direction.RIGHT:
                    self.x += 1

        # Moving tail after moving head
        self._move_tail()

        head = Point(self.x, self.y)

        # Check if snake hit itself and reseting game if so
        if head in self.tail[1:]:
            self._reset()
        else:
            # Otherwise setting new head position
            self.tail[0] = head
