# Function decorator function 
def simple_decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@simple_decorator
def greet():
    print("Hello, World!")

greet()
# method decorator function 
def decorator(func):
    def wrapper(*args,**kwargs):
        print("Before calling function")
        func(*args,**kwargs)
        print("After calling function")
    return wrapper

class Decorator:
    @staticmethod
    @decorator #Applying the decorator  to a function
    def greet():
        print("Hello! Mahadeb")

obj = Decorator()
obj.greet()

# class decorator 

