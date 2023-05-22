input_number = int(input("Please enter a number greater than zero: "))

if input_number <= 0:
    print("The entered number is not greater than zero. I see you are a rebel ;)")
else:
    product = 1
    while input_number > 9:
        digits_product = 1
        while input_number != 0:
            digit = input_number % 10
            digits_product *= digit
            input_number //= 10
        input_number = digits_product
        product = digits_product
    print("The result of multiplying the digits of a number:", product)
