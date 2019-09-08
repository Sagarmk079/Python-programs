n=int(input())
a=[]
k=0
for i in range(n):
    l=input().split();
    a.append(l)
for i in range(n):
    for j in range(n):
        if(a[i][j]!=a[j][i]):
            k=1
if(k==0):
    print("YES")
else:
    print("NO")
            