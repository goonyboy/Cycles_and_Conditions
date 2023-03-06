# 4
# Ввести с клавиатуры номер месяца. Определить сезон в зависимости от номера месяца и вывести сообщение:

# «Весна» для 3, 4, 5 месяцев;
# «Лето» для 6, 7, 8 месяцев;
# «Осень» для 9, 10, 11 месяцев;
# «Зима» для 12, 1, 2 месяцев.

month = int(input('Введите номер месяца: '))

# Плохой код
if month == 3 or month == 4 or month == 5:
    print('Весна')
elif month == 6 or month == 7 or month == 8:
    print('Лето')
elif month == 9 or month == 10 or month == 11:
    print('Осень')
else:
    print('Зима')

# Хороший код
if month in [3, 4, 5]:
    print('Весна')
elif month in [6, 7, 8]:
    print('Лето')
elif month in [9, 10, 11]:
    print('Осень')
else:
    print('Зима')
