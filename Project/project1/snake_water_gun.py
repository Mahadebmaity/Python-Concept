# We all have played snake, water gun game in our childhood. 
# If you haven’t, google the rules of this game and
#  write a python program capable of playing this game with the user.
'''
snake is a  1 
water is a  -1
gun is a  0

'''
# this is normal code formate 
import random
computer = random.choice([-1,1,0])
print("Start to play Snake-Water-gun Game->")
youstr = input("Enter your choice!(like:s,w,g): ").lower()
youDict = {"s": 1 , "w": -1, "g": 0}
reverseDict = {1:"Snake", -1:"Water",0:"Gun"}
 #high priority of this  point - (0 > 1 > -1) that means (Gun > Snake > Water)
if youstr in youDict:
    you = youDict[youstr]
    print(f"you chose {reverseDict[you]} \ncomputer chose {reverseDict[computer]}")
    if computer == you:
        print("it's a Draw!")
    else:
        if computer == -1 and you == 1:
            print("You Win!")
        elif computer == -1 and you == 0:
            print("You loss!")
        elif computer == 1 and you == -1:
            print("You loss!")
        elif computer == 1 and you == 0:
            print("You Win!")
        elif computer == 0 and you == -1:
            print("You Win!")
        elif computer == 0 and you == 1:
            print("You loss!")
else:
    print("your input is wrong! check it!")
    
