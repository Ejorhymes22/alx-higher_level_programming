def magic_calculation(a, b, c):
    """does exactly the same as a bytecode given"""
    if a < b:
        return c
    if c > b:
        return a + b
    return a * b - c
