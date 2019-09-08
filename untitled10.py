x=input();
c=0
a=0
li=[]
for i in range(len(x)):   
    if(x[i].isnumeric()):
        a=int(x[i])+pow(10,c)*a
        print("a=",a,"x[i]=",x[i])
        c=c+1
    else:
        c=0
        li.append(a)
        a=0
print(li)
    

dsgahjkf876teusg123dsah56