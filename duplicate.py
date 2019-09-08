x = input()
l = list(map(int, x.split()))
new_list=[]
n=len(l)
count=0
for i in range (n):
    for j in range(i+1,n):
        if(l[i]==l[j]):
            l[j]="-"
    
for i in range(n):
    if(l[i]!="-"):
        if(i!=n-1):
            print(l[i],end=" ")
        else:
            print(l[i],end="")