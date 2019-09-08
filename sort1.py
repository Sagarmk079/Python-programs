x = input()
num = list(map(int, x.split()))
l=len(num)
dl=l
for z in range(1,l):
  num.append(9999);
nl=len(num)

c=0;
for i in range(0,l):
  for j in range(i+1,nl):
    if(num[i]>=num[j]):
      num[l]=num[i];
      c=c+1
      break
      
      

print(c)
print(num)
      
      
      
      