x = input()
x=x.lower();
l = list(x)
n=len(l)
count=0
for i in range(n):
        if(l[i]=="a" or l[i]=="e" or l[i]=="i" or l[i]=="o" or l[i]=="u"):
            count += 1
            if (count>=2):
                l[i]="-"
        else:
            count=0


for i in range(n):
    if(l[i]!="-"):
        print(l[i],end="")
