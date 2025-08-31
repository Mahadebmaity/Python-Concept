class employee:
    language = "python",  # and salary and language is a class attribute 
    salary = 1200000

    def __init__(self,name,language,salary):# this is a dunder method which is automatically called when any object call 
        self.name = name 
        self.language = language
        self.salary = salary
        print(" Hi I am creating a  class value...")

    def getinfo(self):
        print(f"The language is : {self.language} , and salary is : {self.salary}")
    
    @staticmethod # for  no need to pass object  below this method greet()
    def greet():
        print("Hello , Good Morning")



obj = employee('debotosh',"golang", 1500000)
print(obj.name,obj.language,obj.salary)


# obj.getinfo() #both line are same  employee.getinfo(obj) 
# employee.greet(obj)

# obj.greet()




# Mahadeb = employee()
# Mahadeb.language = "Java" # here this is a instance attribute  it is first priority to print  program and get output 
# Mahadeb.name = "Mahadeb" # Here  name is a object attribute
# print(Mahadeb.name,Mahadeb.language, Mahadeb.salary)

# Jayanta = employee()
# Jayanta.name = "Jayanta"
# print(Jayanta.name,Jayanta.salary,Jayanta.language)



