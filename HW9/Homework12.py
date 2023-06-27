def difference(*args: [int, float]) -> [int, float]:
    if not args:
        return 0
    else:
        min_element = min(args)
        max_element = max(args)
        return max_element - min_element


print(difference(1, 2, 3, 4))

