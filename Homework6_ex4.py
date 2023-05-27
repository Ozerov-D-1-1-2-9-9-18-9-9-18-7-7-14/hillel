nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
summa = 35

pairs = []
num_set = set(nums)

for num in nums:
    complement = summa - num
    if complement in num_set:
        pairs.append((num, complement))

print(pairs)


nums = [1, 2, 3, 4, 5]
summa = 5

pairs = []
num_set = set(nums)

for num in nums:
    complement = summa - num
    if complement in num_set:
        pairs.append((num, complement))

print(pairs)
