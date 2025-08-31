# 6. Operator Overloading
# Create a class Point with x and y. Overload:

# + operator to add two points.

# str method to display point nicely.

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    # overloading + operator
    def __mul__(self,other):
        return point(self.x * other.x, self.y * other.y)
    
    # overloading str() fnc
    def __str__(self):
        return f"point({self.x},{self.y})"
    
# testing the point class
p1 = point(4,6)
p2 = point(5,8)
result = p1 * p2

print(f"point 1:",p1)
print(f"point 2:",p2)
print(f"mul of :",result)

