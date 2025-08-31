# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.
class Animal:
    pass

class Pets(Animal):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!")

D = Dog()
D.bark()
