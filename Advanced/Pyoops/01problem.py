# Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    company = "Microsoft"
    def __init__(self, name , salary , pin):
        self.name = name
        self.salary = salary
        self.pin = pin 
    
Mahadeb = Programmer("Mahadeb Maity", 1600000, 721467)
print(f"Company Name: {Mahadeb.company}\nName of the Employee:{Mahadeb.name}\nAnd his salary is:{Mahadeb.salary}\nhis pin code:{Mahadeb.pin}")

