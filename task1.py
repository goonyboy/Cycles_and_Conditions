# 1
# Напишите программу, которая вернет True, если указывается високосный год, иначе False.
# Например, x = 2000 -> True; x = 1900 -> False; и т.д.

year = int(input('Введите год: '))
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    print('Год ' + str(year) + ' високосный')
else:
    print('Год ' + str(year) + ' не високосный')