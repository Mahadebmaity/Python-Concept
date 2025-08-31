#!/usr/bin/env python3
"""
Main CLI for School Student Management System
"""
import sys
import getpass
from tabulate import tabulate
from colorama import init as color_init, Fore, Style
from database import (
    init_db, authenticate_admin, change_admin_password, add_student,
    update_student, delete_student, list_all_students, list_class_students,
    get_student_by_reg, set_subjects, get_subjects, import_students_from_csv,
    subject_statistics, top_n_toppers, search_students
)
from report_generator import export_class_csv, export_class_excel, export_class_pdf
from utils import ensure_backup

color_init(autoreset=True)
init_db()  # create DB & tables if not exist

def safe_input(prompt):
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\nExiting safely.")
        sys.exit(0)

def login_flow():
    print(Fore.CYAN + "Admin Login")
    for _ in range(3):
        username = safe_input("Username: ").strip()
        
        try:
            password = safe_input("Password: ").strip()

        except (KeyboardInterrupt, EOFError):
            print("\nLogin cancelled.")
            sys.exit(0)

        if authenticate_admin(username, password):
            print(Fore.GREEN + "Login successful.\n")
            return True
        else:
            print(Fore.RED + "Invalid credentials. Try again.\n")

    print(Fore.RED + "Too many failed attempts. Exiting.")
    return False


def interactive_menu():
    while True:
        print(Style.BRIGHT + Fore.YELLOW + "------ SCHOOL STUDENT MANAGEMENT SYSTEM ------")
        print("1. Entry student data")
        print("2. Show student data class wise")
        print("3. Specific student wise")
        print("4. Update student details")
        print("5. Delete student")
        print("6. List all students")
        print("7. Enter/Update subject names")
        print("8. Import students from CSV")
        print("9. Reports (CSV/Excel/PDF) for a class")
        print("10. Subject-wise statistics & Top N")
        print("11. Change admin password")
        print("12. Search students")
        print("13. Exit system")

        choice = safe_input("Enter your choice: ").strip()
        if choice == "1":
            ensure_backup()
            add_student_interactive()
        elif choice == "2":
            show_class()
        elif choice == "3":
            show_student()
        elif choice == "4":
            ensure_backup()
            update_student_interactive()
        elif choice == "5":
            ensure_backup()
            delete_student_interactive()
        elif choice == "6":
            list_all()
        elif choice == "7":
            subjects = safe_input("Enter subjects separated by comma (e.g. Math,English,Science): ")
            sub_list = [s.strip() for s in subjects.split(",") if s.strip()]
            if sub_list:
                set_subjects(sub_list)
                print(Fore.GREEN + "Subjects updated.")
            else:
                print(Fore.RED + "No valid subjects provided.")
        elif choice == "8":
            path = safe_input("Enter CSV filepath to import: ").strip()
            try:
                imported = import_students_from_csv(path)
                print(Fore.GREEN + f"Imported {imported} students (duplicates skipped).")
            except Exception as e:
                print(Fore.RED + f"Import failed: {e}")
        elif choice == "9":
            cls = safe_input("Enter class name: ").strip()
            try:
                export_class_csv(cls)
                export_class_excel(cls)
                export_class_pdf(cls)
                print(Fore.GREEN + f"Reports exported for class '{cls}'.")
            except Exception as e:
                print(Fore.RED + f"Report export error: {e}")
        elif choice == "10":
            cls = safe_input("Enter class name: ").strip()
            try:
                stats = subject_statistics(cls)
                if not stats:
                    print(Fore.RED + "No data for that class.")
                else:
                    for sub, s in stats.items():
                        print(f"\nSubject: {sub}")
                        print(tabulate([["Average", s['avg']], ["Highest", s['max']], ["Lowest", s['min']], ["Topper", s['topper_name'] or "N/A"]], tablefmt="plain"))
                    n = safe_input("Show top N toppers? Enter N (or blank): ").strip()
                    if n.isdigit():
                        toppers = top_n_toppers(cls, int(n))
                        print("\nTopper List:")
                        print(tabulate([[t['rank'], t['name'], t['reg_no'], t['total'], f"{t['percentage']:.2f}%"] for t in toppers],
                                       headers=["Rank", "Name", "Reg No", "Total", "Percentage"]))
            except Exception as e:
                print(Fore.RED + f"Error: {e}")
        elif choice == "11":
            user = safe_input("Admin username: ").strip()
            old = getpass.getpass("Current password: ").strip()
            new = getpass.getpass("New password: ").strip()
            confirm = getpass.getpass("Confirm new password: ").strip()
            if new != confirm:
                print(Fore.RED + "New passwords don't match.")
            else:
                try:
                    change_admin_password(user, old, new)
                    print(Fore.GREEN + "Password changed.")
                except Exception as e:
                    print(Fore.RED + f"Password change failed: {e}")
        elif choice == "12":
            q = safe_input("Search by name/roll/reg (partial allowed): ").strip()
            results = search_students(q)
            if not results:
                print(Fore.RED + "No students found.")
            else:
                print(tabulate([[r['class'], r['name'], r['roll'], r['reg_no'], f"{r['percentage']:.2f}%"] for r in results],
                               headers=["Class", "Name", "Roll", "Reg No", "Percentage"]))
        elif choice == "13":
            print(Fore.CYAN + "Exiting. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Try again.")

def add_student_interactive():
    try:
        cls = safe_input("Enter class: ").strip()
        name = safe_input("Enter student name: ").strip()
        roll = safe_input("Enter roll number: ").strip()
        # add_student performs validation internally
        reg = add_student(cls, name, roll)
        print(Fore.GREEN + f"Student added with Reg No: {reg}")
    except Exception as e:
        print(Fore.RED + f"Failed to add student: {e}")

def update_student_interactive():
    try:
        reg = safe_input("Enter Reg No to update: ").strip()
        ok = update_student(reg)
        if ok:
            print(Fore.GREEN + "Student updated.")
        else:
            print(Fore.RED + "Update failed or student not found.")
    except Exception as e:
        print(Fore.RED + f"Error updating student: {e}")

def delete_student_interactive():
    try:
        reg = safe_input("Enter Reg No to delete: ").strip()
        ok = delete_student(reg)
        if ok:
            print(Fore.GREEN + "Deleted.")
        else:
            print(Fore.RED + "Delete failed or student not found.")
    except Exception as e:
        print(Fore.RED + f"Error deleting student: {e}")

def show_class():
    cls = safe_input("Enter class name: ").strip()
    students = list_class_students(cls)
    if not students:
        print(Fore.RED + "No students in that class.")
        return
    headers = ["Reg No", "Name", "Roll", "Total", "Percentage", "Grade", "Status", "Rank"]
    table = [[s['reg_no'], s['name'], s['roll'], s['total'], f"{s['percentage']:.2f}%", s['grade'], s['status'], s.get('rank')] for s in students]
    print(tabulate(table, headers=headers))

def show_student():
    reg = safe_input("Enter Reg No: ").strip()
    s = get_student_by_reg(reg)
    if not s:
        print(Fore.RED + "Student not found.")
        return
    print(Fore.GREEN + f"\nStudent: {s['name']} (Class: {s['class']})")
    print(tabulate([[sub, mark] for sub, mark in s['marks'].items()], headers=["Subject", "Marks"]))
    print(tabulate([["Total", s['total']], ["Max", len(s['marks'])*100], ["Percentage", f"{s['percentage']:.2f}%"], ["Grade", s['grade']], ["Status", s['status']], ["Rank", s.get('rank')]], tablefmt="plain"))

def list_all():
    all_students = list_all_students()
    if not all_students:
        print(Fore.RED + "No students found.")
        return
    print(tabulate([[s['class'], s['reg_no'], s['name'], s['roll'], f"{s['percentage']:.2f}%"] for s in all_students],
                   headers=["Class", "Reg No", "Name", "Roll", "Percentage"]))

if __name__ == "__main__":
    if login_flow():
        interactive_menu()

        
