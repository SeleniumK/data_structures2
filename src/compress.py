def string_compression(wordstring):
    word = list(wordstring)
    for i, _ in enumerate(word):
        next_letter = i + 1
        indices = []
        try:
            while word[i] == word[next_letter]:
                indices.append(next_letter)
                next_letter += 1
        except IndexError:
            pass
        if indices:
            word[i] = "{}{}".format(word[i], len(indices) + 1)
            word = word[:i + 1] + word[indices[-1] + 1:]
    return "".join(word)
