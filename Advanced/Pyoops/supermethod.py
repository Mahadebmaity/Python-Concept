class employee:
    company ="ITC"
    def __init__(self):
        print("I am a Constructor of employee class.")

    def show(self):
        print(f" This is a employee claas and there -> Name of the company:{self.company}")
    
class Coder(employee):
    Language = "python"

    def __init__(self):
        super().__init__()
        print("I am a Constructor of Coder class.")

    def showLanguage(self):
        print(f"{self.Language} is in the inside of Coder parent class")

class Programmer(Coder):
    company ="ITC_InfoTech"

    def __init__(self):
        super().__init__()
        print("I am a Constructor of Programmer class.")

    def printLanguage(self):
        print(f"Company name is :{self.company} and lauguage use {self.Language}")
    
P = Programmer()
P.printLanguage()
P.showLanguage()
P.show()


