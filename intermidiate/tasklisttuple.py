# Write a program to store seven fruits in a list entered by the user.
''' 
Fruits = []
FruitsName = input("Enter the name of the first fruit: ")
Fruits.append(FruitsName)
FruitsName = input("Enter the name of the second fruit: ")
Fruits.append(FruitsName)
FruitsName = input("Enter the name of the third fruit: ")
Fruits.append(FruitsName)
FruitsName = input("Enter the name of the fourth fruit: ")
Fruits.append(FruitsName)
FruitsName = input("Enter the name of the fifth fruit: ")
Fruits.append(FruitsName)
FruitsName = input("Enter the name of the sixth fruit: ")
Fruits.append(FruitsName)
FruitsName = input("Enter the name of the seventh fruit: ")
Fruits.append(FruitsName)
print(" The List of Fruits is : " , Fruits)
'''

# Write a program to accept marks of 6 students and display them in a sorted manner.
'''
Marks = []
Marks1 = int(input("Enter the name of the first Marks: "))
Marks.append(Marks1)
Marks2 = int(input("Enter the name of the second Marks: "))
Marks.append(Marks2)
Marks3 = int(input("Enter the name of the third Marks: "))
Marks.append(Marks3)
Marks4 = int(input("Enter the name of the fourth Marks: "))
Marks.append(Marks4)
Marks5 = int(input("Enter the name of the fifth Marks: "))
Marks.append(Marks5)
Marks6  = int(input("Enter the name of the sixth Marks: "))
Marks.append(Marks6)
Marks7 = int(input("Enter the name of the seventh Marks: "))
Marks.append(Marks7)
Marks.sort()  # sort the list of marks
print("List of the sorted marks is : " , Marks)
'''
#  check that tuple  type can not be changed 
A = (1, 2,0, 3, 4,0, 5,0)
print(type(A))  # print the type of the tuple
# A[0] = 10
# print(A)
# This will raise an error because tuples are immutable

# Write a program to sum a list with 4 numbers.
print(sum(A))
print(A.count(0))



