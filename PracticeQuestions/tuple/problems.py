# 1️⃣ Create a tuple with 5 elements. Print it.
my_tuple = (1, 2, 3, 4, 5)
print("Tuple with 5 elements:", my_tuple)

# 2️⃣ Access the third element.
third_element = my_tuple[2]
print("Third element:", third_element)

# 3️⃣ Find the length of the tuple.
print(len(my_tuple))

# 4️⃣ Check if an item exists in the tuple.
items_exist = 6 in my_tuple
print("Does 3 exist in the tuple?", items_exist)
# 5️⃣ Count how many times an element appears.
count_of_element = my_tuple.count(3)
print("Count of element 3:", count_of_element)

# 6️⃣ Find the index of an element.
print(my_tuple.index(4))

# Convert tuple to list
convert = list(my_tuple)
# print("Converted to list:", convert)
print( list(my_tuple), type(my_tuple))
print(type(convert), type(my_tuple))

print(tuple(convert))
print(type(tuple(convert)))
# 7️⃣ Convert the tuple to a list and print both types.

# 8️⃣ Try to change an element in the tuple. Note what happens.
# my_tuple[0] = 12
# print("Attempted to change first element:", my_tuple)
# This will raise a TypeError because tuples are immutable.
# 9️⃣ Concatenate two tuples.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)

# 🔟 Repeat a tuple three times using * operator.
print("Repeated tuple:", tuple1 * 3)

# dictionary can repeat  in another way
dict1 = {
    "name": " Mahadeb",
    "age": 30,
    "city": "Kolkata"
}
print("repeated dic1:", [dict1] * 5)

