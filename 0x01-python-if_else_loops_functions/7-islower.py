def islower(c):
    for i in range(ord('a'), ord('z')):
        if chr(i) == c:
            return True
    return False
