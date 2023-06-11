def stepen(a , b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
       return a * stepen(a, b - 1)
a = int(input('Введите число А: '))
b = int(input('Введите число B, степень числа А: '))
print('Число А в степени В =', stepen(a, b))