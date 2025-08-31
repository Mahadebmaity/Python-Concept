# 1️⃣ Create a set with numbers {1, 2, 3, 4, 5}.
numbers = { 12,23,24,35,46,65, 78, 89, 90 }
print("Original set:", numbers)
# numbers.add(5)
# print( "After adding numbers " , numbers)

# print(numbers.remove(90))
# print("After removing 90:", numbers)
# print(numbers.discard(78)) 
# print("After discarding 78:", numbers)
# print(numbers.pop())
# print("After popping an element:", numbers)

numbers_set1 = { 24,56,90,56,12,78}
print( numbers - numbers_set1)
print( numbers_set1 - numbers)
print("Union of both sets:", numbers | numbers_set1) or print("Union of both sets:", numbers.union(numbers_set1))
# print("Intersection of both sets:", numbers & numbers_set1) or print("Intersection of both sets:", numbers.intersection(numbers_set1))
# print("Symmetric difference of both sets:", numbers ^ numbers_set1) or print("Symmetric difference of both sets:", numbers.symmetric_difference(numbers_set1))





