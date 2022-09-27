#!/usr/bin/python3
"""
creats obj from jsonfile
"""


def load_from_json_file(filename):
    """creats obj from
    JSON file
    Args:
        filename: the file
    """
    import json
    with open(filename, 'r', encoding='utf-8') as f:
         return json.load(f)
