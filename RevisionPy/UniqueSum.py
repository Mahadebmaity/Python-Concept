# Create a list of five numbers and print the sum of the first and last elements.
list = [1,2,3,4,5]
first, *middle,last = list   # here i use unpacking 
# Sum = str(sum(first1,last1)) # get error in this line 
sum = first + last 
print(f"Sum of first and last numbers of the list:{sum}")


'''
list = [1,2,3,4,5]
first, *middle,last = list
print(f"Sum of first and last numbers of the list:{sum(first,last)}")

output will be this code :
TypeError: 'int' object is not callable

solve this code: 
only change there : {sum([first,last])} 
# because when we need to  perform any operation using multiple 
# value then combine fine as a tuple or list like these

'''

