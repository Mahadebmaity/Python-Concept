# 1.
# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
f = open("poems.txt")
c = f.read()
if "twinkle" in c:
    print("Yes, twinkle is in this file.")
else:
    print("No, twinkle is not in this file.")
    print(f"This is the file content ->\n{c}")

f.close()
