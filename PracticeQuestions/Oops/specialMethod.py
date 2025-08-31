# 7. Special Methods
# Create a class Student that supports:

# __str__ for friendly print.

# __eq__ to compare students based on marks.

# __len__ to get number of characters in student’s name.

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student Name:{self.name}, Marks:{self.marks}"

    def __eq__(self, value):
        return self.marks == value.marks 

    def __len__(self):
        return len(self.name)
    
s1 = student("Mahadeb",84)
s2 = student("Jayanta", 84)
s3 = student("debotosh",95)

# __str__
print(s1)  # Friendly print
print(s2)  # Friendly print
print(s3)  # Friendly print

# __eq__
print("s1 == s2:", s1 == s2)  # True, since marks are equal
print("s1 == s3:", s1 == s3)  # False

# __len__
print("Length of s1's name:", len(s1))  # 7
print("Length of s2's name:", len(s3))  # 4