"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте
цикл while и арифметические операции.
"""
i = input('Введите целое положительное число:')
s = str(i)
ls = list(map(int, s))
r = max(ls)
print(r)
