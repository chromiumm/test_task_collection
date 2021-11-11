import string

from utils import search_shifted


def my_cipher():
    input_str = input()
    result = ""
    for i in input_str:
        found_index = search_shifted(i)
        result += found_index

    print(result)


def my_date():
    from datetime import date
    date11 = int(input("введи первый год"))
    date12 = int(input("введи первый месяц"))
    date13 = int(input("введи первый день"))
    date21 = int(input("введи второй год"))
    date22 = int(input("введи второй месяц"))
    date23 = int(input("введи второй день"))
    f_date = date(date11, date12, date12)
    l_date = date(date21, date22, date23)
    delta = l_date - f_date
    print(delta.days)


