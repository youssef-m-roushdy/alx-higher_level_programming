#!/usr/bin/python3
import urllib.request
import sys
"""
Python script that takes in a URL,
sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""


with urllib.request.urlopen(sys.argv[1]) as response:
    x_request_id = response.headers['X-Request-Id']
    print(x_request_id)
