#!/usr/bin/python3
"""takes a url and sends a request to the url
"""

import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            html = res.read()
            print(html.decode())
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
