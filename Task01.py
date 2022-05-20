def DayStatus(number):
    if 1 <= number <= 5: return 'Будний день'
    if 6 <= number <= 7: return 'Выходной день'
    return ('Номер дня недели должен быть от 1 до 7')
print('==========Задача № 1==========')
print('Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.')
try:
    dayNumber = int(input('Введите номер дня недели: '))
    print(DayStatus(dayNumber))
except ValueError:
    print('Введено не число')