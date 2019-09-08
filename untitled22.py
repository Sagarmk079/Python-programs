from itertools import permutations 
  
# Get all permutations of length 2 
# and length 2 
n,m=map(int,input().split())
x=input()
input_li=list(map(int,x.split()))
perm = permutations(input_li, m) 

li=[] 
if (m==0 or n==0): 
        print(0)
        exit(0)
    # Sort the given packets 
input_li.sort() 
  
    # Number of students cannot be more than 
    # number of packets 
if (n < m): 
    print(-1)
    exit(0)
        
    
# Print the obtained permutations 
for i in list(perm): 
    i=sorted(i)
    li.append(i[m-1]-i[0])

li=sorted(li)
print(li[0], end="")   
    
