#!/usr/bin/python3
"""
takes URL, sends request, displays X-Request-Id header
"""
from sys import argv

import requests

if __name__ == "__main__":
    url = argv[1]
    with requests.get(url) as response:
        print(response.headers.get("X-Request-Id"))
