print('==========Задача № 3==========')
print('Напишите программу, котораря принимает на вход координаты точки (X, Y) и возвращает номер четверти')


def GetQuoter(x, y):
    if x == 0 and y != 0: return 'Точка на оси Y'
    if x != 0 and y == 0: return 'Точка на оси X'
    if x == 0 and y == 0: return 'Точка совпадает с началом координат'
    if x > 0:
        if y > 0:
            return '1 четверть'
        else:
            return '4 четверть'
    else:
        if y > 0:
            return '2 четверть'
        else:
            return '3 четверть'
    return ''


try:
    x = int(input('Введите координату X: '))
    y = int(input('Введите координату y: '))
    print(GetQuoter(x, y))
except ValueError:
    print('Ошибка ввода')
