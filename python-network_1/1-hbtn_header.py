#!/usr/bin/python3
"""
extract the response header value of X-Request-Id
"""
from sys import argv
from urllib import request

if __name__ == "__main__":
    url = argv[1]
    with request.urlopen(url) as response:
        print(response.info().get("X-Request-Id"))
