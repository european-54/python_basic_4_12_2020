"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def div(*args):

    try:
        arg1 = int(input("Введите числитель "))
        arg2 = int(input("Введите знаменатель "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Делить на ноль нельзя!"

    return res


#   if arg2 != 0:
#       return arg1 / arg2
#   else:
#       print("Ошибка ! Делитель не может быть равен нулю")



print(f'result  {div()}')
