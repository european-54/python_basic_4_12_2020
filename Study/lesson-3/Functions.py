"""
Функции дают возможность следовать принципу DRY(сухой, не повторяй себя).
А это значит, если у нас есть какой-то кусок кода, который повторяется в программе неоднократно, надо
это сжать до функции.Как же мы объявляем функцию - используем ключевое слово def(определить имя).
Задача:
Необходимо напечатать на экране YES, NO, если переданное число(ЦЕЛОЕ) имеет 3 цифры.Делением на 100 проверяем
сколько сотен в числе.
"""
def is_some(number: int, count: int)-> bool:
    """
    Документация первой строкой пишется, создаётся комментарий.Функция возвращает является ли число n разрядным
    :param number: int: число
    :param count: штеЖ количество цифр в числе
    :return: bool
    """
    return 1 <= (number // 10 ** (count -1)) < 10   #   идёт возврат значения, оно высчитывается и возвращается
#  Магия от Питона. Представим,что есть переменная, кот. явл. словарём
a = {
    'count': 5,
    'number': 23456,
}

#  print(is_some(a))  Что делать,чтоб данные правильно ушли внутрь функции? При этой записи не получится. Можно так:
#  print(is_some(a['number'], a['count'])) А вот магия: print(is_some(**a)) При ** порядок не имеет значения.Эти **
#  символы для словарей.

a: bool = is_some(123.3) #  bool это указание аннотации типов.Аннотации помогают увидеть не ошиблись ли вы где-то.Анота
#  ции не обязательны.Анотация-это то, что вы ожидаете, но не обязательно то, что к вам пришло. Это правила хорошего
#  тона.Когда делаешь анотацию, а пользователь туда передал что-то другое, то это уже его проблемы.
b = is_some(123.4)
c = is_some(12.5)
d = is_some(123456.6)

print(any((a, b, c, d))) #  А как проверить хотя бы один из них any.

#  Проверим, что значения функции являются True или False. Для этого есть All. All ознаает, что все объекты,
#  внутри переданного интерированного объекта должны быть истиной.
    #  как нам понять, что число состоит из 3-х цифр(у числа нет len)
    #  В консоли определяем:a = 123
    # a // 100 > 0
    # True
    # a = 1234
    # a // 100 > 0
    # True
    # 1 <= (a // 100) < 10
    # False
    # a = 123
    # 1 <= (a // 100) < 10
    # True

"""
Ключевое слово def определяет функцию.Далее указывается имя функции по тем же правилам,что и имя переменной.
Далее в круглых скобках, может быть, а может и не быть, мы указываем аргументы, которые может принимать функция.
Аргументов может не быть, можно указать пустые скобки.Оаределение заканчивается двоеточием. После двоеточия мы указыва-
ем тело нашей функции. Данная функция у нас реализует определённую логику, она ничего не возвращает, то есть никакого
результата действий она не возвращает.Print это не результат работы функции, это её работа, её тело, то есть то,что
она вернула.Далее идёт то, каким образом мы можем её применять(some). Данная функция не совсем красивая, есть функции
 которые начинаются с is_. Далее у нас будет передаваться число и count(количество знаков которых оно принадлежит).
 Функция, которая начинается со знака is должна проверять.Данных, которые должна вернуть функция будет булевое.
 Мы после двоеточия указываем тип данных, которые принимает. Int можно не указывать, но лучше всё-же указывать, так как
 тогда при наведении курсора будет появляться окно, в котором видно, что это функция. При наведении на int будет ука-
 зываться, что будет возвращать функция. В данном случае, булевое.Ключевое слово return возвращает некий результат за 
 пределы нашей функции. То, что возвращает функция может быть присвоено переменной.В Python есть автодокументация, 
 нужно лишь навести курсор на функцию.
"""
#  Можно сделать и так:
print(is_some.__doc__)

#  и так:
print(int.__doc__)

#  или:
print(list.__doc__)

#  Поговорим о том, что такое позиционная передача данных и именованная передача данных.
print(is_some(234.2)) #  Передаю данные позиционно, последовательность важна!
print(is_some(count=2, number=5)) #  Передача именованная, последовательность не важна!
print(is_some(number=5, count=2)) #  В этом случае можно и так записать
#  При передаче аргументов(number=5) пробел между операторами не ставится, именно когда именованно