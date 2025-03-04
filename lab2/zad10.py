def group_words_by_length(words: list[str]):
    grouped_words = dict()
    for word in words:
        length = len(word)
        if length not in grouped_words:
            grouped_words[length] = []
        grouped_words[length].append(word)
    return grouped_words

words = ["kot", "pies", "dom", "drzewo", "las", "sowa", "krzak"]
print(group_words_by_length(words))
