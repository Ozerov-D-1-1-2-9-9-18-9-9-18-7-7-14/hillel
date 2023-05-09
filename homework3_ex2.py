word = input("Enter 3 word in the format 'snake_case':")
word1 = word.split('_', maxsplit=-1)
word2 = word1[0].capitalize() + word1[1].capitalize() + word1[2].capitalize()
print(word2)

