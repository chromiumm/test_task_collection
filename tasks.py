import string


def my_cipher():
    alphabet = string.ascii_lowercase
    input_str = input()
    result = ""
    for i in input_str:
        found_index = alphabet.find(i)
        result += alphabet[found_index+1]
    print(result)


def my_search():
    stri = input()
    el = input()

    for i, value in enumerate(stri):
        if value == el:
            print(i)
            break
