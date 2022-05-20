print('==========Задача № 4==========')
print('Напишите программу, котораря принимает на вход координаты точки (X, Y) и возвращает номер четверти')
def GetCoordinats(number):
    if number == 1: return 'X > 0, Y > 0'
    if number == 2: return 'X < 0, Y > 0'
    if number == 3: return 'X < 0, Y < 0'
    if number == 4: return 'X > 0, Y < 0'
    return 'Четверти с заданным номером не существует'
try:
    quater = int(input('Введите номер четверти: '))
    print(GetCoordinats(quater))
except ValueError:
    print('Ошибка ввода')
