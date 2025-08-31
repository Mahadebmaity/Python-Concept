# Write a list comprehension to print a list 
# which contains the multiplication table of a user entered number.

# n = int(input("Enter Number which Number you want to get a Multiplecation table?(Higher than 10): "))
# Table =[x*i for i in range(1,11)]
# print(f"Multiplecation table of {n} is:\n {Table}")

# Write a program to display a/b where a and b are integers.
#  If b=0, display infinite by handling the ‘ZeroDivisionError’.

# try:
#     a = int(input("Enter the first number"))
#     b = int(input("Enter the second number"))
#     print(a/b)
# except ZeroDivisionError as e:
#     print("Infinite")


# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

n = int(input("Enter Number which Number you want to get a Multiplecation table?(Higher than 10): "))
for x in range(10,n+1):
    Table =[x*i for i in range(1,11)]
    with open("Tables.txt","a") as f:
        f.write(f"Multiplecation table of {x} is:\n{Table}\n Table Successfully added!\n")




