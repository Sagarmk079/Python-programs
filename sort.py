x = input()
num = list(map(int, x.split()))
l=len(num)
dl=l
for z in range(1,l+1):
  num.append(9999);
nl=len(num)

c=0;
for i in range(0,l):
  for j in range(i+1,nl):
    if(num[i]>num[j]):
      num[dl]=num[i];
      dl=dl+1
      c=c+1
      break

      
      
if(min(num)==num[l-1]):
    c=c+1
print(c)
print(num)      
      

      
      