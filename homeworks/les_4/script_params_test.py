from sys import argv
try:
    script_name, time, salary, bonus = argv
    print("Параметр 1: ", script_name)
    print("Параметр 2: ", time)
    print("Параметр 3: ", salary)
    print("Параметр 4: ", bonus)
    res = time * salary + bonus
    print(f'заработная плата сотрудника {res}')
except TypeError:
    print('Ошибка ввода, введите числовое значение!')
else:
    print('Успех, нет ошибок!')