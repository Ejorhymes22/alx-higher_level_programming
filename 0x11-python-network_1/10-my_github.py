#!/usr/bin/python3
"""displays my id using github api"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(username, token))
    if r.status_code == 200:
        print(r.json()['id'])
    else:
        print("None")
