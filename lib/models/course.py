from . import CONN, CURSOR

class Course:
    def __init__(self, id, name, instructor_id):
        self.id = id
        self.name = name
        self.instructor_id = instructor_id

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            instructor_id INTEGER,
            FOREIGN KEY (instructor_id) REFERENCES instructors(id)
        )
        """)
        CONN.commit()

    @classmethod
    def create(cls, name, instructor_id):
        CURSOR.execute("INSERT INTO courses (name, instructor_id) VALUES (?, ?)", (name, instructor_id))
        CONN.commit()
        return cls(CURSOR.lastrowid, name, instructor_id)

    @classmethod
    def get_all(cls):
        rows = CURSOR.execute("SELECT * FROM courses").fetchall()
        return [cls(*row) for row in rows]

    def __repr__(self):
        return f"Course({self.id}, '{self.name}', Instructor ID: {self.instructor_id})"
