#!/usr/bin/python3
"""
takes letter, sends POST request with letter, displays body of response
"""
from sys import argv

from requests import JSONDecodeError, post

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = ""
    if len(argv) > 1:
        letter = argv[1]
    data = {"q": letter}
    response = post(url, data=data)

    try:
        """
        If the JSON is empty, print No result
        """
        json = response.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except JSONDecodeError:
        """
        If the JSON is invalid, print Not a valid JSON
        """
        print("Not a valid JSON")
