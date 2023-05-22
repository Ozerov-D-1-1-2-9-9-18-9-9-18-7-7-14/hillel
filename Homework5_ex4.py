import random


n = random.randrange(3, 10)
lst = [random.randrange(1, 100) for i in range(n)]
new_list = [lst[0], lst[2], lst[-2]]

print(lst)
print(new_list)
