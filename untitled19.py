x=input();
li=list(map(str,x.split(",")))
li=sorted(li)
for i in range(len(li)):
    if(i!=len(li)-1):
        print(li[i],end=",")
    else:
        print(li[i],end="")