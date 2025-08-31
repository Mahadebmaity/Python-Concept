class employee:
    company = "ITC"
    name = "mahadeb"
    def show(self):
        print(f"Name of the company is:{self.company}\nName of the employee:{self.name}")
    
class Programmer(employee):
    pass
    company = "ITC-Infotech"
    # name ="Jayanta"
    def show(self):
        print(f"Name of the company is:{self.company}\nName of the employee:{self.name}")
        super().show()

    
Progobj = Programmer()
Progobj.show()
# Progobj.showskill()



