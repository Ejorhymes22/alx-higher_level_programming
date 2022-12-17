#!/usr/bin/python3
"""sends a post request with etter parameter
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        if (r.json() == {}):
            print("No result")
        else:
            print("[{}] {}".format(r.json()['id'], r.json()['name']))
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")
