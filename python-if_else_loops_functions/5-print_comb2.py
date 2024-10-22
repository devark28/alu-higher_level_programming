#!/usr/bin/python3
for n in range(99 + 1):
    print("{}".format(str(n).zfill(2)), end=(", " if n < 99 else "\n"))
