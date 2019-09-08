s=input()
low=0
up=0
for i in range(len(s)):
    if(s[i].islower()):
        low=low+1
    elif(s[i].isupper()):
        up=up+1
print(up,end=" ")
print(low,end="")