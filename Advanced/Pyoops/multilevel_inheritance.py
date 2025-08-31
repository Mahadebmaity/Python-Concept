class employee:
    company ="ITC"

    def show(self):
        print(f" This is a employee claas and there -> Name of the company:{self.company}")
    
class Coder(employee):
    Language = "python"
    def showLanguage(self):
        print(f"{self.Language} is in the inside of Coder parent class")

class Programmer(Coder):
    company ="ITC_InfoTech"
    def printLanguage(self):
        print(f"Company name is :{self.company} and lauguage use {self.Language}")
    
P = Programmer()
P.printLanguage()
P.showLanguage()
P.show()


