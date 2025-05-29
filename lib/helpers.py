from .models import CONN, CURSOR

def create_student_course_table():
    CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS student_courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    )
    """)
    CONN.commit()

def enroll_student(student_id, course_id):
    CURSOR.execute("""
    INSERT INTO student_courses (student_id, course_id)
    VALUES (?, ?)
    """, (student_id, course_id))
    CONN.commit()

def get_courses_for_student(student_id):
    CURSOR.execute("""
    SELECT c.id, c.name, c.instructor_id
    FROM courses c
    JOIN student_courses sc ON c.id = sc.course_id
    WHERE sc.student_id = ?
    """, (student_id,))
    return CURSOR.fetchall()

def get_students_for_course(course_id):
    CURSOR.execute("""
    SELECT s.id, s.name
    FROM students s
    JOIN student_courses sc ON s.id = sc.student_id
    WHERE sc.course_id = ?
    """, (course_id,))
    return CURSOR.fetchall()
