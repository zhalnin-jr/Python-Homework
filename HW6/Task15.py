a1 = int(input('a1 = '))
n = int(input('n = '))
d = int(input('d = '))
result = []
for i in range(1, n + 1):
    result.append(a1 + (i - 1) * d)
print(result)