#!/usr/bin/python3
import sys

def print_solutions(solutions):
    """
    Print the solutions of the N-Queens problem
    """
    for solution in solutions:
        print(solution)

def is_safe(board, row, col):
    """
    Check if a queen can be placed in a given position
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n, row=0, board=[]):
    """
    Solve the N-Queens problem
    """
    if row == n:
        solutions.append(board.copy())
        return
    
    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            solve_n_queens(n, row + 1, board)
            board.pop()

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

    solutions = []
    solve_n_queens(N)
    print_solutions(solutions)
