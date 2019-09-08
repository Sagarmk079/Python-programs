x,y=input().split()
x=int(x)
y=int(y)
a=1
for i in range(1,x+1):
    for j in range(1,y+1):
        print(a,end=" ")
        a=a+1
    if(i!=x):
        print("");
    else:
        print(end="");
    
    
    