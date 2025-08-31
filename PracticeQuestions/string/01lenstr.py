''' 
# 1️⃣ Write a program to input a string and print its length. 
Name = input("Enter a string: ")

print("Lenth of input value is " , len(Name))

# 2️⃣ Write a program to convert a string to uppercase.
print( "convert Uppercase of the input name is : " , Name.upper())

# 3️⃣ Write a program to check if a string starts with Hello.
if Name.startswith("Hello"):   #The startswith() method checks if the string begins with the specified prefix ("Hello").
    print("The string starts with Hello")
else:
    print("The string does not start with Hello")

# 4️⃣ Write a program to replace "Python" with "Java" in a given string.

print(Name.replace(Name, "java")) # ase bhi kiya ja sakta hay aur 

input_string = "Python is a programming language."
replaced_string = input_string.replace("Python", "Java")
print("Replaced string:", replaced_string) #isme bhi kiya ja sakta hay 

# 5️⃣ Write a program to find the position of "a" in the string "Mahadeb".
print("possition of 'a' in  input string is : ", Name.find("a"))
# 6️⃣ Write a program to count how many times "a" appears in input from the user.
print("count of 'a' in input string is : ", Name.count("a")) #count() method returns the number of occurrences of a substring in the string.


# 7️⃣ Write a program that removes leading and trailing spaces from a string.
Name = "        My name   is   Mahadeb    Maity  "
print("Original string:", Name)
print("String after removing leading and trailing spaces:", Name.strip())

# if i want to removes all whitespace characters (including spaces, tabs, and newlines) from both ends of the string, we can use the `strip()` method.
replaced_string = Name.replace("  ", " ")
print("After removing white spaces ", replaced_string)

# another way to remove all white spaces from a string is to use the `re` module in Python.
import re 
no_whitespaces = re.sub(r"\s+", "", Name)
print("After removing all white spaces ", no_whitespaces)
'''

# 8️⃣ Write a program to split "one,two,three" into a list.
input_string = "one, two, three"
split_string = input_string.split(", ")
print("Split string into a list:", split_string)

# 9️⃣ Write a program to join ['apple', 'banana', 'cherry'] into a string separated by -.
string = ['apple', 'banana', 'cherry']
joined_string = '-'.join(string)
print("Joined string:", joined_string)
print(type(joined_string))  # This will show that the result is a string
print(type(string))  # This will show that the original is a list
reverse = reversed(joined_string)  #  return object value like this <reversed object at 0x000001779ED26CB0>
reverse_string = ''.join(reverse)  # so convert it into string formate 
print("Reversed string:", reverse_string)

reverse1 = reversed(string)  # return object value like this <reversed object at 0x000001779ED26CB0>
print(reverse1)
print("Reversed list:", list(reverse1))  # convert it into list formate

