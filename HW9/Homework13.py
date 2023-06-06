def popular_words(text, array_of_words: [str, list]) -> dict:
    text = text.lower()
    word_used = {}
    for word in array_of_words:
        word_used[word] = text.count(word)
    return word_used


print(popular_words('''When I wAs One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))
