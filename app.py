import os
from datetime import datetime
import sys

students = {

}
courses = {

}
grades = {

}

def add_students():
    sid = (input("Enter student ID: ")).strip().upper()

    if sid in students.keys() or sid.isalnum() == False:
        return print("ID already exists or it's not alphanumeric")

    name = input("Enter student name: ").strip().upper()

    if name.replace(" ","").isalpha() == False:
        return print("Name must be alpha")

    year = input("Enter year: ")

    if year.isdigit() == False or  not  (1 <= int(year) <= 5):
        return print("Year must be between 1 and 5")
    students[sid] = {}
    students[sid]["name"] = name
    students[sid]["year"] = year
    print(f"Student {name} added successfully")

def View_all_students():
    if  students == {}:
        print("Student list empty!")
        return
    for sid ,student in sorted(students.items()):
        print(f"ID : {sid}\tName : {student['name']}")
def Update_student_info():
    if students == {}:
        print("Student list empty!")
        return
    sid = input("Enter student ID: ").strip().upper()
    if not sid.isalnum() or sid not in students:
        return print("ID must be alphanumeric or sid isn't found")

    print(f"student name is {students[sid]['name']} and year is {students[sid]['year']} ")
    name = input("Enter new student name: ").strip().upper()
    if name :
        if name.replace(" ","").isalpha() == False:
            return print("Name must be alpha")
        students[sid]["name"] = name
    year = input("Enter new student year: ").strip().upper()
    if year:
        if year.isdigit() == False or not (1 <= int(year) <= 5):
            return print("Year must be between 1 and 5")
        students[sid]["year"] = year
    print(f"Student updated successfully")

def Delete_student():
    if students == {}:
        print("Student list empty!")
        return
    sid = input("Enter student ID: ").strip().upper()
    if not sid.isalnum() or sid not in students:
        return print("ID must be alphanumeric or sid isn't found")
    del students[sid]
    keys_to_remove = []
    for key in grades.keys():
        if key[0] == sid:
            keys_to_remove.append(key)
    for key in grades.keys():
        if key in keys_to_remove:
            del grades[key]
    print(" Student deleted successfully!")

def add_course():
    cid = input("Enter course ID: ").strip().upper()
    if not cid.isalnum() or cid in courses:
        return print("ID must be alphanumeric or course id already exists")

    name = input("Enter course name: ").strip().upper()
    if not name.replace(" ","").isalpha():
        return print("Name must be alpha")

    credit = input("Enter course credit: ").strip().upper()
    if  not credit.isdigit():
        return print("Course must be numeric")
    courses[cid] = {"name":name, "credit":credit}
    print(f"Course {name} added successfully")

def List_courses():
    if courses == {}:
        print("Course list empty!")
        return
    for cid,info in courses.items():
        print(f"ID :{cid}\tname :{info['name']}\tcredit :{info['credit']}")
def Delete_or_update_course():
    if courses == {}:
        print("Course list empty!")
        return

    cid = input("Enter course ID: ").strip().upper()
    if not cid.isalnum() or not cid in courses:
        return print("ID must be alphanumeric or course id already exists")
    choice = input("Take a choice\nchoice 1 : update course\nchoice 2 : Delete course")
    if choice == "1":
        name = input("Enter course name: ").strip().upper()
        if not name.replace(" ","").isalpha():
            return print("Course name must be alpha")
        courses[cid]["name"] = name
        credit = input("Enter course credit: ").strip().upper()
        if not credit.isdigit():
            return print("Course credit must be numeric")
        courses[cid]["credit"] = int(credit)
        print(f"Course {name} updated successfully")
    elif choice == "2":
        del courses[cid]
        print(f"Course {name} deleted successfully")
    else:
        print("number you choose is not valid")

def Enroll_student():
    if courses == {}:
        return print("Course list empty!")
    sid = input("Enter student ID: ").strip().upper()
    if not sid.isalnum() or not sid in students:
        return print("ID must be alphanumeric or sid isn't found")
    cid = input("Enter course ID: ").strip().upper()
    if not cid.isalnum() or not cid in courses:
        return print("ID must be alphanumeric or course id not found")
    if (sid,cid) in grades:
        return print("Student already enrolled")
    grades[(sid,cid)]= None

    print(f"Student {students[sid]["name"]} enrolled successfully in course {courses[cid]['name']}")

def Enter_or_update_grades():
    if grades == {}:
        return print("Course list empty!")
    sid = input("Enter student ID: ").strip().upper()
    if not sid.isalnum() or not sid in students:
        return print("ID must be alphanumeric or sid isn't found")
    cid = input("Enter course ID: ").strip().upper()
    if not cid.isalnum() or not cid in courses:
        return print("ID must be alphanumeric or course id not found")
    grade = input("Enter grade: ").strip().upper()
    if not grade.isdigit() or not int(grade) in range(0,21):
        return print("Grade must be between 0 and 20")
    courses[(sid,cid)] = int(grade)
    print(f"Grade updated successfully")

def View_student_grades():
    if not grades:
        return print("Course list empty!")
    sid = input("Enter student ID: ").strip().upper()
    if not sid.isalnum() or not sid in students:
        return print("ID must be alphanumeric or sid isn't found")
    avg = 0
    count = 0
    for key,grade in grades.items():
        if sid == key[0] and grade is not None:
            print(f"cid:{key[1]}\tcourse:{courses[key[1]]["name"]}\tgrade:{grade}")
            avg += grade
            count += 1
    if count == 0:
        return print("student has no grade")
    print(f"Average grade: {avg/count}")

def Delete_enrolment():
    if grades == {}:
        print("Course list empty!")
        return
    sid = input("Enter student ID: ").strip().upper()
    if not sid.isalnum() or not sid in students:
        return print("ID must be alphanumeric or sid isn't found")
    cid = input("Enter course ID: ").strip().upper()
    if not cid.isalnum() or not cid in courses:
        return print("ID must be alphanumeric or course id not found")
    for key in grades.keys():
        if (sid,cid) == key:
            del grades[key]
        else:
            print(f"Student are not enrolled")
            return
    print(f"Student enrolment deleted successfully")

def student_averge():
    if not students:
        return print("Student list empty!")
    if not grades:
        return print("grades list empty!")
    stu_avg = []
    for sid in students:
        count = 0
        avg = 0
        for key,grade in grades.items():
            if sid == key[0] and grade is not None:
                avg += grade
                count += 1
        if count == 0:
            pass
        stu_avg.append((students[sid]["name"],avg/count))
        print(f"Average grade of {students[sid]["name"]}: {avg/count}")
    return stu_avg


def course_averge():
    if not grades:
        return print("Grades list empty!")
    temgrades = {}
    for key in courses:
        count = 0
        avg = 0
        for id,grade in grades.items():
            if key == id[1] and grade is not None:
                avg += grade
                count += 1
                temgrades[id[1]] = {"avg" : avg, "count" : count}

        print(f"Average grade of {courses[key]['name']}: {avg/count:.2f}")
def best_worst_student():
    print("\n--- Best & Worst Students ---")

    if not students:
        print("No students found.")
        return

    student_avgs = []
    for sid, info in students.items():
        total = 0
        count = 0
        for (student_id, course_code), grade in grades.items():
            if student_id == sid and grade is not None:
                total += grade
                count += 1

        avg = total / count if count > 0 else 0
        student_avgs.append((sid, info["name"], avg, count))

    graded_students = [s for s in student_avgs if s[3] > 0]

    if not graded_students:
        print("No students with grades found.")
        return

    best = max(graded_students, key=lambda x: x[2])
    worst = min(graded_students, key=lambda x: x[2])

    print(f"Best Student: {best[1]} ({best[0]}) with average {best[2]:.2f}")
    print(f"Worst Student: {worst[1]} ({worst[0]}) with average {worst[2]:.2f}")


def calculate_student_averages():
    """Calculate averages and return list only (no print)."""
    result = []

    for sid, info in students.items():
        total = 0
        count = 0

        for (student_id, course_code), grade in grades.items():
            if student_id == sid and grade is not None:
                total += grade
                count += 1

        avg = total / count if count > 0 else 0
        result.append((sid, info["name"], avg))

    return result
def pass_fail_rate():
    list = calculate_student_averages()
    pass_count = 0
    fail_count = 0
    for i in list:
        if i[2] >= 10:
            pass_count += 1
        else :
            fail_count += 1
    pass_rate = (pass_count / len(list))*100
    fail_rate = (fail_count / len(list))*100
    print(f"Pass Rate: {pass_rate:.1f}%\t Fail Rate: {fail_rate:.1f}%")

def save_all_data():
    try:
        with open("students.txt", "w") as f:
            for sid, info in students.items():
                f.write(f"{sid};{info['name']};{info['year']}\n")

        with open("courses.txt", "w") as f:
            for code, info in courses.items():
                f.write(f"{code};{info['name']};{info['credits']}\n")

        with open("grades.txt", "w") as f:
            for (sid, code), grade in grades.items():
                grade_str = str(grade) if grade is not None else ""
                f.write(f"{sid};{code};{grade_str}\n")

        print(" All data saved successfully!")
    except Exception as e:
        print(f"Error saving data: {e}")
def load_all_data():
    global students, courses, grades
    try:
        if os.path.exists("students.txt"):
            with open("students.txt", "r") as f:
                lines = f.readlines()

                for line in lines:
                    part =line.strip().split(";")
                    students[part[0]] = {"name": part[1], "year": int(part[2])}

        if os.path.exists("courses.txt"):
            with open("courses.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    part = line.strip().split(";")
                    courses[part[0]] = {"name": part[1], "credits": int(part[2])}
        if os.path.exists("grades.txt"):
            with open("grades.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    part =line.strip().split(";")
                    key = (part[0], part[1])
                    grades[key] = part[2]
        print(" All data loaded successfully!")
    except FileNotFoundError:

        print(" No previous data found. Starting fresh.")
    except Exception as e:

        print(f"Error loading data: {e}")
def backup():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    try:
        if not os.path.exists("backups"):
            os.makedirs("backups")
        with open(f"backups/students_{timestamp}.txt", "w") as f:
            for sid, info in students.items():
                f.write(f"{sid};{info['name']};{info['year']}\n")
        with open(f"backups/courses_{timestamp}.txt", "w") as f:
            for code, info in courses.items():
                f.write(f"{code};{info['name']};{info['credits']}\n")

        with open(f"backups/grades_{timestamp}.txt", "w") as f:
            for (sid, code), grade in grades.items():
                grade_str = str(grade) if grade is not None else ""
                f.write(f"{sid};{code};{grade_str}\n")
        print(f" Backup created: backups/students_{timestamp}.txt")
        print(f"                  backups/courses_{timestamp}.txt")
        print(f"                  backups/grades_{timestamp}.txt")
    except Exception as e:
        print(f"Error creating backup: {e}")

def show_menu():
    print("\n" + "=" * 50)
    print("UNIVERSITY RECORD SYSTEM")
    print("=" * 50)
    print("1. Manage Students")
    print("2. Manage Courses")
    print("3. Manage Enrollments and Grades")
    print("4. Statistics & Reports")
    print("5. File Operations")
    print("6. Exit")
    choice = input("Choose: ").strip()
    return choice
def manage_students():
    while True:
        print("\n" + "-" * 30)
        print("STUDENTS MENU")
        print("-" * 30)
        print("1. Add student")
        print("2. View all students")
        print("3. Update student info")
        print("4. Delete student")
        print("5. Back to main menu")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_students()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")


def manage_courses():
    while True:
        print("\n" + "-" * 30)
        print("COURSES MENU")
        print("-" * 30)
        print("1. Add course")
        print("2. List all courses")
        print("3. Update course")
        print("4. Delete course")
        print("5. Back to main menu")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_course()
        elif choice == "2":
            list_courses()
        elif choice == "3":
            update_course()
        elif choice == "4":
            delete_course()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")


def manage_enrollments():
    while True:
        print("\n" + "-" * 30)
        print("ENROLLMENTS & GRADES MENU")
        print("-" * 30)
        print("1. Enroll student in course")
        print("2. Enter/update grade")
        print("3. View student grades")
        print("4. Delete enrollment")
        print("5. Back to main menu")
        choice = input("Choose: ").strip()

        if choice == "1":
            enroll_student()
        elif choice == "2":
            enter_grade()
        elif choice == "3":
            view_student_grades()
        elif choice == "4":
            delete_enrollment()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")


def statistics_menu():
    while True:
        print("\n" + "-" * 30)
        print("STATISTICS & REPORTS")
        print("-" * 30)
        print("1. Student average")
        print("2. Course average")
        print("3. Best and worst student")
        print("4. Pass/fail rate per course")
        print("5. Back to main menu")
        choice = input("Choose: ").strip()

        if choice == "1":
            student_average_report()
        elif choice == "2":
            course_average_report()
        elif choice == "3":
            best_worst_student()
        elif choice == "4":
            pass_fail_rate()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")


def file_operations_menu():
    while True:
        print("\n" + "-" * 30)
        print("FILE OPERATIONS")
        print("-" * 30)
        print("1. Save all data")
        print("2. Load all data")
        print("3. Create backup")
        print("4. Back to main menu")
        choice = input("Choose: ").strip()

        if choice == "1":
            save_all_data()
        elif choice == "2":
            load_all_data()
        elif choice == "3":
            backup_data()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def main():
    print("=" * 50)
    print("WELCOME TO UNIVERSITY RECORDS SYSTEM")
    print("=" * 50)
    print("Loading existing data...")
    load_all_data()

    while True:
        choice = show_menu()

        if choice == "1":
            manage_students()
        elif choice == "2":
            manage_courses()
        elif choice == "3":
            manage_enrollments()
        elif choice == "4":
            statistics_menu()
        elif choice == "5":
            file_operations_menu()
        elif choice == "6":
            save_all_data()
            print("\nThank you for using University Records System!")
            print("All data saved. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()







