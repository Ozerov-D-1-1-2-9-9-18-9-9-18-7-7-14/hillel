#1)
num1 = input('Enter the number:')
l = list(num1)
num2 = list(map(int, l))
sum_l = str(sum(num2))
print(f'The sum of the numbers is: {sum_l}')
#2)
num1 = int(input('Enter the number:'))
a = num1 % 10
b = num1 // 10
buf = b % 10
c = num1 // 100
sum_num1 = a + buf + c
print(f'The sum of the numbers is: {sum_num1}')

