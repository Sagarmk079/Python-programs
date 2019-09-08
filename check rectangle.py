t=int(input())
li=[]
l=[]
for i in range(t):
    l=list(map(int,input().split()))
    l=sorted(l)
    li.append(l)
    
for i in range(t):
    if(li[i][0]==li[i][1] and li[i][2]==li[i][3]):
        if(i!=t-1):
            print("YES")
        else:
            print("YES",end="")
    else:
        if(i!=t-1):
            print("NO")
        else:
            print("NO  ",end="")
        
    