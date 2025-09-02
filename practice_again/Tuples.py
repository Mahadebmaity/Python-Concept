# what is tuple? 
# tuple is a  collection of all items which is ordered , unchangable(immutable), allow dupplicate value  to store multiple items 

# create tuple 
# numbers = (1,2,3,4,5)
# print(numbers,type(numbers))
# fruits = "Mango", "Apple","Goava" 
# print(fruits,type(fruits))
# # to create tuple using tuple() constructor 
# multi_value = tuple(('Mahadeb',23,bool)) # multiple type value store
# print(multi_value, type(multi_value))
# single_tuple = ("Mahadeb") # this is string 
# single_tuple = ("Mahadeb",) # now this is tuple 
# print(single_tuple,type(single_tuple))
# list = [1,2,True,"string"] # this is a list 
# type_convertion_tuple = tuple(list)  # this is convert list  from tuple 
# print(list,type(list))
# print(type_convertion_tuple,type(type_convertion_tuple)) # then type checking 
# --------------------------------------------------------------------
#accessing element by indexing 
# fruits = ("Mango", "Apple","Goava")
# print(fruits) # print whole tuple 
# print(fruits[0]) # print first element of the tuple
# print(fruits[2]) # print last element of the given tuple 

# # now tuple slicing 
# print(fruits[0:3]) # print whole tuple  using slicing 
# print(fruits[:3]) # same to print whole tuple using slicing 
# print(fruits[:-1:]) # print last element using negetive indexes 
# print(fruits[::-1]) # print reverse tuple using negetive indices 
# ---------------------------------------------------------------
# now we try to learn about tuple operations 
fruits = ("Mango", "Apple","Goava","Mango")
# fruits2 = ("banana","pinapple","orange")
# print(fruits + fruits2) # concatenation tuple operations 
# Repetations  = fruits * 3 # tuple repetation 
# print(Repetations, type(Repetations)) 
# fruits3 = ("mango",) * 4
# print(fruits3, type(fruits3))
# # searching element in the given tuple 
# print("Mango" in fruits) # return true if find or not return false

# now iterate to print tuple element 
# for i in fruits:
#     print(i)

# print("\n")
# i =0
# while i < len(fruits):
#     print(fruits[i])
#     i +=1

# ---------------------------------------------------------------------
# print(fruits.count("Mango"))
# print(fruits.index("Goava"))
# print(len(fruits))
# print(sorted(fruits))# sorted tuple  and return value as a list formate 
# print(sum(numbers)) # sum of all tuple numbers
# print(min(numbers))
# print(max(numbers))
# ----------------------------------------------------------------
#  packing tuple  
# name = "Mahadeb"
# age = 22
# ifmarried = True
# packing_value = name, age, ifmarried
# print(packing_value, type(packing_value))

# # unpacking tuple 
# packing_value = ('Mahadeb', 22, True)
# name , age , ifmarried = packing_value
# print(name, age , ifmarried)
# # ---------------------------------------------------------------------
# We can't modifying tuple 
number = (1,2,3,4,5)
# number[0] = 6 
# print(number) ## raise error  = TypeError: 'tuple' object does not support item assignment

# # but i can modified by another way how ?
# numbers = list(number) # first type cast into list then modified then type cast 
# numbers.append(6) # now this possible to assign
# print(tuple(numbers))  

# ---------------------------------------------------------------------
# Nested Tuples and Access
t = (1, (2, 3), (4, 5, 6))
print(t[1])       # (2, 3)
print(t[2][1])    # 5

# ---------------------------------------------------------------------
# # small notes ::
# Tuple vs List
# Tuple is immutable, List is mutable.
# Tuples are faster than lists.
# Tuples can be used as dictionary keys, lists cannot.

