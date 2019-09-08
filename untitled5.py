n=int(input())
l=[]
for i in range (n):
    x=input();
    li=list(map(int,x.split()))
    l.append(li)
print(l)

   
k=0
l=0
m=n

while(k<m or l<n):
    for i in range(l,n):
        print(l[k][i],end=" ");
    k=k+1
    
    for i in range(k,m):
        print(l[i][n-1],end=" ")
    n=n-1
    
    if(k<m):
        for i in range(n-1,l-1,-1):
            print(l[m-1][i],end=" ")
        m=m-1
    
    if(l<n):
        for i in range(m-1,k-1,-1):
            print(l[i][l],end=" ")
        l=l+1
            
            
    
    
