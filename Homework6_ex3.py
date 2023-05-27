origin_list = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

result = {}

for key, value in origin_list:
    if key in result:
        result[key].append(value)
    else:
        result[key] = [value]

print(result)

