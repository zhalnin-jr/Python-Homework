def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a + 1, b - 1)
a = int(input('Введите число А: '))
b = int(input('Введите число В: '))
print('Сумма двух чисел А и В =', sum(a, b))