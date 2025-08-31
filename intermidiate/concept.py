# now i declear function
def sum():
    number = int(input("Enter the number: "))
    number2 = int(input("Enter the number2 : "))    
    print(f"Sum of two numbers: {number + number2}")

# sum()

def greet(name,question = "How are you bro? "):
    print(f"Hello! {name}")
    print(question)

greet("Mahadeb","how have you been?")



