"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
f = open('my_file.txt', 'w') #  Открыть на запись. При этом удалить содержимое файла. Если файл не существует, создать новый.
line = input('Введите текст \n')
while line:
    f.writelines(line)
    line = input('Введите текст \n')
    print(line)
    if not line:
        break
f.close()
f = open('my_file.txt', 'r')
content = f.readlines()

print(content)
f.close()
