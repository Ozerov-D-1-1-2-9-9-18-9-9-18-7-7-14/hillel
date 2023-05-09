name = input('Enter name: ')
list1 = name.split('*',)
list2 = list1[1].split('-', )
list3 = list1[2].split('-',)
year_of_birth = int(list2[0])
year_of_death = int(list3[0])

age = year_of_death - year_of_birth

if age <= 0:
    print('Error! Please, enter correct data')
else:
    print('Name:', list1[0])
    print('Age:', age)

