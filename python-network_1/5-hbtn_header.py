#!/usr/bin/python3
"""A Python script to send request to given URL and 
display value of X-Request-Id"""

from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
