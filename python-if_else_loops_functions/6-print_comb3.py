#!/usr/bin/python3
for n in range(10):
    for m in range(n + 1, 10):
        print("{}{}".format(n, m),
              end=", " if format("{}{}".format(n, m)) != "89" else "\n")
