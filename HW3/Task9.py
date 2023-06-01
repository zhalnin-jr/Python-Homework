import math
n = int(input('Enter size of array: '))
array = [0]*n
print('Enter elements of array one by one via "enter" button')
for i in range(len(array)):
    array[i] = int(input('--> '))
print(array)
x = int(input('Enter number X, which we need to find closest number in array: '))
closest = array[0]
for i in range(1, len(array)):
    if abs(closest - x) > abs(array[i] - x):
        closest = array[i]
print('Closest number to', x, 'is', closest)