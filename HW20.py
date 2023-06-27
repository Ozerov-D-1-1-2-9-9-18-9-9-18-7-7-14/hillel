def generate_cube_numbers(limit: int) -> list:
    num = 2
    while True:
        cube = num ** 3
        if cube >= limit:
            return
        yield cube
        num += 1


print(list(generate_cube_numbers(10)))
print(list(generate_cube_numbers(100)))
