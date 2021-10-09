import string


def my_cipher():
    alphabet = string.ascii_lowercase
    strin = input()
    for i in strin:
        result = alphabet[str(i) + 1]


def my_index():
    stri = input()
    el = input()

    for i, value in enumerate(stri):
        if value == el:
            el = i
    print(el)
