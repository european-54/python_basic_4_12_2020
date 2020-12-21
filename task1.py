"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
f = open('test.txt', 'w')
line = input('Введите текст \n')
while line:
    f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

f.close()
f = open('test.txt', 'r')
content = f.readlines()
print(content)
f.close()
