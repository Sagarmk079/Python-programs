n=int(input())
a=[]
for i in range(n):
  l=[]
  x = input()
  l= list(map(int, x.split()))
  a.append(l)

print(x.split())
print(l)

    

for i in range(n):
    for j in range(i):
        a[i][j]=0


for i in range(n):
    for j in range(n):
        if(j<n-1):
            print(a[i][j],end=" ")
        else:
            print(a[i][j],end="")
    if(i<n-1):
        print();