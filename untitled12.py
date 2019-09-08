name1=list(input("enter 1st name"))
name2=list(input("enter 2nd name"))
count=0
c=0
for i in range(len(name1)):
    for j in range(len(name2)):
        if(name1[i]==name2[j]):
            name1[i]="-";
            name2[j]="-";
            c=c+1
            break;
    

count=len(name1)+len(name2)-2*c
print("count=",count)
#print("a[-1]=",name1[-1])
            



li=['f','l','a','m','e','s']

ind=count-1;
ind=ind%len(li)
while(len(li)!=1):
    #print("ind",ind)
    ele=li.pop(ind)
    #print(ele)
    ind=ind+count-1
    ind=ind%len(li)
    
    

print(li)