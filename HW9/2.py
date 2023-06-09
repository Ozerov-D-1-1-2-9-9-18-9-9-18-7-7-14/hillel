import string


def first_word(user_txt: str) -> string:
    punctuation = string.punctuation
    for p in punctuation:
        if p != "'":
            user_txt = user_txt.replace(p, " ")
    user_txt += " "

    user_txt = user_txt.split()
    return user_txt[0]


print(first_word("It's amazing"))
