#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv
    if argv[2]:
        data_1 = {}
        data_1['email'] = argv[2]
        data_2 = parse.urlencode(data_1)
        data = data_2.encode("UTF-8")
    if argv[1]:
        req = request.Request(argv[1], data)
        with request.urlopen(req) as response:
            content = response.read()
            print(content.decode("UTF-8"))
