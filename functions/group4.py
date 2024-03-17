# from math import sqrt, cos, sin
#
# # print("hi", 2, 3, 10, "jasurbeki", "medzineba", sep="\n")
#
#
# def multiply(a, b):
#     return a * b
#
#
# def divide(a, b):
#     return a / b
#
#
# def add(a, b):
#     return a + b
#
#
# def substract(a, b):
#     return a - b
#
#
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter a second number: "))
# calculate = input("What do you want calculate? (+, -, *, /): ")
#
# if calculate == "+":
#     print(add(num1, num2))
# elif calculate == "-":
#     print(substract(num1, num2))
# elif calculate == "*":
#     print(multiply(num1, num2))
# elif calculate == "/":
#     print(divide(num1, num2))
# else:
#     print("არ ვიცით მაგის გამოთვლა")
#
#
#
#
# # result = multiply(12, 31)
# # print(result)
# # print(multiply(12, 31))
#
#
# # def odd_or_even(x):
# #     if x % 2 == 1:
# #         return "Odd"
# #     elif x % 2 == 0:
# #         return "Even"
# #     else:
# #         return "It's float"
# #
# #
# # result = odd_or_even(5.2)
# # print(result)
#


# def is_even(i):
#     """თუ რიცხვი ლუწია ფუნქცია აბრუნებს მნიშვნელობას True,
#     წინააღმდეგ შემთხვევაში False"""
#     if i % 2 == 0: return True
#     else: return False
#
#
# value = is_even(4)
# print(value)
#
#
# def hello_twice():
#     print('Hello')
#     print('Hello')
# hello_twice()
#
#
# def hello_name(my_name):
#     print('Hello', my_name)
# hello_name('John')
# hello_name('Ann')
#
# def print_twice():
#     print('Hello')
#     print('Hello')
# print_twice()
#
# def average_numb(a, b):
#     res = (a+b)/2
#     return res
# x = average_numb(2,6)
# print(x)
#
# def average_numb(a, b):
#     res = (a+b)/2
#     return res
# y = 2
# z = 6
# x = average_numb(y+1,z)
# print(x)
#
# def average_numb(a=0, b=0):
#     res = (a+b)/2
#     return res
# x = average_numb()
# print(x)
# x = average_numb(2)
# print(x)
# x = average_numb(2, 8)
# print(x)
#
#
# double = lambda x: x * 2
# print(double(5))



# x = [2, 3, 4]
# res = 5 in x
# print(res)


# def favourite_fruit(fruits, fav):
#     x = fav in fruits
#     if x:
#         return fruits.index(fav)
#     else:
#         return "araa tqveni fav xili siashi sorry not sorry"
#
# fruits_list = ["grape", "apple", "melon", "banana", "strawberry"]
# fav_input = input("Enter your fav fruit: ")
#
# res = favourite_fruit(fruits_list, fav_input)
# print(res)


# def hello_twice(my_name):
#     print('Hello jasurbek')
#     print('Hello')
#     return f"hello {my_name}"
# # hello_twice()
# print(hello_twice("aleqsandre"))
#
# def hello_name(my_name):
#     # print(f"Hello {my_name}")
#     # return None
#     return f"Hello {my_name}"
#
# my_name = "zura"
# # hello_name("zura")
# print(hello_name(my_name="andria"))
# print(hello_name(my_name))
# print(hello_name('zura'))
# print(hello_name('zura'))
# print(hello_name('zura'))
# print(hello_name('zura'))
# hello_name('John')
# hello_name('Ann')
# hello_name('natia')
# hello_name('nika')
# hello_name('giorgi')



# def average_numb(a=0, b=0):
#     res = (a+b)/2
#     return res
#
# x = average_numb()
# print(x)
# x = average_numb(2)
# print(x)
# x = average_numb(2, 8)
# print(x)


def is_even(i):
    """თუ რიცხვი ლუწია ფუნქცია აბრუნებს მნიშვნელობას True,
        წინააღმდეგ შემთხვევაში False"""
    if i % 2 == 0: return True
    else: return False

# print(pow.__doc__)
print(help(is_even))
