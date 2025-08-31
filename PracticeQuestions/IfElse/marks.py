# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
'''
Math = int(input("Enter your Math subject marks: "))
physics = int(input("Enter your Physics subject marks: "))
chemistry = int(input("Enter your Chemistry subject marks: "))

Math_percentage = (Math / 100) * 100
physics_percentage = (physics / 100) * 100
chemistry_percentage = (chemistry / 100) * 100
total_marks = Math + physics + chemistry
percentage = (total_marks / 300) * 100

if Math_percentage >= 33 and physics_percentage >= 33 and chemistry_percentage >= 33  and percentage >= 40:
    print(f" Congratulations Mr./Mrs. You are passed The exam,your total marks is:{total_marks} and your persentage is : {percentage}%")
else:
    print(f"Sorry Mr./Mrs. You are failed The exam. Your total marks is: {total_marks} and your percentage is: {percentage}% below the passing criteria, which is 40%, and each subject must be at least 33%.")
    print("Please try again next time.")
'''
# End of the code
# here code is better structured and conditions are clearly defined for passing criteria.
Math = int(input("Enter your Math subject marks: "))
physics = int(input("Enter your Physics subject marks: "))
chemistry = int(input("Enter your Chemistry subject marks: "))

Math_percentage = (Math / 100) * 100
physics_percentage = (physics / 100) * 100
chemistry_percentage = (chemistry / 100) * 100

total_marks = Math + physics + chemistry
percentage = (total_marks / 300) * 100

if Math_percentage >= 33 and physics_percentage >= 33 and chemistry_percentage >= 33 and percentage >= 40:
    print(f"Congratulations Mr./Mrs.! You passed the exam. Your total marks are: {total_marks} and your percentage is: {percentage}%.")
else:
    print(f"Sorry Mr./Mrs.! You failed the exam.")
    print(f"Your total marks are: {total_marks} and your percentage is: {percentage}%.")
    print("Reasons for failure (or pass status per subject):")
    if Math_percentage < 33:
        print(f"- Math marks are below passing: {Math} ({Math_percentage}%)")
    else:
        print(f"- Math marks are fine: {Math} ({Math_percentage}%)")
    
    if physics_percentage < 33:
        print(f"- Physics marks are below passing: {physics} ({physics_percentage}%)")
    else:
        print(f"- Physics marks are fine: {physics} ({physics_percentage}%)")
    
    if chemistry_percentage < 33:
        print(f"- Chemistry marks are below passing: {chemistry} ({chemistry_percentage}%)")
    else:
        print(f"- Chemistry marks are fine: {chemistry} ({chemistry_percentage}%)")
    
    if percentage < 40:
        print(f"- Overall percentage is below passing criteria: {percentage}% < 40%")
    else:
        print(f"- Overall percentage is fine: {percentage}%")
    
    print("Please try again next time.")
# The code has been structured to clearly define the passing criteria and provide detailed feedback on each subject's performance.
