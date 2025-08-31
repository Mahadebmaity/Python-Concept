#  2. Inheritance
# Create a base class Vehicle with attributes make, model, year. Add a display() method.

# Create a child class Car inheriting Vehicle with an extra attribute number_of_doors. Override display() to include doors.

# Add a child class ElectricCar with an attribute battery_capacity. Override display() to show all details.

class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model =model
        self.year = year 

    def display(self):
        print(f"Brand Name:{self.make}\nModel Name:{self.model}\nYear of manufacturing:{self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year,number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors
    
    def display(self):
        super().display()
        print(f"Number of Doors: {self.number_of_doors}")

class ElectricCar(Car):
    def __init__(self, make, model, year, number_of_doors,battery_capacity):
        super().__init__(make, model, year, number_of_doors)
        self.battery_capacity =battery_capacity

    def display(self):
        super().display()
        print(f"Battery Capacity: {self.battery_capacity} kWh")


veh1 = Vehicle("Tata","civic",2019)
veh1.display()
car1 =Car("Honda","nexon",2018,4)
car1.display()
e1 = ElectricCar("Tesla", "Model S", 2023, 4, 100)
e1.display()

