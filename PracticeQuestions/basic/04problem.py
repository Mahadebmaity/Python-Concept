# 4️⃣ Write a program that prints the following path exactly:
# output: C:\newfolder\python\scripts
# code snippet:
'''
So, if I wrote:
# print("C:\newfolder\python\scripts") causeing error 
Python would think \n means newline, \p is invalid, and so on — causing unexpected results or errors.

'''
# But solve this another way using raw string or escape sequence.
# Here's how to do it correctly:
print(r"C:\newfolder\python\scripts")  # Using raw string to avoid escape sequences
# or
# solve this problem using escape sequence:
print("C:\\newfolder\\python\\scripts")  # Using escape sequences to avoid interpreting \n and \p
# or
# solve this problem using forward slashes:
print("C:/newfolder/python/scripts")  # Using forward slashes, which are valid in Python paths
#  but this is not the correct way to solve this problem.

