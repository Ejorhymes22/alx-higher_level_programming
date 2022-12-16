#!/usr/bin/env python3
""" fetches from a url url is intranet
"""

from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        html = res.read()

    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
    if res.headers.get_content_charset() == 'utf-8':
        print('\t- utf8 content: OK')
