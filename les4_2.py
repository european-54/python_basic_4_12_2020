from sys import argv

if len(argv) != 7:
    print('Ошибка ввода параметров')
    exit()

params = {}

name = ''
variables = []
for param in argv[1:]:
    try:
        param = int(param)
        variables.append(param)
    except ValueError:
        name = param #  Мы должны хранить под именами списки значений
        variables = []
    if len(variables) == 2:
        params[name] = variables

print(params)
