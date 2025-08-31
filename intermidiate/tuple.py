# Tuple = (1,3 ,45, "Mahadeb", "Anjan", 67.5, True ) # tuple can contain different data types
# print(Tuple[0]) # print first element of the tuple
# print(Tuple)
# Tuple[0] = "Madhurima" # this will occur an error because tuples are immutable in python, so we cannot change the value of a tuple at a specific index.
# print(Tuple) #error generate 

# Now discuss about tuple methods 
Tuple1 = (1,3 ,45, "Mahadeb", "Anjan", 67.5, True ) 
Tuple2 = ( 23, 45, 67, "Sourav", "jayanta", 78.5, False ) # tuple can contain different data types
Tuple3 = (2,3,4,5,3,6,7,8,9) # another tuple for demonstration
# tuple can contain different data types
print(len(Tuple1)) # print the length of the tuple
concatenated_tuple = Tuple1 + Tuple2 # concatenate two tuples
print(concatenated_tuple) # print the concatenated tuple
result =Tuple3.count(3) # count the number of occurrences of an element in the tuple
print(result) # print the result
print("the index of 6: ", Tuple3.index(6)) # print the index of the first occurrence of an element in the tuple

# slicing tuple 
sliced = Tuple3[3:6]
print("Removed elements: ", sliced) # print the sliced tuple
print("Original tuple after slicing: ", Tuple3) # print the original tuple after slicing
 
print(5 in Tuple3) # check if an element is in the tuple
print('Mahadeb ' in Tuple1) # check if an element is in the tuple

