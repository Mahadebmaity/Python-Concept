class employee:
    company ="ITC"

    def show(self):
        print(f"Name of the company:{self.company}")
    
class Coder:
    Language = "python"
    def showLanguage(self):
        print(f"{self.Language} is in the inside of Coder parent class")

class Programmer(employee,Coder):
    company ="ITC_InfoTech"
    def printLanguage(self):
        print(f"Company name is :{self.company} and lauguage use {self.Language}")
    

P = Programmer()
P.show()
P.showLanguage()
P.printLanguage()
# yeh hay multiple inheritance in oops 

