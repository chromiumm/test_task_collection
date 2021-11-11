import string


def search_shifted(char):
    alphabet = string.ascii_lowercase + "a"
    index = alphabet.find(char)
    return alphabet[index + 1]
