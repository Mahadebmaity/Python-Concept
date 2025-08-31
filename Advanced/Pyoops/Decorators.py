class employee:
    # company = " IBM"
    salary = 12000
    @classmethod
    def company(cls):
        print(f"Get In hand salary :{cls.salary}")
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

    
P = employee()
P.name  = "Mahadeb Maity"
print(P.fname ,P.lname)

P.company()

# P.salary = 13000
# P.company()
