# Write a program to find the greatest of four numbers entered by the user.

user_input1 = int(input("Enter the first number: "))
user_input2 = int(input("Enter the second number: "))
user_input3 = int(input("Enter the third number: "))
user_input4 = int(input("Enter the fourth number: "))

if( user_input1 > user_input2 and 
    user_input1 > user_input3 and 
    user_input1 > user_input4):
    print(f"{user_input1} is the largest.")
elif(user_input2 > user_input3 and 
     user_input2 > user_input4):
    print(f"{user_input2} is the largest.")
elif(user_input3 > user_input4):
    print(f"{user_input3} is the largest.")
else:
    print(f"{user_input4} is the largest.")

