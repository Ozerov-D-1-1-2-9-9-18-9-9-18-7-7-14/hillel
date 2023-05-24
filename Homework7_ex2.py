sentence = input('Enter a sentence for correction:')
sentence = sentence.strip()


def correct_sentence(sentence):
    if not sentence.endswith('.'):
        sentence += '.'
    new_sentence = sentence[0].upper() + sentence[1:]
    return new_sentence


new_sentence = correct_sentence(sentence)
print(new_sentence)
