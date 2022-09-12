#!/usr/bin/python3
def safe_function(fct, *args):
    """executes a fuction safely"""
    try:
        return fct(*args)
    except:
        print("Exception: {}".format(except), file = stderr)
        return None
