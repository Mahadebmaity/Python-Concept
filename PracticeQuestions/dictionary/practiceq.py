# 1️⃣ Create a dictionary with keys: name, age, city.
student = {
    "Name": " Mahadeb Maity",
    "class": "BCA",
    "CGPA": 8.5
}
print(student)
# 2️⃣ Access the value of the key name.
print(student["Name"])

# 3️⃣ Add a new key email to the dictionary.
student["email"] = " maitymahadeb530@gmail.com"
print(student)  

# 3️⃣ update the value of the key email.
updated_email = student.update({"email" : "jayanta530@gmail.com"})
print(student) 

print(student.pop("CGPA"))
print(student)

print(student.keys())
print(student.values())
print(student.items())
print(student.get("Name"))
print(student.get("city", "Key not found in the student dictionary."))  # Default value if key doesn't exist

print(student.clear()) 
print(student)  # This will print an empty dictionary after clearing







