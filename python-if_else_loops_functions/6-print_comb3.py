#!/usr/bin/python3
for n in range(10):
    for m in range(10):
        if (n * 10 + m) < (m * 10 + n):
            print("{}".format((n * 10 + m)), end="")
        else:
            print("{}".format((m * 10 + n)), end="")
        if (n * 10 + m) < 89 or (m * 10 + n) < 89:
            print(", ", end="")
        else:
            print()