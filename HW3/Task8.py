n = int(input('Enter size of array: '))
array = [0]*n
print('Enter elements of array one by one via "enter" button')
for i in range(len(array)):
    array[i] = int(input('--> '))
print(array)
x = int(input('Enter number X, which we need to find in array: '))
count = 0
for i in range(len(array)):
    if array[i] == x:
        count += 1
print(x, 'is found in the array', count,'times')