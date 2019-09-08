x=input();
c=0
li=[]
for i in range(len(x)):   
    if(x[i]=='@'):
        c=1
    if(c==1):
        if(x[i]=='.'):
            break;
        li.append(x[i])
        
for i in range(1,len(li)):
    print(li[i],end="")
    
    