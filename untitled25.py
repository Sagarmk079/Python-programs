s=input().lower()
li=[]
for i in range(len(s)):
    li.append(s[i])
    
for i in range(len(li)):
    if(li[i]=="."):
        li[i]=li[len(li)-1-i]
        
rev_li=li[::-1]       
if(li==rev_li):
    for i in range(len(li)):
        if(li[i]=="."):
            li[i]="a";
    print("".join(li))
else:
    print(-1)

