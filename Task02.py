print('==========Задача № 2==========')
print('Напишите программу для проверки истинности утверждения -(X v Y V Z) = -X /\\ -Y /\\ -Z')
print()
print(f'X\t\tY\t\tZ\t\t-(X v Y V Z)\t-X /\\ -Y /\\ -Z\t-(X v Y V Z) = -X /\\ -Y /\\ -Z')
for x in False, True:
    for y in False, True:
        for z in False, True:
            print(f'{x}\t{y}\t{z}\t{not(x or y or z)}\t\t\t{not(x) and not(y) and not(z)}\t\t\t{(not(x or y or z)) == (not(x) and not(y) and not(z))}')