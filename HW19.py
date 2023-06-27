def is_prime(n: int) -> int:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_generator(limit):
    for num in range(2, limit):
        if is_prime(num):
            yield num


print(list(prime_generator(10)))
