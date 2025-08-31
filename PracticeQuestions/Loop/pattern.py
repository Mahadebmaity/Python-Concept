""" 
Write a program to print the following star pattern.
*
***
***** for n = 3
"""
# starsNumber = int(input("Enter Number:"))
# for i in range(1,starsNumber+1):
#     spaces = starsNumber -i
#     stars = 2 * i - 1
#     print(" " * spaces + "*" * stars)

''' 
Write a program to print the following star pattern: *
**
*** for n = 3'''

# starsNumber = int(input("Enter Number:"))
# for i in range(1,starsNumber+1):
#     print("*" * i)


'''
Write a program to print the following star pattern.

* * *
*    * for n = 3
* * *
'''
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    
