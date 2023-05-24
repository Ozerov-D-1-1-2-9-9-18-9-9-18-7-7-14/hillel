name = input('Enter your name: ')
age = input('Enter your age: ')


def say_hi(name: str, age: int):
    return f"Hi. My name is {name} and I'm {age} years old."


greeting = say_hi(name, age)
print(greeting)
