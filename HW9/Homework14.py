def fact(x: int) -> int:
    if x == 1 or x == 0:
        return 1
    else:
        result_fact = fact(x - 1) * x
    return result_fact


print(fact(5))

