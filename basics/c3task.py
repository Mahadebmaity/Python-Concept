# Write a python program to display a user entered name followed by Good Afternoon using input () function.
# Name = input("please enter your name ")
# print("Good Afternoon ", Name) #i use this simple way 
# i can use f string also 
# print(f"Good Afternoon,{Name}") # this is also a good way to print the string
# Write a program to fill in a letter template given below with name and date.
letter = """ Dear <|Name|>,
             You are Selected!
             Date: <|Date|>"""
# print(letter.replace("<|Name|>", "Mahadeb").replace("<|Date|>", "12/12/2023")) #  this is perform like this but  outhers way to implement is 
#  taking a user input 
# Name = input("Enter your Name:-")
# Date = input("Enter Date of writting!, (DD-MM-YYYY)")
# print(letter.replace("<|Name|>", Name).replace("<|Date|>", Date))
# but i can generate present date and time 
# for  teking current date first import this 
from datetime import datetime
current_datetime = datetime.now()
# print(letter.replace("<|Name|>", Name).replace("<|Date|>", current_datetime.strftime("%Y-%m-%d %H:%M:%S")))

# Write a program to detect double space in a string.
Name = " My Name is  Mahadeb "  # This string contains a double space
print(Name.find("  ")) # if we find another word i can use this method
# Replace the double space from problem 3 with single spaces.
print(Name.replace("  ", " "))  # This will replace double spaces with single spaces  and this  method create a new string and return it 


# Write a program to format the following letter using escape sequence characters.
letter = "Dear Mahadeb, \n\t This python course is nice.\n Thanks!"
print(letter)  # This will print the letter with escape sequences interpreted

