n=int(input())
x = input()
num = list(map(int, x.split()))
l=len(num)
k=int(input())
value=num[k-1];
num.sort();
print("value", value)

for i in range(l):
  if(num[i]==value):
      print(i+1)