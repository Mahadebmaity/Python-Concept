# 1️⃣ Create a list with 5 numbers. Print the list.
numbers = [10,12,13,14,15]
print(numbers)  

# 2️⃣ Append a number to the list
numbers.append(16)
print(numbers)
# 3️⃣ Insert a number at index 2.
numbers.insert(2,28)
print(numbers)

# 4️⃣ Remove a specific number from the list.
numbers.remove(14)
print(numbers)

# 5️⃣ Pop the last item and print it.
numbers.pop()
print(numbers)

# 6️⃣ Sort the list in ascending order.
numbers.sort()
print(numbers)

# 7️⃣ Sort the list in descending order.
numbers.sort(reverse = True)
print(numbers)

reversed_numbers = reversed(numbers)
print(list(reversed_numbers))

# 8️⃣ Count how many times a number appears in the list.
print(numbers.count(12))

# 9️⃣ how many items are in the list?
print(len(numbers))
# 10️⃣ Clear the list.
# numbers.clear()
# print(numbers)

# 9️⃣ Find the index of a specific number.
print(numbers.index(10))

#extend methods 
b = [ 1,34,56,43,23]
numbers.extend(b)
print(numbers)

# copy methods 
c =  b.copy()
print(c)

# reverse methods 
reversed = numbers.reverse()
print(numbers)

# list methods
s = "Mahadeb"
L = list(s)
print(L)



print(max(numbers))
print(min(numbers))
print(sum(numbers))

