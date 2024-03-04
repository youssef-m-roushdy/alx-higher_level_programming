#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    x_request_id = response.headers['X-Request-Id']
    print(x_request_id)
