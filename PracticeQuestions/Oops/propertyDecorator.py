#  8. Property Decorators
# Create a Temperature class:

# Store temperature in Celsius.

# Use @property to get Fahrenheit.

# Use setter to set Fahrenheit and update Celsius.

class Temperature:
    def __init__(self, Celsius):
        self._Celsius = Celsius

    @property
    def Fahrenheit(self):
        return (self._Celsius * 9/5) +32

    @Fahrenheit.setter
    def Fahrenheit(self, value):
        self._Celsius = (value -32)*5/9
    
    def __str__(self):
        return f"{self._Celsius:.2f}°C / {self.Fahrenheit:.2f}°F"

    
t = Temperature(25)
print("Initial:",t)

print("Fahrenheit", t.Fahrenheit)
t.Fahrenheit = 98.6
print("After setting Fahrenheit:", t)
# Using the property

