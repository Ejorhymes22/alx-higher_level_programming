#!/usr/bin/python3
"""
script that adds all arguments
to a list
"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    list_arg = load_from_json_file("add_item.json")
except Exception:
    list_arg = []

for i in range(1, len(sys.argv)):
    list_arg.append(sys.argv[i])

filename = "add_item.json"
save_to_json_file(list_arg, filename)
