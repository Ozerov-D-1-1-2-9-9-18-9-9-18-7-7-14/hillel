num1 = int(input("Enter the height of the triangle: "))

for num2 in range(num1):
   spaces = num1 - num2 - 1
   simbol = 2 * num2 + 1
   print(" " * spaces + "*" * simbol)
