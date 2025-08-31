Set = { 2,4,6,"r"} #this is set 
print(Set , type(Set))
# first question is : how to create a empty set in python 
Emptyset = set() # this is how we create an empty set in python
print(Emptyset , type(Emptyset)) # Now Emptyset is an empty set

newset = { 12,34,53,24,12,12,12,45,53}
print(newset) # set does not allow duplicate values, so it will only keep unique values
print(len(newset))  # calculate lenth of a given set 
# set methods1
print(newset.pop()) # removes and returns an arbitrary element from the set
