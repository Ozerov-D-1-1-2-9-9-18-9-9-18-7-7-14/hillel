from math import *

#1
a = input('a: ')
b = input('b: ')
c = a

a = b
b = c

print('a =', a)
print('b =', b)

#2
a = input('a: ')
b = input('b: ')

a, b = b, a

print('a =', a)
print('b =', b)

#3
a = int(input('a: '))
b = int(input('b: '))

a = a + b
b = a - b
a = a - b

print('a =', a)
print('b =', b)

