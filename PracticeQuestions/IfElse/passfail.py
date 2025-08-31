Student_name = input("Enter your name: ")
marks = int(input("Enter student marks: "))

if marks >= 90 and marks <=100:
    print("Grade: Ex")
    print(f"{Student_name} has passed with distinction")
elif marks >= 75 and marks < 90:
    print("Grade: A")
    print(f"{Student_name} has passed with first class")
elif marks >= 60 and marks < 75:
    print("Grade: B")
    print(f"{Student_name} has passed with second class")
elif marks >= 50 and marks < 60:
    print("Grade: C")
    print(f"{Student_name} has passed with third class")
elif marks >= 40 and marks < 50:
    print("Grade: D")
    print(f"{Student_name} has passed")
else:
    print("Grade: F")
    print(f"{Student_name} has failed")


# Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Enter a post: ")
if "Harry" in post:
    print("The post is talking about Harry.")   
else:
    print("The post is not talking about Harry.")



