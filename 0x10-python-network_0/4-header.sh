#!/bin/bash
# send a GET request to a URL with header variable X-School-User-Id set to 98
curl -sH "X-School-User-Id: 98" "$1"
