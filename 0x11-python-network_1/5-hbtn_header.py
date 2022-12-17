#!/usr/bin/python3
"""displays the value of a variable
"""

import sys
import requests

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
