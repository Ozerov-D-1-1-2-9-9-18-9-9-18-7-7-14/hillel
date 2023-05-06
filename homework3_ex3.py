name = input('Enter name: ')
born = int(input('Enter year of birth: '))
death = int(input('Enter year of death: '))

age = death - born

if age <= 0:
    print('Error! Please, enter correct data')
else:
    print('Name:', name)
    print('Age:', age)

