#!/usr/bin/python3
"""A script that takes in a URL,
sends a request to the URL,
and displays the body of the response (decoded in utf-8).

If the HTTP status code is greater than or equal to 400,
prints: Error code: followed by the value of the HTTP status code.
"""

import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as resp:
            print(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
