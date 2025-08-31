#  Walrus operator 
numbers = [1, 2, 3, 4, 5]

while (n := len(numbers)) > 0:
         print(numbers.pop())

## The below example is without Walrus Operator
# foods = list()
# while True:
#   food = input("What food do you like?: ")
#   if food == "quit":
#     break
#   foods.append(food)

# Below Approach uses Walrus Operator
# foods1 = list()
# while (food := input("What food do you like? (type 'quit' to stop): ")) != "quit":
#     foods1.append(food)

# another example 

# sample_data = [
#     {"userId": 1, "name": "rahul", "completed": False},
#     {"userId": 1, "name": "rohit", "completed": False},
#     {"userId": 1, "name": "ram", "completed": False},
#     {"userId": 1, "name": "ravan", "completed": True}
# ]

# print("With Python 3.8 Walrus Operator:")
# for entry in sample_data:
#     if name := entry.get("name"):
#         print(f'Found name: "{name}"')

# print("Without Walrus operator:")
# for entry in sample_data:
#     name = entry.get("name")
#     if name:
#         print(f'Found name: "{name}"')