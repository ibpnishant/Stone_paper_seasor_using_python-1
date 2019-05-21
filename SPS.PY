import random
list=["stone","paper","seasor"]
cpu_score=0 
user_score=0 
i=1
n=int(input("enter no of times you want to play\n"))
while i<=n:
    cpu_choice=random.choice(list)
    user_choice=input("Please choose from - stone-paper-seasor\n")
    if cpu_choice==user_choice:
        print("tie")
    elif cpu_choice=='stone' and user_choice=='paper':
        print("user wins\n")
        user_score=user_score+1
    elif cpu_choice=='stone' and user_choice=='seasor':
        print("cpu wins\n")
        cpu_score=cpu_score+1 
    elif cpu_choice=='paper' and user_choice=='stone':
        print("cpu wins\n")
        cpu_score=cpu_score+1 
    elif cpu_choice=='paper' and user_choice=='seasor':
        print("user wins\n")
        user_score=user_score+1
    elif cpu_choice=='seasor' and user_choice=='stone':
        print("user wins\n")
        user_score=user_score+1 
    elif cpu_choice=='seasor' and user_choice=='paper':
        print("cpu wins\n")
        cpu_score=cpu_score+1
    else:
        print("YOU HAVE CHOOSEN WRONG INPUT")
    i=i+1
print("user_score=",user_score)
print("cpu_score=",cpu_score)
if cpu_score>user_score:
    print("cpu wins")
elif cpu_score==user_score:
    print("tie")
else:
    print("user wins")
