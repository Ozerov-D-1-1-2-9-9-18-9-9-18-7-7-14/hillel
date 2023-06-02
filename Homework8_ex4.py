from collections import Counter


def find_unique_value(my_list):
    counter = Counter(my_list)
    counted_elements = dict(counter)
    unique_number = [element for element, count in counter.items() if count == 1]
    for element in unique_number:
        print(f"The unique number is {element}")


find_unique_value([6, 6, 6, 6, 9, 6, 6])
