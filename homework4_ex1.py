while True:
    print('To exit of the app, enter: quit')
    num1 = input("Enter the first number: ")
    if num1 == "quit":
        print("End")
        break
    symbol = input("Enter the math symbol: ")
    if symbol == "quit":
        print("End")
        break
    num2 = input("Enter the second number: ")
    if num2 == "quit":
        print("End")
        break
    if symbol == "-":
        print(int(num1) - int(num2))
    elif symbol == "+":
        print(int(num1) + int(num2))
    elif symbol == "*":
        print(int(num1) * int(num2))
    elif symbol == "/":
        if int(num2) == 0:
            print("You can't divide by zero, but I won't tell anyone ;)")
        else:
            print(int(num1) / int(num2))
