l1st = input("Enter the list:")

if len(l1st) == 0:
    output = [[], []]
elif len(l1st) % 2 == 0:
    half_l1st = len(l1st) // 2
    output = [l1st[:half_l1st], l1st[half_l1st:]]
else:
    half_l1st = len(l1st) // 2
    output = [l1st[:half_l1st + 1], l1st[half_l1st + 1:]]

print(output)