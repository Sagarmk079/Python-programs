import math
x=input()
li=list(map(int,x.split(",")))
c=50
h=30
for i in range(len(li)):
    d=li[i]
    q=math.sqrt((2*c*d)/h)
    if(i!=len(li)-1):
        print(round(q),end=",")
    else:
        print(round(q),end="")
