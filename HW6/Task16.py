init_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min = int(input('min = '))
max = int(input('max = '))
res = list(filter(lambda x: min < x < max, init_list))
print(res)