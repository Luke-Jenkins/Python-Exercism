def is_isogram(string):
    string = [letter.lower() for letter in string if letter.isalpha()]
    return len(set(string)) == len(list(string))
