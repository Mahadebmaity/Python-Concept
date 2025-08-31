# 2. Write a program to input name, marks and phone number of a student and format it using the format function like below:
# “The name of the student is Harry, his marks are 72 and phone number is 99999888”

# Info = "The name of the student is {},His marks are {} and phone number is {}".format(input("Enter Your Name:"),input("Enter your HS marks:"),input("Enter your phone Number:"))
# print(Info)


# 3. A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers
table =[str(7*i) for i in range(1,11)]
Multiplecation_table = "\n".join(table)
# print(Multiplecation_table)

# 4. Write a program to filter a list of numbers which are divisible by 5.

def Divisible5(n):
    if(n%5==0):
        return True
    return False

a = [ 12,45,56,78,95,125,120,132,456]
f = list(filter(Divisible5,a))
print(f)

# Write a program to find the maximum of the numbers in a list using the reduce function.
