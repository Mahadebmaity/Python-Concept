# Write a class “Calculator” capable of finding square, cube and square root of a number.
class Calculator:
    def __init__(self,n):
        self.n = n 

    def square(self):
        print(f"The square of a {self.n} is : {self.n* self.n}")
    def cube(self):
        print(f"The cube of a {self.n} is : {self.n* self.n *self.n}")
    def squareroot(self):
        print(f"The squareroot of a {self.n} is : {self.n**1/2}")
    
    @staticmethod
    def great():
        print(" Calculate in the progress.")

# obj = Calculator(4)
# obj.great()
# obj.square()
# obj.cube()
# obj.squareroot()



# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?
# class Myclass:
#     a = 10

# obj = Myclass()
# print(Myclass.a)
# print(obj.a)
# obj.a = 0
# print(Myclass.a)
# print(obj.a)


