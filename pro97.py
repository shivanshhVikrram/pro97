import random
num=random.randint(1,9)
count=0
while(count<5):
    mynum=int(input('enter your choice'))
    if (mynum==num):
        print("you won")
        break
    else:
        print("try again")    
    count=count+1  
      
