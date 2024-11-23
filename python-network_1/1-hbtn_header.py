#!/usr/bin/python3
"""
extract the response header value of X-Request-Id
"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        print(response.info().get("X-Request-Id"))
