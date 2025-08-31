#  9. Composition
# Create Employee and Address classes. An Employee should contain an Address. Print employee details with address.

# at first discuss Composition then solve it 

class Address:
    def __init__(self,street,city,state,pin):
        self.street = street
        self.city = city
        self.state = state
        self.pin = pin 
    
    def get_address(self):
        return f"{self.street},{self.city},{self.state}- {self.pin}"

class Employee:
    def __init__(self,name,emp_id,address):
        self.name = name
        self.emp_id = emp_id
        self.address = address # use here composition
    
    def show_details(self):
        print("Employee Details:")
        print(f"Name    : {self.name}")
        print(f"Emp ID  : {self.emp_id}")
        print(f"Address : {self.address.get_address()}")


# create Address object
Address1 = Address("124 kerani tala","Kolkata","West Bengal","725600")

#create Employee object with address class object 
Employee1 = Employee("Mahadeb","E1098",Address1)

# display employee details
Employee1.show_details()
