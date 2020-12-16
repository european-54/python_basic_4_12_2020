from sys import argv

try:

    script_name, time, salary, bonus = argv

print("Имя скрипта: ", script_name)
print("Параметр 1: ", time)
print("Параметр 2: ", salary)
print("Параметр 2: ", bonus)

res = time * salary + bonus

print(f'заработная плата сотрудника {res}')

    except TypeError:

print('Ошибка ввода, введите числовое значение!')

    else:

print('Успех, нет ошибок!')
