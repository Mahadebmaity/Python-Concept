f = open("file.txt")
# lines = f.readlines()
# print(lines, type(lines))
# singleLine = f.readline()
# print(singleLine, type(singleLine))
# singleLine = f.readline()
# print(singleLine, type(singleLine))
# singleLine = f.readline()
# print(singleLine, type(singleLine))
# singleLine = f.readline()
# print(singleLine, type(singleLine))
# singleLine = f.readline()
# print(singleLine, type(singleLine))
# singleLine = f.readline()
# print(singleLine == "")
# f.close()

# same code write advanced process
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close() 
