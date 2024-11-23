#!/usr/bin/python3
"""
takes URL and email, sends POST request with email, displays body of response
"""
from sys import argv

import requests

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = {"email": email}
    response = requests.post(url, data=data)
    print(response.text)
