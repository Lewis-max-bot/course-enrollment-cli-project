from models.instructor import Instructor
from models.course import Course
from models.student import Student
from helpers import create_student_course_table, enroll_student

def reset_db():
    print("Resetting database...")
    Instructor.create_table()
    Course.create_table()
    Student.create_table()
    create_student_course_table()
    print("Tables created.")

def seed_data():
    print("Seeding data...")

    # Create Instructors
    alice = Instructor.create("Alice")
    bob = Instructor.create("Bob")

    # Create Courses
    math = Course.create("Math 101", alice.id)
    science = Course.create("Science 101", bob.id)

    # Create Students
    john = Student.create("John Doe")
    jane = Student.create("Jane Smith")

    # Enroll students
    enroll_student(john.id, math.id)
    enroll_student(jane.id, math.id)
    enroll_student(jane.id, science.id)

    print("Seeding complete.")

if __name__ == "__main__":
    reset_db()
    seed_data()
