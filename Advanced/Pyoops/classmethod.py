class employee:
    # company = " IBM"
    salary = 12000
    @classmethod
    def company(cls):
        print(f"In hand salary :{cls.salary} of every employees")
    
P = employee()
P.salary = 13000
P.company()
