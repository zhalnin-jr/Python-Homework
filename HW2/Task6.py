s=int(input('summ'))
p=int(input('X*Y'))
x=1
y=s-1
while x<=s/2:
    if x+y==s and x*y==p:
        print("x =",x)
        print("y =",y)
        break
    else:
        x+=1
        y-=1
