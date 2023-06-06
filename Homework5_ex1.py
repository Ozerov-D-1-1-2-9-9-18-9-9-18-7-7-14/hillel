import string


letters = string.ascii_letters
start, end = input('Введите две буквы, разделенные "-" ').split('-')

start_letter = letters.index(start)
end_latter = letters.index(end)+1

for i in range(start_letter, end_latter):
    print(letters[i], end='')
