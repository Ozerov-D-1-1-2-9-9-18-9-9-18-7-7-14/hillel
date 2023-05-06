from art import *
from math import *
# задание 2
a=1
b=5
c=4
d = -b + sqrt((b**2)-4*a*c)
x1=d/(2*a)
print('x1 =', x1)
x2 = (-b - sqrt((b**2) - 4*(a*c)))/(2*a)
print('x2 =', x2)

# задание 3
print('Please enter your name: ')
name=input()
print('Hello,',name, end='')
print("! Use Viet's theorem in the future =)")

# задание 4
print(name,"enter the amount in hryvnia:")
cash = float(input())
usd = 36.8
my_usd = round(cash / usd, 2)
print('Now you have ', my_usd,'usd! This is not much, but more than any russian ork. \nGlory to Ukraine.')
print("***Press 'F' to pay respect***")
respect=input()
if(respect == 'F'):
    print('Glory to heroes')
elif(respect == 'f'):
    print('Glory to heroes')
else:
    print('Russian warship, go f*** your self!')
# задание 5
tprint(name,"rnd-xlarge")

#задание 6*
#1)
n1 = int(input('Введите число: '))

thousand, left = divmod(n1, 1000)
print(thousand)
hundreds, left = divmod(left, 100)
print(hundreds)
tens, left = divmod(left, 10)
print(tens)
print(left)
#2)

n2 = int(input('Введите целое пятизначное число:'))

ten_thousand, left1 = divmod(n2, 10000)
thousand, left2 = divmod(left1, 1000)
hundreds, left3 = divmod(left2, 100)
tens, left4 = divmod(left3,10)
print(left4, tens, hundreds, thousand, ten_thousand)
