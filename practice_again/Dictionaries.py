# Now discuss about most usefull concept in python which is use several  concept , and things
# What is ? =>   In python Dictionary is a data structure to store data as a key-value pairs , it is ordered , mutable and not allow dupplicate keys

# how to create dictionary => it is create three methods such as 
# method1 => using curly braces {}
# info = {
#     "Name" : "Mahadeb Maity",
#     "age" : 22,
#     "Living" : "Panskura", 
#     "Ismaried" : False
# }

# print(f"This is method 1 => {info}")

# Now method2 =>  dict() constructor 
# info = dict(name = "Mahadeb", Age = 22 , Living = "Panskura", Ismaried = True)
# print(f"This is method 2 => {info}")

# now method3 =>  using a list of tuples 
# info = dict([("name","Mahadeb"),("age",22),("Living","Panskura")])
# print(f"This is method 3 => {info}")
# ----------------------------------------------
# accessing key and value pairs  => 
# print(info["Name"])

# Dictionary methods 
# print(f" Using items() method => {info.items()}")
# print(f"Using values() method to get only all values into dict=> {info.values()}")
# print(f"Using keys() method to get only all keys into dict => {info.keys()}")
# print(f" Using get() method to acccess specified value => {info.get("Name")}")

# removeing key value pairs => 
# info.pop("age")
# print(info)
# info.popitem()
# print(info)

# info.clear()
# print(info)

# copied_dict = info.copy()
# print(info)
# print(copied_dict)
# change_value = copied_dict.update(Name = "jayanta" )
# print(copied_dict)
# print(change_value) # return only None 
# -------------------------------------------
# Dictionary iterations

# for key in info:
#     print(key)
#     print(info[key])

# for value in info.values():
#     print(value)

# for key, value in info.items():
    # print(f"{key}:{value}")


# -----------------------------------
# We can create and display nested  dictionary key values 
students = {
    "Student1" : {
        "Name" : "Mahadeb Maity",
        "Age" : 22,
        "Ismaried" : False,
        "Parent" :{
            "Father_Name":{
                "IsAlive": False
            },
            "Mother_Name" : {
                "IsAlive": True
            }
        }
    },
    "Student2" : {
        "Name" : "Jayanta Samanta",
        "Age" : 22,
        "Ismaried" : True,
        "Parent" :{
            "Father_Name":{
                "IsAlive": False
            },
            "Mother_Name" : {
                "IsAlive": True
            }
        }
    }
}

# print(students) # print whole dict of nested dict 
# How to access single key value pairs =>
# print(students["Student1"]["Parent"]["Father_Name"]["IsAlive"])

# -------------------------------------------------------------

# Dictionary comprehension 
# How?=>
# Syntax ={key_expression : value_expression for item in iterable if condition }

# Square = {X: X **2 for X in range(1,10) if X%2==0}
# print(f" Square of Even values => {Square}")
# output=>  Square of Even values => {1: 4, 3: 16, 5: 36, 7: 64}

# problem solved  using enumerate(iterable,start=0) with list comprehension
# but i want like this output => {1: 4, 2: 16, 3: 36, 4: 64}

Square2 = {i+1: X**2 for i, X in enumerate([x for x in range(1, 10) if x % 2 == 0])}
print(Square2)

