from models.instructor import Instructor
from models.course import Course
from models.student import Student
from helpers import enroll_student, get_students_for_course, get_courses_for_student

def print_menu():
    print("\n=== Course Enrollment System ===")
    print("1. List all instructors")
    print("2. List all courses")
    print("3. List all students")
    print("4. Add instructor")
    print("5. Add course")
    print("6. Add student")
    print("7. Enroll student in course")
    print("8. View students in a course")
    print("9. View courses for a student")
    print("0. Exit")

def list_instructors():
    instructors = Instructor.get_all()
    print("\nInstructors:")
    for inst in instructors:
        print(f"  ID: {inst.id}, Name: {inst.name}")

def list_courses():
    courses = Course.get_all()
    print("\nCourses:")
    for c in courses:
        print(f"  ID: {c.id}, Name: {c.name}, Instructor ID: {c.instructor_id}")

def list_students():
    students = Student.get_all()
    print("\nStudents:")
    for s in students:
        print(f"  ID: {s.id}, Name: {s.name}")

def add_instructor():
    name = input("Enter instructor name: ").strip()
    if name:
        inst = Instructor.create(name)
        print(f"Instructor created: {inst}")
    else:
        print("Name cannot be empty.")

def add_course():
    name = input("Enter course name: ").strip()
    list_instructors()
    try:
        instructor_id = int(input("Enter instructor ID for this course: "))
        inst_ids = [i.id for i in Instructor.get_all()]
        if instructor_id not in inst_ids:
            print("Invalid instructor ID.")
            return
        course = Course.create(name, instructor_id)
        print(f"Course created: {course}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def add_student():
    name = input("Enter student name: ").strip()
    if name:
        student = Student.create(name)
        print(f"Student created: {student}")
    else:
        print("Name cannot be empty.")

def enroll():
    list_students()
    try:
        student_id = int(input("Enter student ID to enroll: "))
        stud_ids = [s.id for s in Student.get_all()]
        if student_id not in stud_ids:
            print("Invalid student ID.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    list_courses()
    try:
        course_id = int(input("Enter course ID to enroll in: "))
        course_ids = [c.id for c in Course.get_all()]
        if course_id not in course_ids:
            print("Invalid course ID.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    enroll_student(student_id, course_id)
    print("Enrollment successful.")

def view_students_in_course():
    list_courses()
    try:
        course_id = int(input("Enter course ID to view students: "))
        course_ids = [c.id for c in Course.get_all()]
        if course_id not in course_ids:
            print("Invalid course ID.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    students = get_students_for_course(course_id)
    print(f"\nStudents enrolled in course ID {course_id}:")
    if not students:
        print("  No students enrolled.")
    else:
        for s in students:
            print(f"  ID: {s[0]}, Name: {s[1]}")

def view_courses_for_student():
    list_students()
    try:
        student_id = int(input("Enter student ID to view courses: "))
        stud_ids = [s.id for s in Student.get_all()]
        if student_id not in stud_ids:
            print("Invalid student ID.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    courses = get_courses_for_student(student_id)
    print(f"\nCourses for student ID {student_id}:")
    if not courses:
        print("  No courses enrolled.")
    else:
        for c in courses:
            print(f"  ID: {c[0]}, Name: {c[1]}, Instructor ID: {c[2]}")

def main():
    while True:
        print_menu()
        choice = input("Select an option: ").strip()
        if choice == "1":
            list_instructors()
        elif choice == "2":
            list_courses()
        elif choice == "3":
            list_students()
        elif choice == "4":
            add_instructor()
        elif choice == "5":
            add_course()
        elif choice == "6":
            add_student()
        elif choice == "7":
            enroll()
        elif choice == "8":
            view_students_in_course()
        elif choice == "9":
            view_courses_for_student()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
