from . import CONN, CURSOR

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """)
        CONN.commit()

    @classmethod
    def create(cls, name):
        CURSOR.execute("INSERT INTO students (name) VALUES (?)", (name,))
        CONN.commit()
        return cls(CURSOR.lastrowid, name)

    @classmethod
    def get_all(cls):
        rows = CURSOR.execute("SELECT * FROM students").fetchall()
        return [cls(*row) for row in rows]

    def __repr__(self):
        return f"Student({self.id}, '{self.name}')"
