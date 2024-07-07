#!/usr/bin/python3
import urllib.request
import sys

""""the function takes in url, sends a request to the url
and disp the value of X-Request-Id"""

if __name__ == "__main__":
    url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    print(response.getheader('X-Request-Id'))
