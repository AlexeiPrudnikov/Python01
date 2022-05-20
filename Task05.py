print('==========Задача № 5==========')
print('Напишите программу, котораря принимает на вход координаты точки (X, Y) и возвращает номер четверти')
def Get2DLength(x, y):
     if len(x) != 2 or len(y) != 2:
         raise ValueError
     return ((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2) ** 0.5
x = []
y = []
try:
    for i in range(2):
        x.append(int(input(f'Введите координату X {i + 1}-й точки: ')))
        y.append(int(input(f'Введите координату y {i + 1}-й точки: ')))
    print(round(Get2DLength(x, y), 3))
except ValueError:
    print('Ошибка ввода')
