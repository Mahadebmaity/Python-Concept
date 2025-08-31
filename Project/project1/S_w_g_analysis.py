#  this is a same project of snake water  gun game 
#but this is a advanced way to write code 
import random
computer = random.choice([-1,1,0])
print("Start to play Snake-Water-gun Game->")
youstr = input("Enter your choice!(like:s,w,g): ").lower()
youDict = {"s": 1 , "w": -1, "g": 0}
reverseDict = {1:"Snake", -1:"Water",0:"Gun"}
 #high priority of this  point - (0 > 1 > -1) that means (Gun > Snake > Water)
# if youstr in ["s", "w", "g"]:
if youstr in youDict:
    you = youDict[youstr]
    print(f"you chose {reverseDict[you]} \ncomputer chose {reverseDict[computer]}")
    if computer == you:
        print("it's a Draw!")
    else:
        if ((computer - you) == -1 or (computer -you) == 2):
            print("you Loss!")
        else:
            print("You Win!")
else:
    print("something went wrong! \n  your input in wrong!\n   please check your input!")
