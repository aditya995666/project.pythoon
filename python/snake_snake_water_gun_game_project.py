#import function
import random
def snake_water_gun(computer,turn):
    if computer==turn:
        return None
    # retuer nune means match is drie:
    elif computer=="s":
        if turn=="w":
            return False
        elif turn=="g":
            return True
    elif computer=="w":
        if turn=="g":
            return False
        elif turn=="s":
            return True
    elif computer=="g":
        if turn=="s":
            return False
        elif turn=="w":
            return True

# two players you & turn:

# computer turn in game:
computer=input("computer turn:snake (s),water(w),gun(g)?")
random_no=random.randint(1,3)
#   snake in random_no :
if random_no==1:  
    computer ="s"
    # water in random_no 2 
elif random_no==2:
    computer="w"
    # 3 random_no is gun:
elif random_no==3:
    computer="g"
# your turn in game:
# turn=you:
turn=input("players turn:snake(s),water(w),gun(g)?")
a=snake_water_gun(computer,turn)
if a==None: #the game is grie:
    print("the game is drie")
elif a:    #you  game is winner:
    print("you win")
else:  # you loos in game:
    print("you loose") 



