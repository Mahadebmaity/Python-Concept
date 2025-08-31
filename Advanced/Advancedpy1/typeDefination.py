# Type Definition 
age :int = 20 # variable type deff

# function type deff 
def greet(Name:str,age:int) -> str:
    return f"Hello, {Name}! are you {age} years old?"

# print(greet("Mahadeb",age))

# this is advanced hint in  python 

from typing import List, Tuple, Dict, Set

Numbers: List[int] = [1,2,3,5,6,7]
# numbers: List[int] = [1, 2, 3]
pair: Tuple[str, int] = ("Age", 25, "roll", 10)
person: Dict[str, str] = {"name": "Alice"}
unique_ids: Set[int] = {1, 2, 3}

print(Numbers, type(Numbers))
print(pair,type(pair))
print(person , type(person))
print(unique_ids , type(unique_ids))

