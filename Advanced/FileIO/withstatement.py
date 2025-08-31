f = open("file.txt")
print(f.read())
f.close()

# same code write using with statement 
with open("file.txt") as f:
    print(f.read())
# The best way to open and close the file automatically is the with statement.
