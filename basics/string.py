# Now practice the string  data types  in the various ways
a = "hello world " # this  is the single quoted string
b = 'python programming ' # this is the double quoted string 
c = '''this is a multiline string 
it can span multiple lines''' # this is a triple quoted string 
d = """this is also a multiline string
it can also span multiple lines""" # this is also a triple quoted string

# String slicing and indexing
name = "python programming"
st = name[0:7]
print("String slicing:", st)  # Output: python
st = name[7:18]
print("String slicing:", st)  # Output: programming
negeative_indexing = name[-1]  # Last character
print("Negative indexing:", negeative_indexing)  # Output: g
# if i'll write  
print(name[:7]) #  this is  the  same as name[0:7]
# it will print the first 7 characters of the string 
print(name[7:]) # Output: programming  and this is the same as name[7:18]
print(name[-11:]) # Output: programming and this is the same as name[7

