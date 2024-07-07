#!/usr/bin/python3
"""A script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

If the response body is properly JSON formatted and not empty,
displays the id and name.
Otherwise:
    Displays "Not a valid JSON" if the JSON is invalid.
    Displays "No result" if the JSON is empty.
"""

import sys
import requests

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': letter}
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data=data)
    try:
        result = response.json()
        if result:
            print(f"[{result.get('id')}] {result.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
