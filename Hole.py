x=input()
x.upper()
count=0
for i in range(len(x)):
    if(x[i]=="A" or x[i]=="D" or x[i]=="O" or x[i]=="P" or x[i]=="R"):
        count=count+1
    elif(x[i]=="B"):
        count=count+2
        
print(count)
        


