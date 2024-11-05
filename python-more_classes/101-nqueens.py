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

    def __str__(self) -> str:
        return f"Point({self.__x}, {self.__y})"


class QueensChessEngine:
    def __init__(self, n):
        self.__N = n
        self.__board = [[False for _ in range(n)] for _ in range(n)]
        self.solutions = []

    def is_safe(self, row: int, col: int) -> bool:
        # Check column
        for i in range(row):
            if self.__board[i][col]:
                return False
        # Check main diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.__board[i][j]:
                return False
        # Check secondary diagonal
        for i, j in zip(range(row, -1, -1), range(col, self.__N)):
            if self.__board[i][j]:
                return False
        return True

    def solve_nqueens(self, row: int = 0) -> None:
        if row == self.__N:
            self.solutions.append([[i, row.index(True)] for i, row in enumerate(self.__board)])
            return
        for col in range(self.__N):
            if self.is_safe(row, col):
                self.__board[row][col] = True
                self.solve_nqueens(row + 1)
                self.__board[row][col] = False  # Backtrack

    def get_solutions(self):
        return self.solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    engine = QueensChessEngine(N)
    engine.solve_nqueens()

    for solution in engine.get_solutions():
        print(solution)
