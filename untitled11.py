x=input();
c=0
a=''
li=[]
for i in range(len(x)):   
    if(x[i].isnumeric()):
        a=a+x[i]
    else:
        if(x[i-1].isnumeric()):
            li.append(int(a))
            a=''
print(sorted(li))
print(max(li))
