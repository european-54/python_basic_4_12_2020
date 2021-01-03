"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные
аргументы. Реализовать вывод данных о пользователе одной строкой.
"""

name = str(input('enter name'))
surname = str(input('enter surname'))
year = int(input('enter year'))
city = str(input('enter city'))
email = str(input('enter email'))
telephone =int(input('input telephone'))


def my_func(*args):
    args = (name, surname, year, city, email, telephone)
    return args


print(my_func('name', 'surname', year, 'city', 'email', telephone))
