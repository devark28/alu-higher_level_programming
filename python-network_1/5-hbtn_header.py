#!/usr/bin/python3
"""
takes URL, sends request, displays X-Request-Id header
"""
from sys import argv

import requests

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
