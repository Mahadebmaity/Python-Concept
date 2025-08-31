# Write a program using functions to find greatest of three numbers.

# without argument 
def greatest():
    a = int(input("enter  first number"))
    b = int(input("enter  second number"))
    c = int(input("enter  third number"))
    if a > b and  a > c:
        print(f"{a} is greater")
    elif b > c :
        print(f"{b} is greater")
    else:
        print(f"{c} is greater")

# greatest()

#  with argument  and default value 
def greatest(a=34,b=78,c=56):
    if a > b and  a > c:
        print(f"{a} is greater")
    elif b > c :
        print(f"{b} is greater")
    else:
        print(f"{c} is greater")

# greatest(45,56,12)

# try extra doubt solve itself and experiment 
def greatest():
    a = int(input("enter  first number : "))
    b = int(input("enter  second number : "))
    c = int(input("enter  third number : "))
    if a > b and  a > c:
        if b > c:
            print(f"{a} is greater and {b} is second greater, {c} is samller.")
        else:
            print(f"{a} is greater and {c} is second greater, {b} is samller.")
    elif a < b and   b > c :
        if a > c:
            print(f"{b} is greater and {a} is second greater, {c} is samller.")
        else:
            print(f"{b} is greater and {c} is second greater, {a} is samller.")
    elif c >  a and c > b:
        if a > b : 
            print(f"{c} is greater and {a} is second greater, {b} is samller.")
        else:
            print(f"{c} is greater and {b} is second greater, {a} is samller.")
    
# greatest()

    # above code is very heavily so i rewrite this code is better way 


def greatest(a,b,c):
    # greater_number = max(a,b,c)
    # smallest_greater = min(a,b,c)
    # second_greater = a+b+c -(greater_number + smallest_number)
    # print(f"{greater_number} is greater, {second_greater} is second greater ,  {samllest_number} is  smallest")
    print(f"{max(a,b,c)} is greater, {a+b+c -(max(a,b,c) + min(a,b,c))} is second greater ,  {min(a,b,c)} is  smallest")
greatest(34,56,78)

