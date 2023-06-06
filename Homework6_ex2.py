word = input('Enter the word: ')

result = {}

for symbol in word:
    if symbol in result:
        result[symbol] += 1
    else:
        result[symbol] = 1

print(result)

