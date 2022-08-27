def new_in_list(my_list, idx, element):
    """replaces an element in al list at a specific position
    without modifying the original list"""
    if idx < 0 or len(my_list) <= idx:
        return my_list
    m = my_list.copy()
    m[idx] = element
    return m
