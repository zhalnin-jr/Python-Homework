def print_reverse(n):
    
    if n > 0:
        num = int(input())
        print_reverse(n-1)
        print(num, end=" ")

n = int(input())
print_reverse(n)