def pow(num):
    return num**2

def some_gen(begin , end , func):
    x = 0
    while x < end:
        yield begin
        begin = func(begin)
        x += 1

print(list(some_gen(2, 4, pow)))