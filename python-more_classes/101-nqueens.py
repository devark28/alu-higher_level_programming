#!/usr/bin/python3
import sys
from typing import List

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"[{self.x}, {self.y}]"

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

class Solution:
    def solveNQueens(self, n: int) -> List[List[Point]]:
        def is_safe(board, row, col):
            # Check this row on the left side
            for i in range(col):
                if board[row][i] == 1:
                    return False

            # Check upper diagonal on the left side
            i = row
            j = col
            while i >= 0 and j >= 0:
                if board[i][j] == 1:
                    return False
                i -= 1
                j -= 1

            # Check lower diagonal on the left side
            i = row
            j = col
            while i < n and j >= 0:
                if board[i][j] == 1:
                    return False
                i += 1
                j -= 1

            return True

        def solve_n_queens(n):
            board = [[0 for _ in range(n)] for _ in range(n)]
            solutions = []
            stack = []

            col = 0
            row = 0
            while col < n:
                while row < n:
                    if is_safe(board, row, col):
                        board[row][col] = 1
                        stack.append(Point(row, col))
                        row = 0
                        col += 1
                        break
                    row += 1

                if row == n:
                    if not stack:
                        return solutions
                    stack.pop()
                    row = stack[-1].x if stack else 0
                    col = stack[-1].y + 1 if stack else 0

                if col == n:
                    solutions.append([point for point in stack])
                    if stack:
                        stack.pop()
                        row = stack[-1].x if stack else 0
                        col = stack[-1].y + 1 if stack else 0

            print(board)
            print(solutions)

            return solutions

        return solve_n_queens(n)

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

    solution = Solution()
    result = solution.solveNQueens(N)

    if result:
        print(f"Number of solutions: {len(result)}")
        for i, positions in enumerate(result):
            print(f"Solution {i+1}: {positions}")
    else:
        print("No solution found")