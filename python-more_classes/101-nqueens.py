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

    def __str__(self) -> str:
        return f"Point({self.__x}, {self.__y})"

    def __repr__(self) -> str:
        return f"Point({self.__x}, {self.__y})"

    def __eq__(self, point: 'Point') -> bool:
        return self.__x == point.x and self.__y == point.y

    def __add__(self, vector: Vector) -> 'Point':
        return Point(self.__x + vector.x, self.__y + vector.y)


class QueensChessEngine:
    __knights_moves = [
        Vector(2, 1), Vector(2, -1), Vector(-2, 1), Vector(-2, -1),
        Vector(1, 2), Vector(1, -2), Vector(-1, 2), Vector(-1, -2)
    ]

    def __init__(self, n):
        self.__N = n
        self.__board = [[False for _ in range(n)] for _ in range(n)]

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

    def remove_queen(self, point: Point) -> None:
        if not point.x in range(self.__N):
            raise ValueError("Row out of bounds")
        if not point.y in range(self.__N):
            raise ValueError("Col out of bounds")
        if not self.__board[point.x][point.y]:
            raise ValueError("Queen does not exist in this position")
        self.__board[point.x][point.y] = False

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
        n = self.__N - 1
        end_point = Point(
            point.x + min(n - point.x, n - point.y),
            point.y + min(n - point.x, n - point.y)
        )
        for x, y in zip(
                range(start_point.x, end_point.x + 1),
                range(start_point.y, end_point.y + 1)
        ):
            if self.__board[x][y]:
                return False
        return True

    def is_safe_secondary_diagonal(
            self, point: Point
    ) -> bool:
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

    def all_knight_points(
            self, point: Point
    ) -> list[Point]:
        return [
            point + move
            for move in self.__knights_moves
            if point.x + move.x in range(self.__N)
            and point.y + move.y in range(self.__N)]

    def get_queens_positions(self) -> list[Point]:
        return [
            Point(i, j)
            for i in range(self.__N)
            for j in range(self.__N)
            if self.__board[i][j]
        ]

    def __str__(self) -> str:
        return "\n".join([
            " ".join([
                "Q" if self.__board[i][j] else "."
                for j in range(self.__N)])
            for i in range(self.__N)
        ])

    def auto_add_queens(
            self,
            points: list[Point]
    ) -> None:
        for point in points:
            for move in self.all_knight_points(point):
                try:
                    self.add_queen(move)
                    continue
                except ValueError:
                    continue


class Node:
    cold = False

    def __init__(self, point: Point, parent: 'Node' = None):
        self.__point = point
        self.__parent = parent
        if parent is None:
            self.__depth = 0
        else:
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


class Tree:
    def __init__(self, max_children):
        self.__max_children = max_children
        self.__nodes_pool = []
        # self.__nodes_pool = [Node(Point(0, 0))]
        self.__root = None
        # self.__root = self.__nodes_pool[0]
        self.__engine = QueensChessEngine(max_children)

    @property
    def engine(self) -> QueensChessEngine:
        return self.__engine

    @property
    def root(self) -> Node:
        return self.__root

    @property
    def max_children(self) -> int:
        return self.__max_children

    def add_node(self, parent: Node | None, point: Point):
        self.__nodes_pool.append(Node(point, parent))

    def forward(self, node: Node, point: Point) -> bool:
        try:
            self.engine.add_queen(point)
            node = Node(point, node)
            self.__nodes_pool.append(node)

            if len(self.__nodes_pool) == self.__max_children:
                return True

            for safe_point in self.engine.all_knight_points(point):
                if self.forward(node, safe_point):
                    return True

            self.backward()
            return False
        except ValueError:
            self.backward()
            return False

    def backward(self) -> list[Point]:
        if not self.__nodes_pool:
            return []

        node = self.__nodes_pool.pop()
        self.engine.remove_queen(node.point)
        return self.engine.get_queens_positions()

    def solve(self) -> bool:
        initial_point = Point(0, 1)
        self.engine.add_queen(initial_point)
        self.__root = Node(initial_point)
        self.__nodes_pool.append(self.__root)

        for safe_point in self.engine.all_knight_points(initial_point):
            if self.forward(self.__root, safe_point):
                return True

        return False


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

    tree = Tree(max_children=N)
    if tree.solve():
        print(tree.engine)
    else:
        print("No solution found")
