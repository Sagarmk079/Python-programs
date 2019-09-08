m,n=input().split()
m=int(m)
n=int(n)
a=[]
for i in range(m):
    x = input()
    l= list(map(int, x.split()))
    a.append(l);

c=0
for i in range(m):
    for j in range(n):
        if(a[i][j]!=0 and a[i][j]!=1):
            c=1
if(c==0):
    print("YES",end="")
else:
    print("NO",end="")