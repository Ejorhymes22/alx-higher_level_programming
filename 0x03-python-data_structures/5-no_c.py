def no_c(my_string):
    """function that removes all characters c and C from a string"""
    m = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            m += i
    return m
