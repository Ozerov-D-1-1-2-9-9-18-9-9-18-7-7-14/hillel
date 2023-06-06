lst = [1, 4, 5, 6, 0, 7, 2, 0, 5, 0, 4]
new_lst = []
quantity_zeros = 0

for element in lst:
    if element != 0:
        new_lst.append(element)
    else:
        quantity_zeros += 1

new_lst.extend([0] * quantity_zeros)

print(new_lst)
