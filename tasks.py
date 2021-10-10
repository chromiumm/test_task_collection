import string


def my_cipher():
    alphabet = string.ascii_lowercase
    strin = input()
    for i in alphabet:
        strin.find(i)
        i += 1



def my_search():
    stri = input()
    el = input()

    for i, value in enumerate(stri):
        if value == el:
            print(i)
            break
