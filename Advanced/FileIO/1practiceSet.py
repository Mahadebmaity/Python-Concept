# Q1. Write a program to create a file hello.txt and write "Hello World!" into it.
# with open("hello.txt","w") as f:
#     f.write("Hi, this is a python file I/O chapter concept.")

# Q2. Write a program to read the content of hello.txt and print it.
# with open("hello.txt") as f:
#     print(f.read())

# Q3. Write a program to append "Python is fun!" to hello.txt and then print its updated content.
# string = "Python is a fun language\n"
# with open("hello.txt","a") as f:
#     content = f.write(string)

# with open("hello.txt") as f:
#     print(f.read())

# Q4. Write a program to count how many words are in a file sample.txt.
# with open("hello.txt") as f:
#     content = f.read()

# with open("hello.txt") as f:
#      lines = f.readlines()


# line_Number = len(lines)
# words = content.split()
# word_count = len(words)
# print(f"Number of lines in this file are : {line_Number}")
# print(f"Number of words in this file are : {word_count}")

# print(f" Number of lines in this file are: {len(open("hello.txt").readlines())}") # this is a one liner version to write code 

# Q6. Write a program that replaces all occurrences of "Java" with "Python" in sample.txt and writes the changes to a new file output.txt.
# with open("hello.txt") as f:
#     content = f.read()
# replace_word = content.replace("Python","Java")
# # print(replace_word)   
# with open("output.txt","w") as f:
#     # print(f.write(replace_word)) # this line return number of character given this file
#     f.write(replace_word)
# print("replace word  successful from the hello file")

# below this code is experimental because above this code is not work so check it and done this 
# Open the original file and read its content
# with open("hello.txt") as f:
#     content = f.read()

# # Replace all occurrences of "Java" with "Python"
# updated_content = content.replace("Python", "JAVA")

# # Write the updated content to a new file
# with open("output.txt", "w") as f:
#     f.write(updated_content)

# print("Replacement done! Check 'output.txt'.")

#  File Exists
# Q8. Write a program to check if a file data.txt exists or not.

# below code is not actual answer of above this question
# with open("hello.txt") as f:
#     content = f.read()

# print(content)
# if content == "":
#     print("The file is empty!")
# else:
#     print("The file is in the data")

# here is the right code above this question 

# import os

# if os.path.exists("hi.txt"): # check  file exist or not  with os module 
#     print("File exists.")
#     os.remove("hello.txt")
# else:
#     print("File does not exist.")
#  Write a program to delete test.txt if it exists.  same code but a little changes in this code 


# 9️⃣ Read Specific Line
# Q10. Write a program to print the 3rd line of a file sample.txt.

# with open("hello.txt") as f:
#     lines = f.readlines()

# if len(lines) >= 3:
#     print(f"{lines[2]}")
# else:
#     print("lines of numbers are less than 3 ")



# 🔟 Read File in Reverse
# Q11. Write a program to read a file sample.txt and print its lines in reverse order.

# with open("hello.txt") as f:
#     lines = f.readlines()

# for line in reversed(lines):
#     print(line.strip())

# 🔍 How it works
# 1️⃣ readlines() → reads all lines into a list.
# 2️⃣ reversed(lines) → returns the lines in reverse order.
# 3️⃣ print(line.strip()) → prints each line without extra newline characters.


#  Find Longest Line
# Q12. Write a program to find the longest line in a file sample.txt.

# with open("hello.txt") as f:
#     lines = f.readlines()

# longest_line = ""
# max_length = 0
# for line in lines :
#     if len(line) >= max_length:
#         max_length = len(line)
#         longest_line = line

# print(f"Here is a longesst line in this file:\n{longest_line.strip()}\nand length of this line is(Character) : {max_length}")


# 1️⃣2️⃣ Word Search
# Q13. Write a program to search for a word given by the user in sample.txt and print the line numbers where it appears.
# Searching_element = input("Enter your Search element:")
# with open("hello.txt") as f:
#     lines = f.readlines()

# lineno = 1
# line_numbers = []
# for line in lines:
#     if Searching_element in line:
#         line_numbers.append(str(lineno))
#     lineno +=1

# if line_numbers:
#     print(f"Yes,{Searching_element} is  present on line no: {line_numbers}")
# else:
#     print(f"No, {Searching_element} is not present in this line.")


# Count Character Occurrence
# Q14. Write a program to count how many times the letter "e" appears in sample.txt.
# with open("hello.txt") as f:
#     content = f.read()

# count = content.count("p")
# print(f"The Number of p is {count}")


#  Write a program to take multiple lines of user input and store them in user.txt (stop taking input when the user types "stop").
# with open("User.txt","w") as f:
#     while True:
#         line = input("Enter a line (type 'stop' to finish):")
#         if line.lower() == "stop":
#             break
#         f.write(line + "\n")
# with open("User.txt") as f:
#     print(f.read())

# print("All lines are saved  in user.txt file, please check!")


# 1️⃣5️⃣ Merge Files
# Q16. Write a program to merge two files file1.txt and file2.txt into merged.txt.
with open("file1.txt") as f1, open("file2.txt") as f2:
    margefile1 = f1.read()
    margefile2 = f2.read()

with open("margefile.txt","w") as f3:
    f3.write(margefile1 + "\n")
    f3.write(margefile2 + "\n\t\n")

print("marge file successfully please check it.")

with open("margefile.txt") as f:
    print(f" \n{f.read()} \n")



