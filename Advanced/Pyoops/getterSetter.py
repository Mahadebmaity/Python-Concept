''''
#Here I use single underscore to convention on protection age this can directly access  and using getter and setter method 
class getterSetter:

    def __init__(self,age = 0):
        self._age = age
    
    #getter method 
    def get_age(self):
        return self._age

    #setter method 
    def set_age(self,x):
        self._age = x

obj = getterSetter()
obj.set_age(21)
print(obj.get_age())
print(obj._age)
'''

'''
# here i use double under(__) score  to avoid accidental direct access the age 
class Myclass:

    def __init__(self,age =0):
        self.__age = age 
    
    def get_age(self):
        return self.__age
    
    def set_age(self,value):
        self.__age = value

obj = Myclass()
obj.set_age(45)
print(f"This is get a age using get method : {obj.get_age()}")
print(f"This is directly access the age : {obj.__age}") 
'''


# above coding explanation is one way to use getter and setter method 
# below coding is another way to use  getter and setter method 

'''
class Property:
    def __init__(self):
        self._age = 0
    
    def get_age(self):
        print("Getter method called")
        return self._age
    
    def set_age(self,a):
        print("Setter method called")
        self._age = a
    
    def del_age(self):
        del self._age
    
    age = property(get_age,set_age,del_age)
obj = Property() # when object create then set age value is 0 after that 
obj.age = 34 #  when instance value assign then call setter method  using property  function 
print(obj.age) #when print age call get method and del method 

'''


# above coding explanation is one way to use getter and setter method 
# below coding is another way to use  getter and setter method 
# today python new features are used to another style getter and setter method to access value 
# Using @property decorators
# In this approach, the @property decorator is used for the getter 
# and the @<property_name>.setter decorator is used for the setter.
#  This approach allows a more elegant way to define getter and setter methods.

class Decorators:
    def __init__(self):
        self._age = 0
    
    @property
    def age(self):
        print("Getter method called")
        return self._age
    
    @age.setter
    def age(self,a):
        if (a < 18):
            raise ValueError("Sorry your age is below eligibility criteria ")
        print("setter method called")
        self._age = a
             

obj= Decorators()
obj.age = 12
print(obj.age)
