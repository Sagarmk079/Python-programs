import math
n,v1,v2=input().split()
n=int(n)
v1=int(v1)
v2=int(v2)
if(v1>=1 and v2<=100 and n>=1 and n<=200):
  tw=(2*math.sqrt(2*n))/v1
  tc=(2*n)/v2
  if(tw>tc):
    print("Walk",tw )
    print("Cab",tc)
  else:
    print("Cab",tc)