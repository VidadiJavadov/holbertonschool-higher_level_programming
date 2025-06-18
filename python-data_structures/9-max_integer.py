def max_integer(my_list=[]):
    if not my_list:
        return None
    max = my_list[0]
    for el in my_list:
        if(max < el):
            max = el
    return max

print(max_integer([]))
