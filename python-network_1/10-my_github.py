#!/usr/bin/python3
"""
fetches https://api.github.com/user and displays id
"""
from sys import argv

from requests import get, auth

if __name__ == "__main__":
    url = "https://api.github.com/user"
    response = get(url, auth=auth.HTTPBasicAuth(argv[1], argv[2]))
    print(response.json().get("id"))
