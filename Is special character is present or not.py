s=input()
l=len(s)
c=0
for i in range(l):
    if((s[i].isalpha() or s[i].isnumeric() or s[i]==" ")==0):
        print("YES")
        c=1
        break        
if(c==0):        
    print("NO")
        
