#!/usr/bin/python3
""" displays the value of X-Request-id
"""

import sys
from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen(sys.argv[1]) as res:
        var = res.getheader('X-Request-Id')

    print(var)
