"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
 город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
 данных о пользователе одной строкой.
"""

def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])
name = input('enter name')
surname = input('enter surname')
year = int(input('enter year'))
city = input('enter city')
email = input('enter email')
telephone = input('input telephone')

print(my_func(surname = 'Frolov', name = 'Sergey', year = '1990', city = 'Syzran', email = 'error@mail.ru', telephone = '8-903-300-99-87'))