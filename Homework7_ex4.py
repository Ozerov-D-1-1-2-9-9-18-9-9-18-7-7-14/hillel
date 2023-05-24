import random


def common_elements(n1, n2):
    list_3 = [i for i in range(3, n1 * 3 + 1, 3)]
    list_5 = [i for i in range(5, n2 * 5 + 1, 5)]

    set_3 = set(list_3)
    set_5 = set(list_5)

    print(set_3)
    print(set_5)

    common_set = set_3.intersection(set_5)
    return common_set


n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))


print(common_elements(n1, n2))
