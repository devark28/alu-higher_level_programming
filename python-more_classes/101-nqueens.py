#!/usr/bin/python3
import sys

class Vector:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_displacement(self, point: 'Point') -> Vector:
        return Vector(point.__x - self.__x, point.__y - self.__y)

class Tree:
    def __init__(self, max_children):
        self.__max_children = max_children
        self.__nodes_pool = [Node()]

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
