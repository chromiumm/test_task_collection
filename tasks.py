import string


def my_cipher():
    input_str = input()
    result = ""
    for i in input_str:
        found_index = search_shifted(i)
        result += found_index
    print(result)


def search_shifted(char):
    alphabet = string.ascii_lowercase + "a"
    index = alphabet.find(char)
    return alphabet[index + 1]



