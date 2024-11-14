#!/usr/bin/python3
"""Print Pascal's Triangle."""


def pascal_triangle(n):
    """Print Pascal's Triangle."""
    if n <= 0:
        return []
    for i in range(0, n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(pascal_triangle(n - 1)[i - 1][j - 1] +
                           pascal_triangle(n - 1)[i - 1][j])
            row.append(1)
        print(" ".join(str(x) for x in row))
