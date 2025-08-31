# def countdown(n=5):
#     if n <= 0:
#         print("Done!")
#     else:
#         print(n)
#         countdown(n - 1)

# countdown(6)

# Write a recursive function to calculate the sum of first n natural numbers.
# def sum(n):
#     if n==1:
#         return 1
#     else:
#          return sum(n-1)+ n

# n = int(input("enter number: "))
# print(sum(n))


# Write a python function to print first n lines of the following pattern:

# def pattern(n):
#     if n==0:
#         return 
#     print("*" * n)
#     pattern(n-1)

# pattern(6)

# Write a python function which converts inches to cms.

# def inch_cms(inch):
#     return inch * 2.54

# inch = int(input("Enter the inch: "))
# print(f"the corresponding value in cms is: {inch_cms(inch)}")

# Write a python function to remove a given word from a list ad strip it at the same time

def remove(list,word):
    n=[]
    for items in list:
        if not(items==word):
            n.append(items.strip(word))
    return n

list = ["Mahadeb", " rohan", "an", "jayanta"]
# print(remove(list,"an"))

# Write a python function to print multiplication table of a given number.

#using only function
def multiplecation(n):
     for num in range(1,11):
         Num = n * num
         print(f"{n} * {num} = {Num}") 
     
# Number = int(input("Enter the numbers: "))
# multiplecation(Number)

#using recursive function
def multiply(number,i=1,n=20):
    if i > n:
        return
    else:
        print(f"{number} x {i} = {number * i}")
        multiply(number,i+1,n)

mulvalue =int(input("Enter the multiplecation value :"))
multiply(mulvalue)