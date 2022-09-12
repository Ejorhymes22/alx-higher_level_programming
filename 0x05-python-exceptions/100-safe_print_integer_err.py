#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    """function that prints an integer"""
    #if __name__ == "__main__":
    try:
        print("{:d}".format(value))
        return True
    except ValueError as ve:
        print("Exception: {}".format(ve), file = sys.stderr)
        return False
