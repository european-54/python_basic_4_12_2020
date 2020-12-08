user_name = input("Введите ваше имя\n>>>")
user_age = input('Введите ваш возраст>>>')  # Функция input всегда будет возвращать строку

if user_age.isdigit():  # Любая переменная типа строка имеет ряд методов. isdigit. Дословный перевод строки: возраст пользователя - цифровой
    user_age = int(user_age)
else:
    print(user_name, 'Ошибка ввода возраста, введите число')
    exit()

#   print("Добрый вечер", user_name)
sys_message = f'Пользователь {user_name} в возрасте {user_age} лет вошел в систему'
print(sys_message)

if user_age >= 18:
    print("Доступ разрешен в ХХХ")
elif user_age >= 16:
    print("Доступ к боевикам")
else:
    print("Ограниченный доступ")

print('Отсчет возраста')

temp_age = user_age
while temp_age > 0:
    if not temp_age & 1:
        temp_age -= 1
        continue
    print(temp_age)
    #if temp_age == 15:
    #    break
    #  temp_age = temp_age - 1   равнозначные строки
    temp_age -= 1
else:
    print('Сработал esle цикла')