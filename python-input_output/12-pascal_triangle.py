#!/usr/bin/python3
"""Print Pascal's Triangle."""


def pascal_triangle(n):
    if n <= 0:
        return []
    # result = []
    for i in range(n):
        res = [1]
        for j in range(i):
            if j > 0:
                res.append(res[j - 1] + res[j])
        res.append(1)
        # result.append(res)
        print(res)
