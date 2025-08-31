# Program to check if a number is prime or not
Number = int(input("Enter the valid number:"))

if Number > 1:
    for i in range(2,int(Number ** 0.5) +1): # i can calculate square root using math libraries using sqrt()method or pow() using 0.5 value  
        if Number%2==0: #but must calculate square root of a number 
            print(f"{Number} is not a Prime number")
            break
    else:
        print(f"{Number} is a Prime number")
else:
    print(f"{Number} is not a prime Number")


