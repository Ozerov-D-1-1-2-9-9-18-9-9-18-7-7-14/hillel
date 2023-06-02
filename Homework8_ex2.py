def add_one(lst):
    str_list = ''.join(map(str, lst))
    int_list = int(str_list)
    int_list += 1
    int_list = str(int_list)
    result = [int(digit) for digit in int_list]
    print(result)


add_one([1, 9, 9, 7])
