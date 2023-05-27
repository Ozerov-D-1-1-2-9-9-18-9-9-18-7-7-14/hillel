def second_index(string, substring):
    first_index = string.find(substring)
    if first_index == -1:
        return None  
    second_index = string.find(substring, first_index + 1)
    if second_index == -1:
        return None
    return second_index

string = input("Enter string:")
substring = input('Enter an item to search:')
second_inclusion_index = second_index(string, substring)

print(second_inclusion_index)
