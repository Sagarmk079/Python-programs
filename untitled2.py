def index(p,q):
    ind=p*n+q
    return int(ind)

def position(num,p,q):
    if(num==(n*n+1)):
        return 0
    p=p-1;
    q=q+1;
    if(p==-1 and q==n):
        p=0;
        q=n-2;
    elif(p==-1 and q!=n):
        p=n-1;
    elif(p!=-1 and q==n):
        q=0;
    
    while(1):
        ind=index(p,q);
        if(magic_squre[ind]=="-"):
            magic_squre[ind]=num
            break;
        else:
            p=p+1;
            q=q-2;
    
    position(num+1,p,q)
    
            
    
    


while(1):
    n=int(input("Please enter odd number"));
    if(n%2==1):
        break;

magic_squre=[]
for i in range(n):
    for j in range(n):
        magic_squre.append("-")
print(magic_squre)
num=1
p=int(n/2)
q=n-1
ind=index(p,q)
magic_squre[ind]=num
position(num+1,p,q)
for i  in range(n*n):
    if(i%3==0):
        print();
    print(magic_squre[i],end=" ")
        
