"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
a = int(input("Введите первое число : a "))
b = int(input("Введите первое число : b "))


def my_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'No / 0'
    except ValueError:
        return 'No value'


print((my_div(a, b)))





#  def exe_1_use():
#   print(exe_1((int(input('Enter first number: '))), (int(input('Enter second number: ')))))