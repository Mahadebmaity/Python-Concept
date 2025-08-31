def Input():
        N = int(input("Enter Number Which you want to print pattern Square::"))
        return N

#square printing
def Starsquare(N):
    for _ in range(1,N):
        for _ in range(1,N):
            print(" *",end="")
        print()

# Starsquare()

# same task using string multiplecation 
def Starsquare1(N):
        print((" *" * N +"\n")*N)

# Starsquare1()

def Numbersquare(N):
    for i in range(1,N):
        for _ in range(1,N):
            print(" ", i,end="")
        print()

# Numbersquare()

def Numbersquare(N):
    for _ in range(1,N):
        for j in range(1,N):
            print(" ", j,end="")
        print()

# Numbersquare()


def Numbersquare(N):
    for i in range(N,0,-1):
        for _ in range(N,0,-1):
            print(" ", i,end="")
        print()

# Numbersquare()

def Numbersquare(N):
    for _ in range(N,0,-1):
        for j in range(N,0,-1):
            print(" ", j,end="")
        print()

# Numbersquare()

def NumberPrint(N):
    # n = 5 
    k = 1
    for _ in range(1, N + 1):       # Outer loop for rows
        for _ in range(1, N + 1):   # Inner loop for columns
            print("{:2d}".format(k), end=" ")  # Print with 2-width formatting
            k += 1                  # Increment number
        print()                     # Move to next line

# NumberPrint()


def listofpatterns():
    print("1. Starsquare")
    print("2. Starsquare1")
    print("3. Numbersquare")
    print("4. Numbersquare (with j)")
    print("5. Numbersquare (decreasing i)")
    print("6. Numbersquare (decreasing j)")
    print("7. NumberPrint")

def main():
    listofpatterns()
    choice = int(input("Enter the number of the pattern you want to print: "))
    N = Input()
    
    if choice == 1:
        Starsquare(N)
    elif choice == 2:
        Starsquare1(N)
    elif choice == 3:
        Numbersquare(N)
    elif choice == 4:
        Numbersquare(N)  # This will call the same function as above, consider renaming
    elif choice == 5:
        Numbersquare(N)  # This will call the same function as above, consider renaming
    elif choice == 6:
        Numbersquare(N)  # This will call the same function as above, consider renaming
    elif choice == 7:
        NumberPrint(N)
    else:
        print("Invalid choice. Please try again.")
        return main()
    
def main2():
    main()
    Validation = input("Choice again to write 'yes'=>> ")
    if Validation.lower()== "yes":
        return main2()
    elif Validation.lower()== " ":
        return exit()
    else:
        return exit()


if __name__ == "__main__":
    main2()







