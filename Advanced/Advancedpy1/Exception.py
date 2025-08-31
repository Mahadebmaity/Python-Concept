# Number = int(input("Enter number:")) # if user input string value output occures error 
# print(Number) # but without using this type  i can use this exception handling 

# Exception handling 
# try:
#     Number = int(input("Enter number:"))
#     print(Number)
# except Exception as e:
#     print(e)

# problem 
Number1 = int(input("Enter number:"))
Number2 = int(input("Enter number:"))

# print(f"Division is:{Number1 / Number2}") #  output occures ZeroDivisionError: division by zero
# so we can use this Raise  custom exception

if(Number2 == 0):
    raise ZeroDivisionError("Hey, this is not divided by zero")
else:
    print(Number1/Number2)



