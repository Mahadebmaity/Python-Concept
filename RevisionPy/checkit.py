def get_student_data():
    while(line:=input("Enter Student name:(To stop Enter name write 'exit'):: "))!="Exit".lower():
        roll = int(input("Enter roll no:"))
        dictionary = []
        dictionary.append({
            "Name of the student": line,
            f"Roll of {line}": roll
        })
    return dictionary

print(get_student_data())


    # print(f"Name of the student:{line}\nRoll of {line}: {roll}")







