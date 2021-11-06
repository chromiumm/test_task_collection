
# from math import pi

# a = float(input(":"))
# print((a**2)*pi)

# ----------------------------------

# s = input("введи фамилию : ")
# n = input("введи имя : ")
# print(n, s)

# ----------------------------------

# n = input("введи имя : ")
# print(n[::-1])

# ----------------------------------

# f = input("введи : ")
# s = f.split(".")
# print(s[-1])

# ----------------------------------

# a = input("введи : ")
# b = a * 2
# c = a * 3
# print(int(a) + int(b) + int(c))

# ----------------------------------

# from datetime import date
# f_date = date(2014, 7, 2) 
# l_date = date(2014, 7, 11)
# delta = l_date - f_date
# print(delta.days)

# ----------------------------------

# b = input("введи : ")
# s = "аоуыиэ"
# print("гласная") if b in s else print("согласная")

# ----------------------------------

# for i in range(20, 256):
#   print(i, bin(i), hex(i), chr(i))

# ----------------------------------

# yarik = {
#   "name": "Yarik",
#   "skill": 0.1,
#   "age": 15,
#   "humour": False,
#   "items": [1,2,3,4]
# }
# yarik["name"] = "Yaroslav"
# yarik["money"] = 100500
# print(yarik)

# ----------------------------------

# def my_sum(a, b):
#   return a + b

# c = my_sum(2, 5)

# print(c)

# ----------------------------------

# def max_of_two(a, b):
#   if a > b:
#     return a
#   return b

# def max_of_three(a, b, c):
#   return max_of_two(a, max_of_two(b, c))

# ----------------------------------

# def sum_list(lst):
#   s = 0
#   for i in lst:
#     s += i
#   return s

# ----------------------------------

# def reverse(st):
#   return st[::-1]

# ----------------------------------

# def factorial(n):
#   if n == 0:
#     return 1
#   else:
#     return n * factorial(n-1)

# print(factorial(20))

# ----------------------------------

# def right():
#   return "Right"

# def left():
#   return "Left"

# def message(lane):
#   print("turn " + lane())

# message(left)
# message(right)

# ----------------------------------

# def print_all(*args, **kwargs):
#   for item in args:
#     print(item)
#   print(kwargs)
#   for key, value in kwargs.items():
#     print(key, value)

# print_all(1, 2, "Привет", ["Яблоки", "Груши"], name="Test", age=135, icq=424665913)

# ----------------------------------

# def char_find(arg_str, char):
#   for index, item in enumerate(arg_str):
#     if item == char:
#       return index


# print(char_find("abcdefg", "f"))

# ----------------------------------
import string


def search_shifted(char):
    alphabet = string.ascii_lowercase + "a"
    index = alphabet.find(char)
    return alphabet[index + 1]


print(search_shifted("a"))
