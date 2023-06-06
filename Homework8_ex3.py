sentence = 'A man, a plan, a canal: Panama'


def is_palindrome(sentence):
    lst = ['.', ",", '!', '?', ';', ':', ' ']
    for element in lst:
        sentence = sentence.replace(element, "")
    sentence = sentence.lower()
    return sentence == sentence[::-1]


print(is_palindrome(sentence))
