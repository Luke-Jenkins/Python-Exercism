def is_isogram(string):
    string = sorted(string.lower())

    for i, letter in enumerate(string):
        if i == 0:
            pass
        elif letter == string[i - 1] and letter.isalpha() is True:
            return False

    return True
