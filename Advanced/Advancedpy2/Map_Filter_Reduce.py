from functools import reduce
# Map method
Numberlist =[1,2,3,4,5,6,7,8,9,10]
square = lambda x:x*x
store = map(square,Numberlist)
# print(list(store))

# filter method 
def odd(n):
    if(n%2 !=0):
        return True
def even(n):
    if(n%2==0):
        return True


onlyOdd = filter(odd,Numberlist)
onlyEven = filter(even,Numberlist)
# print(f"Odd number of {Numberlist} is:{list(onlyOdd)}")
# print(f"Even number of {Numberlist} is:{list(onlyEven)}")

# Reduce method 
# def sum(a,b): # i can use user defined function 
#     return a+b

sum = lambda a,b: a*b # i can use this lambda function   write code in one line

# result =reduce(sum,Numberlist)
# print(result)



# Write a program to find the maximum of the numbers in a list using the reduce function.
Number = [56,45,78,59,25,10,35,45,95]

max = lambda a, b: a if a > b else b
result = reduce(max,Number)
print(f" Maximum Number is : {result}")

