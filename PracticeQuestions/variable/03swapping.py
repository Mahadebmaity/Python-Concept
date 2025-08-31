# 3️⃣ Write a Python program to swap two variables without using a third variable.
a = 12
b = 15
print("Before swapping the value of a is ", a , "and b is ", b )
#  with out 
a = a + b # a = 27
b = a -b  # b = 12
a = a - b  # a = 15
print("After swapping the value of a is ", a , "and b is ", b )
# with thired variable
swap = a
a = b 
b = swap
print("After swapping the value of a is ", a , "and b is ", b )
#  Run any one code 
