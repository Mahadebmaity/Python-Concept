# All possible walrus operator operations

# avoids writing input twice 
# while (line := input("Enter something: ")) != "exit":
    # print("You typed:", line)

# check length 
# if(length := len(input("Enter your Name:"))) > 5:
#     print(f"Your name lengh is: {length} which is greter than required  length.")

# chained condition 

# x = 5
# if (y := x + 3) > 5:
#     print("y is greater than 5:", y)


# def get_value():
#     return "Mahadeb"

# if (name := get_value()):
#     print("Hello,", name)
# else:
#     print("blank")


# list comprehension with walrus operator  and verious condition

# squares = [square for x in range(1, 6) if (square := x**2) % 2 == 0]
# squares = [square for x in range(1, 6) if (square := x**2) > 10]
# squares = [square for x in range(1, 6) if (square := x**2) < 10] 
# squares = [square for x in range(1, 6) if (square := x**2)% 2!=0] 
# print(squares)

# improve one step level up this code 
# result = [(i, square) for i in range(1, 11) if (square := i ** 2) > 30]
# print(result)

# output : [(6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]

table = []
for i in range(1, 4):
    for j in range(1, 4):
        table.append(i * j)

print(table)
