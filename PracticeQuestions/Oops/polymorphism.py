# 3. Polymorphism
# Write a function show_vehicle_details() that takes a list of Vehicle objects and calls their display() — demonstrating polymorphism.

# Implement method overloading using default arguments or *args (Python doesn’t have built-in overloading).


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display(self):
        print(f"Vehicle: {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def display(self):
        print(f"Car: {self.make} {self.model}, Doors: {self.doors}")

class Bike(Vehicle):
    def __init__(self, make, model, cc):
        super().__init__(make, model)
        self.cc = cc

    def display(self):
        print(f"Bike: {self.make} {self.model}, Engine: {self.cc}cc")

# ✅ Polymorphic function
def show_vehicle_details(vehicles):
    for vehicle in vehicles:
        vehicle.display()

# 🔍 Testing
vehicles = [
    Car("Toyota", "Corolla", 4),
    Bike("Yamaha", "R15", 155),
    Car("Honda", "Civic", 4)
]

# show_vehicle_details(vehicles)


# Implement method overloading using default arguments or *args (Python doesn’t have built-in overloading).
#implement method overloading using default argument

class calculator:
    def add(self,a=2,b=3,c=4):
        return a+b+c

# calc = calculator()
# print(calc.add())
# print(calc.add(1))
# print(calc.add(1,2))
# print(calc.add(1,2,3))

#implement method overloading using *args  and method 

class calculator:
    def add(self,*args):
        return sum(args)

calc = calculator()
# print(calc.add()) #output:0
# print(calc.add(1)) #output:1
# print(calc.add(1,2)) #output:3
# print(calc.add(1,2,3)) #output:6
