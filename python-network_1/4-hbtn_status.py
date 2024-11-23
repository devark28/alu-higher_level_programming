#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""
from urllib import request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        print("Body response:")
        print("\t- type:", type(response.read()))
        print("\t- content:", response.read())
