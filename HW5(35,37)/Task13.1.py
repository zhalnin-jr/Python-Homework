def Prost(n):
    if n < 2:
        return False
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

num = int(input("Введите число: "))
if Prost(num):
    print("yes")
else:
    print("no")