#!/usr/bin/python3
"""
Send a POST request URL and prints the response body
"""
from sys import argv
from urllib import error, request

if __name__ == "__main__":
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code:", e.code)
