#!/usr/bin/python3
"""this takes 2 argumernt and list 10 commit s on github
"""

import sys
import requests

if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/' + sys.argv[2] + '/'
                     + sys.argv[1] + '/commits', params={'per_page': 10})
    for item in r.json():
        print("{}: {}".format(item['sha'], item['commit']['author']['name']))
