import random
n = int(input("Chislo kustov: "))
grydka = g = list()
for i in range(n):
    g.append(random.randint(1,9))
print(g)
if n == 3:
    max = g[0] + g[1] + g[2]
else:
    sum1 = g[n - 1] + g[n - 2] + g[0]
    sum2 = g[n - 1] + g[0] + g[1]
    max = g[0] + g[1] + g[2]
    for i in range(3, len(g)):
        if max < g[i] + g[i - 1] + g[i - 2]:
            max = g[i] + g[i - 1] + g[i - 2]
    if sum1 > max > sum2:
        max = sum1
    elif sum2 > max > sum1:
        max = sum2
print(max)