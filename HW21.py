def is_even(n: int) -> int:
    last_number = n & 1
    return last_number == 0


print(is_even(2494563894038 ** 2))
print(is_even(1056897 ** 2))
print(is_even(24945638940387 ** 3))
