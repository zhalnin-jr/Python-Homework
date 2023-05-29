num= int(input("enter num:"))
count_eagle=0
count_tail=0
print("input 0 or 1, where 0 = eagle, 0 = tail")
for i in range(num):
    coin = int(input())
    if coin == 0:
        count_eagle += 1
    else:
        count_tail += 1
if count_eagle <= count_tail:
    print('You need turn over', count_eagle, 'coins')
else:
    print('You need turn over', count_tail, 'coins')
