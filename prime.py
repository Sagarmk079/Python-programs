import math

def checkSemiprime(num): 
    cnt = 0
  
    for i in range(2, int(math.sqrt(num)) + 1): 
        while num % i == 0: 
            num /= i 
            cnt += 1 # Increment count 
                    # of prime number 
  
        # If count is greater than 2, 
        # break loop  
        if cnt >= 2:  
            break
    # If number is greater than 1, add it to 
    # the count variable as it indicates the 
    # number remain is prime number 
    if(num > 1): 
        cnt += 1
  
    # Return '1' if count is equal to '2' else 
    # return '0'
    return cnt == 2

def dupli(i,b):
    li=[1,4,9,16,25,36,49,64,81,100,121]
    for j in range(0,10):
        if(li[j]==i or li[j]==b):

            return False
    
    return True;
        
        
        
    
    

c=0
n=int(input())
l=int((n/2)+1)
for i in range(2,l):
  value1=checkSemiprime(i)
  b=n-i
  value2=checkSemiprime(b)
  if(value1==True and value2==True and dupli(i,b)):
    print("Yes")
    c=1
    break;

if(c==0):
  print("No")