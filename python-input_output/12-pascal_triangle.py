#!/usr/bin/python3
"""Print Pascal's Triangle."""


def pascal_triangle(n):
    """Print Pascal's Triangle."""
    row = []
    if n <= 0:
        return row
    column = []
    for i in range(0, n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(column[i - 1][j - 1] + column[i - 1][j])
            row.append(1)
        column.append(row)
    return column

# if __name__ == "__main__":
#     print(pascal_triangle(5))
