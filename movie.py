import random
movie_list=["utrun","lucia","jakie","annabond","tagaru","yajamana","kotigobba","kgf","ramachari","rajakumara"]
r_movie=random.choice(movie_list)
r_movie=list(r_movie)
length=len(r_movie)
li=["_"]*length
count=0
print("guess the movie name");
while("_" in li):
    turn=0
    print(li);
    ch=input();
    count=count+1
    for i in range(length):
        if(ch==r_movie[i]):
            li[i]=ch;
            turn=1
    if(turn==1):
        print("'",ch,"'  is present in movie name ")
        print("Guess the next character")
    else:
        print("'",ch,"'  is not present in movie name ")
        print("Guess again")

print("you won",count)
        
        
        