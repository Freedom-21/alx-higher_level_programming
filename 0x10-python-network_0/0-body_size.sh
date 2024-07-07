#!/bin/bash
# the script takes a url, send request, and displays responds size
curl -s "$1" | wc -c
