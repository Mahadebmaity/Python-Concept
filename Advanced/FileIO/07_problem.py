'''
question: -- 
6.
Write a program to mine a log file and find out whether it contains ‘python’.
7.
Write a program to find out the line number where python is present from ques 6.
'''
'''
this is a first attempt code to and learning time then experimental and odubt solving myself
with open("Log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes python is present , Line no : {lineno}")
        continue
        
    lineno +=1
else:
    print("No python is not present.")
'''

'''
this is a final correction code fix the all bug

with open("Log.txt") as f:
    lines = f.readlines()

lineno = 1
line_numbers = []

for line in lines:
    if "python" in line:
        line_numbers.append(str(lineno))
    lineno += 1
    
if line_numbers:
    print(f"Yes, python is present on line no: {line_numbers}")
else:
    print("No, python is not present.")
''' 

''' 
this is a testing of fix all bug and successfully donr my code and my self doubt 

with open("Log.txt") as f:
    lines = f.readlines()

lineno = 1
line_numbers = []

for line in lines:
    if "python" in line:
        line_numbers.append(str(lineno))
    lineno += 1

if line_numbers:
    print(" ".join(line_numbers))
else:
    print("Not found")
'''

    