def uppercase(str):
    x = ""
    y = 0
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            y = ord(i) - 32
            x += chr(y)
        else:
            x += i
    print("{}".format(x))
