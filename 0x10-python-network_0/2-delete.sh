#!/bin/bash
# send a DELETE request to the URL passed as the first argument, display response
curl -sX DELETE "$1"
