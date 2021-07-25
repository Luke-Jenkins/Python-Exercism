def is_isogram(string):
    # converts string to array of lower alpha chars
    string = [letter.lower() for letter in string if letter.isalpha()]
    # returns boolan comparison of set(string) vs list(string)
    # set(string) returns only unique items
    # list(string) returns all items
    return len(set(string)) == len(list(string))
