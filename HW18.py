def lchain(*iterables) -> list:
    result = []
    for iterable in iterables:
        result.extend(iterable)
    return result


print(lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)))
