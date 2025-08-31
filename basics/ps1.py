# question number 1 :: Write a program to print Twinkle twinkle little star poem in python.
# print('''
#       twincle, twincle, little star,
#       how I wonder what you are!
#         Up above the world so high,
#         like a diamond in the sky.
#       Twinkle, twinkle, little star,
#         how I wonder what you are!
        
#         When the blazing sun is gone,
#         when he nothing shines upon,
#             then you show your little light,
#             twinkle, twinkle, all the night.
#         Twinkle, twinkle, little star,
#         how I wonder what you are!
        
#         Then the traveler in the dark
#         thanks you for your tiny spark;
#             he could not see which way to go,
        #     if you did not twinkle so.
        # Twinkle, twinkle, little star,
        # how I wonder what you are!
      
        # In the dark blue sky you keep,
        # and often through my curtains peep,
        #     for you never shut your eye
        #     till the sun is in the sky.
        # Twinkle, twinkle, little star,
        # how I wonder what you are!  
      
        # As your bright and tiny spark
        # lights the traveler in the dark,
        #     though I know not what you are,
        #     twinkle, twinkle, little star.
        # how I wonder what you are!
    #   ''')
# question number 2 :: Use REPL and print the table of 5 using it. 
# this is done in REPL

# question number 3 :: Install an external module and use it to perform an operation of your interest.
# This code uses the pyttsx3 library to convert text to speech.

# You can install the pyttsx3 library using pip:
# import pyttsx3
# engine = pyttsx3.init()
# engine.say(" Hello , jayanta samanta . how are you ?")
# engine.runAndWait()

# question number 4 :: Write a python program to print the contents of a directory 
# using the os module. Search online for the function which does that.

import os

# Specify the directory you want to list
directory = "C:/Users/Mahadeb Maity/OneDrive/Python/Python_programming/basics"

# Get the list of files and directories
contents = os.listdir(directory)

# Print the contents
print(f"Contents of directory '{directory}':")
for item in contents:
    print(item)


# question number 5:: Label the program written in problem 4 with comments.
# i will add comments to the code in problem 4
