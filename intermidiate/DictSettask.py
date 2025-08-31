# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
words = {
    "jal" : " water",
    "peyara" : "goava",
    "kola" : "banana"   
}
 
# userinputword = input("Enter a bengali word to look up its English translation: ").strip().lower()
# print("The English translation of", userinputword, "is", words[userinputword])

# Write a program to input eight numbers from the user and display all the unique numbers (once).

# bigginer way to  solve this problem using set 
"""
s = set()
input_numbers = input("Enter  number :")
s.update(int(input_numbers))
input_numbers = input("Enter  number :")
s.update(int(input_numbers))
input_numbers = input("Enter  number :")
s.update(int(input_numbers))
input_numbers = input("Enter  number :")
s.update(int(input_numbers))
input_numbers = input("Enter  number :")
s.update(int(input_numbers))
input_numbers = input("Enter  number :")
s.update(int(input_numbers))
input_numbers = input("Enter  number :")
s.update(int(input_numbers))

print("user input unique numbers are :", s)
 """

# Write a program to input eight numbers from the user and display all the unique numbers (once).
# smart way to solve this problem using List and  using set
'''
numbers = []
for i in range(8):
    number = int(input("Enter a Number : "))
    numbers.append(number)
unique_numbers = set(numbers)
print(" user input unique numbers  are :", unique_numbers )
'''

# Can we have a set with 18 (int) and '18' (str) as a value in it?
# s = set() # i can update values like this 
# s.update(18)
# s.update('18')
# print(s) # what will be the output 
# s = {18, '18'} # i can take  value like this 
# Yes, we can have both 18 (int) and '18' (str) as values in a set because they are of different types.

# What will be the length of following set s:
'''
s = set() 
s.update(20) 
s.update(20.0)  
s.update('20') # length of s after these operations?
print(len(s))
print(s) # Here, int 20 and float 20.0 are considered equal, so they will not be counted as separate elements in the set. The string '20' is a different type, so it will be counted as a separate element. Therefore, the length of the set will be 2.
'''

# what is the type os s 
# s ={ 12,23 ,23}
# print(type(s))  # The type of s will be <class 'dict'> because it is an empty dictionary.

# s = set()
# print(type(s))  # The type of s will be <class 'set'> because it is an empty set.

# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
# this is the first way to solve this problem
'''
dict = {}
Name = input("Enter your name: ")
Language = input("Enter your favorite language: ")
dict.update({Name : Language})
Name = input("Enter your name: ")
Language = input("Enter your favorite language: ")
dict.update( {Name: Language})
print(dict)
'''
# this is the another way to solve this problem

dict = {}
Name = input("Enter your name: ")
Language = input("Enter your favorite language: ")
dict[Name] = Language
Name = input("Enter your name: ")
Language = input("Enter your favorite language: ")
dict[Name] = Language
print(dict)


# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
# this is sort way but not actual 
# dict = {}
# dict.update({"Mahadeb": "Bengali", "Sourav": "English", "Suman": "Hindi"})
# print(dict)
# print ( type(dict) ) # The type of dict will be <class 'dict'> because it is a dictionary.

# If the names of 2 friends are same; what will happen to the program in problem 6? 
# If the names of two friends are the same, the second entry will overwrite the first entry in the dictionary.
# For example, if both friends enter the name "John", the second friend's favorite language will replace the first friend's favorite language in the dictionary.

# Can you change the values inside a list which is contained in set S? 
s = {8, 7, 12, "Harry", [1,2]}
print(s) 
print(type(s))  # The type of s will be <class 'set'> because it is a set containing various types of elements.
# No, you cannot change the values inside a list that is contained in a set. Sets are immutable, meaning that their elements cannot be changed once they are added. If you try to modify the list inside the set, it will raise a TypeError because lists are mutable and cannot be hashed.
