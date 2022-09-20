def magic_string():
    magic_string.counter = getattr(magic_string, 'counter', 0) + 1
    n = 'BestSchool'
    return (n * magic_string.counter) if magic_string.counter == 1 else "BestSchool, " * magic_string.counter
