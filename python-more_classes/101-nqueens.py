#!/usr/bin/python3
import sys

class Vector:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

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

    def __add__(self, vector: Vector) -> 'Point':
        return Point(self.__x + vector.x, self.__y + vector.y)

class QueensChessEngine:
    __knights_moves = [
        Vector(2, 1), Vector(2, -1), Vector(-2, 1), Vector(-2, -1),
        Vector(1, 2), Vector(1, -2), Vector(-1, 2), Vector(-1, -2)
    ]

    def __init__(self, N):
        self.__N = N
        self.__board = [[False for i in range(N)] for j in range(N)]

    def add_queen(self, point: Point) -> None:
        if not point.x in range(self.__N):
            raise ValueError("Row out of bounds")
        if not point.y in range(self.__N):
            raise ValueError("Col out of bounds")
        if self.__board[point.x][point.y]:
            raise ValueError("Queen already exists in this position")
        if not self.is_safe(point):
            raise ValueError("Queen cannot be placed in this position")
        self.__board[point.x][point.y] = True

    def is_safe(self, point: Point) -> bool:
        if not self.is_safe_row(point.x):
            return False
        if not self.is_safe_col(point.y):
            return False
        if not self.is_safe_main_diagonal(point):
            return False
        if not self.is_safe_secondary_diagonal(point):
            return False
        return True

    def is_safe_row(self, row: int) -> bool:
        return not any(self.__board[row])

    def is_safe_col(self, col: int) -> bool:
        return not any([self.__board[i][col] for i in range(self.__N)])

    def is_safe_main_diagonal(self, point: Point) -> bool:
        # Get the start and end points of the main diagonal
        start_point = Point(
            point.x - min(point.x, point.y),
            point.y - min(point.x, point.y)
        )
        N = self.__N - 1
        end_point = Point(
            point.x + min(N - point.x, N - point.y),
            point.y + min(N - point.x, N - point.y)
        )
        for x, y in zip(
            range(start_point.x, end_point.x + 1),
            range(start_point.y, end_point.y + 1)
            ):
            if self.__board[x][y]:
                return False
        return True

    def is_safe_secondary_diagonal(self, point: Point) -> bool:
        # Get the start and end points of the secondary diagonal
        start_point = Point(
            point.x - min(point.x, self.__N - 1 - point.y),
            point.y + min(point.x, self.__N - 1 - point.y)
        )
        end_point = Point(
            point.x + min(self.__N - 1 - point.x, point.y),
            point.y - min(self.__N - 1 - point.x, point.y)
        )
        for x, y in zip(
            range(start_point.x, end_point.x + 1),
            range(start_point.y, end_point.y - 1, -1)
            ):
            if self.__board[x][y]:
                return False
        return True

    def all_knight_points(self, point: Point) -> list[Point]:
        return [point + move for move in self.__knights_moves]

    def get_queens_positions(self) -> list[Point]:
        return list([
            Point(i, j)
            for i in range(self.__N)
            for j in range(self.__N)
            if self.__board[i][j]
        ])

    def auto_add_queens(self, default_point: Point = Point(0, 0)) -> None:
        points = self.get_queens_positions()
        if len(points) == 0:
            self.add_queen(default_point)
        points = self.get_queens_positions()
        for point in points:
            for move in self.all_knight_points(point):
                try:
                    self.add_queen(move)
                    break
                except ValueError:
                    continue

class Node:
    cold = False

    def __init__(self, point: Point, parent: 'Node' = None):
        self.__point = point
        self.__parent = parent
        self.__depth = parent.depth + 1

    @property
    def depth(self) -> int:
        return self.__depth

    @property
    def point(self) -> Point:
        return self.__point

    @property
    def parent(self) -> 'Node':
        return self.__parent if self.__parent else None

# class Tree:
#     def __init__(self, max_children):
#         self.__max_children = max_children
#         self.__nodes_pool = [Node(Point(0, 0))]
#         self.__root = self.__nodes_pool[0]

#     def add_node(self, parent: 'Node', point: Point) -> 'Node':
#         self.__nodes_pool.append(Node(point, parent))

#     @property
#     def root(self) -> Node:
#         return self.__root

#     @property
#     def max_children(self) -> int:
#         return self.__max_children

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

    # tree = Tree(max_children=8)
    engine = QueensChessEngine(N)
    engine.auto_add_queens()
    print(engine.get_queens_positions())
    engine.auto_add_queens(Point(1, 0))
    print(engine.get_queens_positions())
    engine.auto_add_queens(Point(0, 1))
    print(engine.get_queens_positions())
