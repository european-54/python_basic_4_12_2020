"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
 город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
 данных о пользователе одной строкой.
"""


def exe_2(**kwargs):
    return list(kwargs.values())


def exe_2_use():
    print(exe_2(name=input('Enter name: '),
                s_name=input('Enter second name: '),
                b_date=input('Enter birth day: '),
                l_town=input('Enter live town: '),
                email=input('Enter email: '),
                tel=input('Enter tel number: ')))

def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])
name = input('enter name')
surname = input('enter surname')
year = int(input('enter year'))
city = input('enter city')
email = input('enter email')
telephone = input('input telephone')

print(my_func(surname = 'Frolov', name = 'Sergey', year = '1990', city = 'Syzran', email = 'error@mail.ru', telephone = '8-903-300-99-87'))