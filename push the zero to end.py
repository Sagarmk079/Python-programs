x=input()
li=list(map(int,x.split()))
l=len(li)
for i in range(l):
    if(li[i]==0):
        li.remove(0)
        li.append(0)
        
for i in range(len(li)):
    if(i!=len(li)-1):
        print(li[i],end=" ")
    else:
        print(li[i], end="")