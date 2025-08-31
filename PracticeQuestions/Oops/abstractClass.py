# this is learning base code 

# from abc import ABC,abstractmethod

# class car(ABC):
#     @staticmethod
#     def show():
#         print("Every car have 4 wheels")
    
#     @staticmethod
#     @abstractmethod
#     def speed():
#         pass

# class Maruti(car):
#     @staticmethod
#     def speed():
#         print("Maruti speed is 100 km/h")
# class Suzuki(car):
#     @staticmethod
#     def speed():
#         print("Suzuki speed is 70 km/h")
    
# maruti = Maruti()
# suzuki = Suzuki()
# maruti.show()
# maruti.speed()
# suzuki.show()
# suzuki.speed()

# this is practice base mode

# 5. Abstraction
# Create an abstract class Shape with an abstract method area().

# Derive Rectangle and Circle classes from Shape and implement area() for each.

# Write code to create objects of Rectangle and Circle and calculate their areas.

from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area():
        pass

class Rectangle(shape):
    def area(self,length,width):
        self.length = length
        self.width = width
        self.area = self.length * self.width
        print(f"Area of a Rectangle is:{self.area}")


class Circle(shape):
    def area(self,radius):
        self.radius = radius
        self.area = (22/7)*(self.radius**2)
        print(f"Area of a Circle is: {self.area}")
    
Rec = Rectangle()
Rec.area(20,10)
Cir = Circle()
Cir.area(5)

