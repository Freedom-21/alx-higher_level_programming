#!/bin/bash
# send a POST request to a URL with email and subjec
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
