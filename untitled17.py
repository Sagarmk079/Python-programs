x=int(input())
bi=input()
count=0
for i in range(x-1,-1,-1):
    if(bi[i]=='1'):
        break;
    count=count+1
print(count)
