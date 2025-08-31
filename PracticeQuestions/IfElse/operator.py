a = 10000000
b = 10000000
print(a is b)  # Might be False — because big integers aren’t always cached
print(a is not b)
