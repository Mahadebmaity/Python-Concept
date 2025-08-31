# 1️⃣ Write a Python program to input your name, age, and GPA. Then print each variable with its type.

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
GPA = float(input("Enter your GPA: "))
# print({"Name:", Name, "Type:",type(Name)},
#       {"Age:", Age, "Type:", type(Age)},
#       {"GPA:", GPA, "Type:", type(GPA)})

# i can use this type of declaration also
print(f"Name: {Name}, Type: {type(Name)}\nAge: {Age}, Type: {type(Age)}\nGPA: {GPA}, Type: {type(GPA)}")
# print(f"Name: {Name}, Type: {type(Name)}\nAge: {Age}, Type: {type(Age)}\nGPA: {GPA}, Type: {type(GPA)}")

#  we can use this type of declareation also 
print(f"Name: {Name!r}, Type: {type(Name)!r}\nAge: {Age!r}, Type: {type(Age)!r}\nGPA: {GPA!r}, Type: {type(GPA)!r}")

# another way to solve this or print this 
print("Name:", Name, "Type:", type(Name))
print("Age:", Age, "Type:", type(Age))
print("GPA:", GPA, "Type:", type(GPA))
# another way to print this