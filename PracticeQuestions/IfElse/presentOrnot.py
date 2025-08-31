# Write a program which finds out whether a given name is present in a list or not.

name = ["mahadeb", "jayanta", "biswajit", "sourav", "naren"]

check_name = input("Enter a name to check: ")
if check_name in name:
    print(f"{check_name} is present in the list.")
else:
    print(f"{check_name} is not present in the list.")
    