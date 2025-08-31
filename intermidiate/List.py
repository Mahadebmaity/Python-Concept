# A = "Mahadeb"
# # A[0] = "S"
# # print(A[0]) # now occurred an error because strings are immutable in python, so we cannot change the value of a string at a specific index.
# #  its write like this 
# print(A) # if i print whole string 
# print(A[4]) # if i want to write specific index value i can write like this

List = [ "Anjan", "Mahadeb",32.5, True ,  "Sourav", "jayanta", 45, 67.5, "Madhurima" ] # list can contain different data types
print(List[0]) # print first element of the list
List[0] = "Madhurima" # change the first element of the list
print(List[2]) # print third element of the list 
print(List)  # print whole list # unlike strings, lists are mutable in python, so we can change the value of a list at a specific index.

# list methods
List.append(" Debotosh") # append a new element to the end of the list
print(List) # print whole list after appending a new element
Newlist = [ 12,34,56,78,90 ] # create a new list
Newlist.sort()
print(Newlist) # print whole list after sorting the list
Newlist.reverse()
print(Newlist) # print whole list after reversing the list
print(len(Newlist)) # print the length of the list