x = input()
x=x.upper();
l = list(x)
n=len(l)
new_list=[]
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_list=list(alpha)
for i in range(n):
    if(l[i]!=" "):
        new_list.append(l[i])
n=len(new_list)

count=0
for i in range(26):
    for j in range(n):
        if(alpha_list[i]==new_list[j]):
            count=count+1;
            break;

if(count==26):
    print("YES",end="")
else:
    print("NO",end="")
