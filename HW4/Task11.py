n1 = int(input("Enter long 1 mas: "))
n2 = int(input("Enter long 2 mas: "))
a1 = set()
a2 = set()
for i in range(n1):
    a1.add(int(input("1  ")))
for i in range(n2):
    a2.add(int(input("2  ")))
print(a1.intersection(a2))