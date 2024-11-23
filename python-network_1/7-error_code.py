#!/usr/bin/python3
"""
takes URL, sends request, displays body or error code
"""
from sys import argv

import requests

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
