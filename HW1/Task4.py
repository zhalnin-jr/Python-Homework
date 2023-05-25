n = int(input('Enter n: ' ))
m = int(input('Enter m: ' ))
k = int(input('Enter k: ' ))
if k >= n * m:
    print('No')
elif k == n and k == m:
    print('Yes')
elif k % n == 0 or k % m == 0:
    print('Yes')
else:
    print('No')