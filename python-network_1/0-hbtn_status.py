#!/usr/bin/python3
"""
Python script that fetches https://alu-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    from urllib.request import urlopen
    import sys

    with urlopen(sys.argv[1]) as re:
        header_var = re.headers.get('X-Request-Id')
        print(header_var)
