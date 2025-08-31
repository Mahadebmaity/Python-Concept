import os  # To work with files like checking if a file exists

# ---------- Base Class ----------
class Person:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self.age = age    # Public attribute

    def show_info(self):
        return f"Name: {self.name}, Age: {self.age}"


# ---------- Student Class ----------
class Student(Person):
    student_count = 0  # Class variable to count students

    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call Person class constructor
        self.student_id = student_id
        self.__grades = {}       # Private dictionary to store grades
        self.__promoted = False  # Initially not promoted

        Student.student_count += 1  # Count this student

        # Load grades from file if it already exists
        filename = f"grades_{self.student_id}.txt"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                for line in f:
                    try:
                        sub, grd = line.strip().split(":")
                        self.__grades[sub.strip()] = int(grd.strip())
                    except:
                        continue  # Skip bad lines

        # Save/update student info in students.txt file
        student_data = {}
        if os.path.exists("students.txt"):
            with open("students.txt", "r") as f:
                for line in f:
                    sid, sname, sage = line.strip().split(",")
                    student_data[sid] = (sname, sage)

        # Update or add this student
        student_data[self.student_id] = (self.name, self.age)

        # Rewrite the whole file to avoid duplicates
        with open("students.txt", "w") as f:
            for sid, (sname, sage) in student_data.items():
                f.write(f"{sid},{sname},{sage}\n")


    def add_grade(self, subject, grade):
        self.__grades[subject] = grade  # Add/Update grade
        # Save grades to file
        with open(f"grades_{self.student_id}.txt", "w") as f:
            for sub, grd in self.__grades.items():
                f.write(f"{sub}: {grd}\n")

    def view_grades(self):
        print(f"\nGrades for {self.name}:")
        if self.__grades:
            for subject, grade in self.__grades.items():
                print(f"{subject}: {grade}")
        else:
            print("No grades assigned yet.")

    def promote(self):
        if self.__grades:
            avg = sum(self.__grades.values()) / len(self.__grades)
            self.__promoted = avg >= 40  # Promotion rule
            if self.__promoted:
                print(f"{self.name} has been promoted.")
            else:
                print(f"{self.name} has not been promoted.")
        else:
            print("No grades to evaluate promotion.")

    @classmethod
    def total_students(cls):
        return cls.student_count  # Class method to get total students



# ---------- Teacher Class ----------
class Teacher(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)  # Call Person constructor
        self.emp_id = emp_id

        # Update teacher info in file
        teacher_data = {}
        if os.path.exists("teachers.txt"):
            with open("teachers.txt", "r") as f:
                for line in f:
                    tid, tname, tage = line.strip().split(",")
                    teacher_data[tid] = (tname, tage)

        # Add or update this teacher
        teacher_data[self.emp_id] = (self.name, self.age)

        # Save to file without duplicates
        with open("teachers.txt", "w") as f:
            for tid, (tname, tage) in teacher_data.items():
                f.write(f"{tid},{tname},{tage}\n")

    def assign_grade(self, student, subject, grade):
        if isinstance(student, Student):
            student.add_grade(subject, grade)
            print(f"{self.name} assigned grade {grade} in {subject} to {student.name}")

    @staticmethod
    def school_motto():
        return "Knowledge is Power!"  # Static method, no need for self


# ---------- MAIN MENU ----------
students = {}  # Dictionary to store students in current session
teachers = {}  # Dictionary to store teachers in current session

def main():
    while True:
        print("\n----- School Management System -----")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Assign Grade")
        print("4. View Student Grades")
        print("5. Promote Student")
        print("6. Total Students (Current Session)")
        print("7. Show School Motto")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter age: "))
            sid = input("Enter student ID: ")
            students[sid] = Student(name, age, sid)
            print(f"Student {name} added.")

        elif choice == '2':
            name = input("Enter teacher name: ")
            age = int(input("Enter age: "))
            tid = input("Enter teacher ID: ")
            teachers[tid] = Teacher(name, age, tid)
            print(f"Teacher {name} added.")

        elif choice == '3':
            tid = input("Enter teacher ID: ")
            sid = input("Enter student ID: ")
            subject = input("Enter subject: ")
            grade = int(input("Enter grade (0-100): "))

            teacher = teachers.get(tid)
            student = students.get(sid)

            if teacher and student:
                teacher.assign_grade(student, subject, grade)
            else:
                print("Invalid teacher or student ID.")

        elif choice == '4':
            sid = input("Enter student ID: ")
            student = students.get(sid)
            if student:
                student.view_grades()
            else:
                print("Student not found in current session.")

        elif choice == '5':
            sid = input("Enter student ID: ")
            student = students.get(sid)
            if student:
                student.promote()
            else:
                print("Student not found in current session.")

        elif choice == '6':
            print(f"Total Students (this session): {Student.total_students()}")

        elif choice == '7':
            print(f"School Motto: {Teacher.school_motto()}")

        elif choice == '8':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1-8.")

# Only run the app if it's the main program
if __name__ == "__main__":
    main()
