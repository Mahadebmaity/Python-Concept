# # string function which is required for future development 
# # String functions
#     # String concatenation
# str1 = "Hello"
# str2 = "World"
# print(len(str1))  # Output: 5
# concatenated = str1 + " " + str2
# print("Concatenated String:", concatenated)  # Output: Hello World

#     # String length
# length = len(concatenated)
# print("Length of String:", length)  # Output: 11

#     # String methods
# lower_case = concatenated.lower()
# print("Lowercase:", lower_case)  # Output: hello world

# upper_case = concatenated.upper()
# print("Uppercase:", upper_case)  # Output: HELLO WORLD

# stripped = "   Hello World   ".strip()
# print("Stripped String:", stripped)  # Output: Hello World

# # replaced = concatenated.replace("World", "Python")
# # print("Replaced String:", replaced)  # Output: Hello Python

# replaced = concatenated.replace("Hello", "Hi")
# print("Replaced String:", replaced)  # Output: Hi World
# print(replaced.find("d"))  # Output: 7 

#  list of all string functions 
# string_functions = [
#     "capitalize()", "casefold()", "center()", "count()", "encode()",
#     "endswith()", "expandtabs()", "find()", "format()", "format_map()",
#     "index()", "isalnum()", "isalpha()", "isdecimal()", "isdigit()",
#     "isidentifier()", "islower()", "isnumeric()", "isprintable()",
#     "isspace()", "istitle()", "isupper()", "join()", "ljust()",
#     "lower()", "lstrip()", "partition()", "replace()",
#     "rfind()", "rindex()", "rjust()", "rpartition()",
#     "rstrip()", "split()", "splitlines()", "startswith()",
#     "strip()", "title()", "upper()"
# ]
# print("List of String Functions:")
# for func in string_functions:
#     print(func)

    # excercise  1 : Write a python program to display a user entered name followed by Good Afternoon using input () function.
userinput = input("Enter your name: ")
print("Good Afternoon", userinput)
    # excercise 2 : Write a python program to display the current date and time.
from datetime import datetime
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))

# task 2 : Write a program to fill in a letter template given below with name and date.
name = input("Enter your name: ")
date = input("Enter the date (YYYY-MM-DD): ")
letter_template = f"""
Dear {name},
This letter is to inform you that your application has been received on {date}.
Thank you for your interest.    
Sincerely,
The Team    
"""
print(letter_template)


