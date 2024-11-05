#!/usr/bin/python3
import sys

class QueensChessEngine:
    def __init__(self, N):
        self.__N = N
        self.__board = [[False for i in range(N)] for j in range(N)]

    def add_queen(self, point: 'Point') -> None:
        row, col = point.x, point.y
        if row in range(self.__N):
            raise ValueError("Row out of bounds")
        if col in range(self.__N):
            raise ValueError("Col out of bounds")
        if self.__board[row][col]:
            raise ValueError("Queen already exists in this position")
        if not self.is_safe(row, col):
            raise ValueError("Queen cannot be placed in this position")
        self.__board[row][col] = True

    def is_safe(self, row, col) -> bool:
        return False

class Vector:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

class Point:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    def get_displacement(self, point: 'Point') -> Vector:
        return Vector(point.__x - self.__x, point.__y - self.__y)

class Tree:
    def __init__(self, max_children):
        self.__max_children = max_children
        self.__nodes_pool = [Node(Point(0, 0))]

class Node:
    def __init__(self, n):
        pass

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    if argc != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(argv[1])
        if N < 4:
            print("N must be at least 4")
            exit(1)
    except ValueError:
        print("N must be a number")
        exit(1)

    tree = Tree(max_children=8)
