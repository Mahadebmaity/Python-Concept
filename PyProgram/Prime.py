# Q1 => written a Python program to find all prime numbers between 1 and n.
def Prime_checking_Method1():
    count = 0
    n = int(input("Enter a number:"))
    print(f"List of prime numbers between 1 to {n}")
    Prime =[]
    for i in range(1,n+1):   # loop through all numbers from 1 to n
        cn = i               # current number to test
        count=0              # reset divisor count for each number
        for j in range(1,cn+1):   # check all numbers from 1 to cn
            if cn % j == 0:       # if j divides cn
                count += 1        # increase divisor count
        if count == 2:            # prime numbers have exactly 2 divisors (1 and itself)
            Prime.append(cn)      # add prime number to list

    print(Prime)

Prime_checking_Method1()

# since this method is a bit slow for large numbers =>  
# Why My current method is slow
#For every number i, you loop from 1 to i and count divisors.
# That means if n = 1000, the program does 1000 × 1000 = 10,00,000 checks.
# For large n, it becomes very slow.

# optimized way 
def Prime_checking_Method2():
    import math

    n = int(input("Enter a number: "))
    print(f"List of prime numbers between 1 to {n}")
    Prime = []

    for i in range(2, n+1):   # start from 2, since 1 is not prime
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):  # check up to √i
            if i % j == 0:
                is_prime = False
                break   # no need to check further
        if is_prime:
            Prime.append(i)

    print(Prime)

Prime_checking_Method2()
