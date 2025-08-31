"""# Dictionary in Python
if we create an empty dictionary 
Empty_dict = {} that's it 
marks = {
     "Math" : 90,
     "Physics": 85,
     "Chemistry" :88
}
print(marks , type(marks))
# print(marks[1]) # This will raise an error because dictionary keys are not accessed by index
print( "Math:" , marks["Math"])

# Dicstionary methods 
print(marks.items()) # Returns a view object that displays a list of dictionary's key-value tuple pairs
print(marks.keys()) # Returns a view object that displays a list of all the keys in the dictionary
print(marks.values()) # Returns a view object that displays a list of all the values in the dictionary

marks.update({"Math" : 95}) 
# marks.update({"english" : 92} , {"bengali": 56})   only one dictionary can be passed to update method
print(marks)

print(marks.get("Math")) # Returns the value for the specified key if it exists, otherwise returns None
# print(marks["Math2"]) # This will raise a KeyError if the key does not exist

# marks.clear() # Removes all items from the dictionary
# print(marks) # Now marks is an empty dictionary

# marks.pop("Physics") # Removes the specified key and returns its value
# print(marks)
# marks.popitem("Math")  # popitem is not contain key, it removes the last inserted key-value pair
marks.popitem() # Removes the last inserted key-value pair 
# print(marks) 

marks.setdefault("English", 92) # If the key does not exist, it inserts the key with the specified value
# print(marks)

new_marks = marks.copy() # Creates a shallow copy of the dictionary
# print(new_marks)
new_marks1 = marks
print(new_marks1) # new_marks1 is a reference to the same dictionary as marks, so changes to one will affect the other
new_marks1["English"] = 75 # Changing new_marks1 will also change marks  
print(marks) # Now marks will also reflect the change made in new_marks1
"""
# keys = [ 1 ,2 ,3]
key = (1, 2, 3) # tuple can also be used as keys in dictionary
newdict = dict.fromkeys(key) 
print(newdict) # Creates a new dictionary with keys from the list and values set to None by default
 
newdict1 = dict.fromkeys(key,"value")
print(newdict1) # Creates a new dictionary with keys from the list and values set to "value"

# if i want to add value to existing dictionary
newdict1[1] = "one"
newdict1[2] = "two" 
newdict1[3] = "three"
print(newdict1) # Now newdict1 has values assigned to the keys

