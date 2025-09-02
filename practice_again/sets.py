# what is set in python ?
# In python, set is a collection of unique items which is store value as a unordered , mutable for add and remove value but immutable can't change value 

# create set 
# number = {1,2,3,4,5}
# print(number, type(number))
# using set() constructor 
# number = set([1,2,3,4,5])
# print(number,type(number))
# now create empty set how?
# number = {} # return type dict not set  
# print(number,type(number)) # output : {} <class 'dict'>
# but this is done using set() method
# number = set()
# print(number,type(number))

# -------------------------------------------
# add value into set how ?
# number.add("Value")
# print(number)

# two types of removing method in set 

# name = {"Mahadeb","Jayanta","Debotosh"}
# name.remove("Biswajit") # this method raise error when does not exist any element but 
# print(name)

# name.discard("Biswajit") # but this method  not raise error 
# print(name)

# --------------------------------------------------------------------
# now I will teach you about set method 
# usually there are  sevarel set method but now I'll discuus about set operations which is the most important 
# concept in python set  these are => union , intersection , difference , symmetric difference 
# union => it combine element from two set , removing dupplicate element 
# number = {1,2,5,6}
# number1 = {3,4,5,6}
# number_union = number.union(number1)
# print(f"Number union of two set {number} and {number1} => {number_union}")
# same_union = number1.union(number1)
# print(f"the union of Same number set {number1} => {same_union}")

# alternative ways 
# union_set = number | number1
# print(f" Alternative ways => {union_set}")
# ----------------------
# intersection => it combine two set but only duplicate element just
# intersect_number1 = number.intersection(number1)
# print(f"Intersection of two set {number} and {number1} is => {intersect_number1}")
# same_intersection = number.intersection(number)
# print(f"intersection of same set {number} is => {same_intersection}")

# alternative ways
# intersect_set = number & number1
# print(f"Alternative ways => {intersect_set}")
# ------------------------
# Difference => it combine two set but only return present element in the first set not second set 
# difference_set = number.difference(number1)
# print(f"Difference between two set { number} and {number1} is => {difference_set}")

# alternative_way = number - number1
# print(f"Alternative ways => {alternative_way}")
# --------------------------
# symmetric difference_set => it returns element into the two set element either two set but not in both set same element 
# symmetric_diff_set = number.symmetric_difference(number1)
# print(f"symmetric_diff_set of two set {number} and {number1} => {symmetric_diff_set}")

# alternative_way = number ^ number1
# print(f" alternative ways => {alternative_way}")
# --------------------------------

# iteration of set 
# for i in number1:
#     print(i)

# but while loop is not possible  possible when we convert set to a list  because set in not indexing 
# -----------------------------
Numbers ={1,2,3,4,5,6}
# set_comprehension = {expression for valiable in iterable if condition} # syntax
# set_comprehension = { X ** 2 for X in Numbers if X%2!=0}
# print(f"set_comprehension:=> {set_comprehension}")

from sympy import isprime
set_comprehension = {X for X in range(1,10) if isprime(X)}
print(set_comprehension)

# ------------------------------------------
