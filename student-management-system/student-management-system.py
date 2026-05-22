# =====================================================
# MODERATE LEVEL STUDENT MANAGEMENT SYSTEM
# =====================================================

import json
import os

FILE_NAME = "students.json"


# =====================================================
# LOAD STUDENT DATA
# =====================================================
def load_students():

    if os.path.exists(FILE_NAME):

        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)

        except:
            return {}

    return {}


# =====================================================
# SAVE STUDENT DATA
# =====================================================
def save_students(students):

    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


students = load_students()


# =====================================================
# ADD STUDENT
# =====================================================
def add_student():

    roll = input("\nEnter Roll Number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    phone = input("Enter Phone Number: ")

    try:
        marks = float(input("Enter Marks: "))
    except:
        print("Invalid marks input!")
        return

    # Grade Calculation
    if marks >= 90:
        grade = "A"

    elif marks >= 75:
        grade = "B"

    elif marks >= 50:
        grade = "C"

    else:
        grade = "Fail"

    students[roll] = {

        "Name": name,
        "Age": age,
        "Course": course,
        "Phone": phone,
        "Marks": marks,
        "Grade": grade

    }

    save_students(students)

    print("\nStudent added successfully!")


# =====================================================
# DISPLAY ALL STUDENTS
# =====================================================
def display_students():

    if not students:
        print("\nNo student records found!")
        return

    print("\n========== STUDENT RECORDS ==========")

    for roll, details in students.items():

        print(f"\nRoll Number : {roll}")

        for key, value in details.items():
            print(f"{key} : {value}")

        print("---------------------------------")


# =====================================================
# SEARCH STUDENT
# =====================================================
def search_student():

    roll = input("\nEnter Roll Number to Search: ")

    if roll in students:

        print("\nStudent Found!")

        for key, value in students[roll].items():
            print(f"{key} : {value}")

    else:
        print("Student not found!")


# =====================================================
# UPDATE STUDENT
# =====================================================
def update_student():

    roll = input("\nEnter Roll Number to Update: ")

    if roll not in students:
        print("Student not found!")
        return

    print("\nEnter New Details")

    students[roll]["Name"] = input("Enter New Name: ")
    students[roll]["Course"] = input("Enter New Course: ")
    students[roll]["Phone"] = input("Enter New Phone Number: ")

    try:
        marks = float(input("Enter New Marks: "))
        students[roll]["Marks"] = marks

        if marks >= 90:
            students[roll]["Grade"] = "A"

        elif marks >= 75:
            students[roll]["Grade"] = "B"

        elif marks >= 50:
            students[roll]["Grade"] = "C"

        else:
            students[roll]["Grade"] = "Fail"

    except:
        print("Invalid marks input!")

    save_students(students)

    print("\nStudent updated successfully!")


# =====================================================
# DELETE STUDENT
# =====================================================
def delete_student():

    roll = input("\nEnter Roll Number to Delete: ")

    if roll in students:

        del students[roll]

        save_students(students)

        print("Student deleted successfully!")

    else:
        print("Student not found!")


# =====================================================
# MAIN MENU
# =====================================================
while True:

    print("\n======================================")
    print("    STUDENT MANAGEMENT SYSTEM")
    print("======================================")

    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":

        print("\nThank You for Using the System!")
        break

    else:
        print("\nInvalid choice! Please try again.")