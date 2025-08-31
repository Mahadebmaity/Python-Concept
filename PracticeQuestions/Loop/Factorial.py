# Write a program to calculate the factorial of a given number using for loop.

Number = int(input("Enter the number, which number you want to calculate factorial!:"))
i = 1
fact = 1
for i in range(i,Number+1):
    fact *= i

print(f" The factorial of {Number} is ", fact)

