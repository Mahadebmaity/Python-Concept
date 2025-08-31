# Define variable naming rules in Python with two valid and invalid examples.
# _name = "Mahadeb Maity"
# name = "Mahadeb Maity"
# &name = " Mahadeb Maity" #  this variable naming rule is invalid 
# *name = "Mahadeb Maity" # invalid


# print(_name)
# print(name)
# print(&name)
# print(*name)

# --- end question answer ---
# new things -- unpacking 
# ✅ What is the Meaning of "Unpack" in Python?
# Unpacking means taking individual elements from a collection (like a list, tuple, string, etc.) and assigning them to separate variables.

# Basic unpacking with * 
first ,second, *last = [1,2,2,3,6,7,8] # Here's first contain only first element from the list  and *last captured remaining all 
print(f"first number:{first}\nSecond number:{second}\nsecond number:{last}") # then print aa a variable 
# string unpacking 
*name, = "Mahadeb"
print(*name,) # this is return only value with space like this : M a h a d e b
print(name) # but  it is return al the charecter in the  name list  like this : ['M', 'a', 'h', 'a', 'd', 'e', 'b']
# Middle unpacking 
first ,*middle , last = [10,20,30,40,50]
print(f"first value:{first}\nMiddle values:{middle}\nLast value:{last}")

# this is another unpacking 
'''
list = [10,20,30,60,50,25,18,45]
a,b,c,d,e,f,g,h = list 
print(f"Unpacking a value:{a}")
print(f"Unpacking b value:{b}")
print(f"Unpacking c value:{c}")
print(f"Unpacking d value:{d}")
print(f"Unpacking e value:{e}")
print(f"Unpacking f value:{f}")
print(f"Unpacking g value:{g}")
print(f"Unpacking h value:{h}")
'''

a,b,c,d,e,f,g,h =[10,20,30,60,50,25,18,45]
list = a,b,c,d,e,f,g,h
print(f"packing all value as a tuple and as a list name: {list}\ntype() this:{type(list)}")


