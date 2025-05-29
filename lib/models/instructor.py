from . import CONN, CURSOR

class Instructor:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS instructors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """)
        CONN.commit()

    @classmethod
    def create(cls, name):
        CURSOR.execute("INSERT INTO instructors (name) VALUES (?)", (name,))
        CONN.commit()
        return cls(CURSOR.lastrowid, name)

    @classmethod
    def get_all(cls):
        rows = CURSOR.execute("SELECT * FROM instructors").fetchall()
        return [cls(*row) for row in rows]

    def __repr__(self):
        return f"Instructor({self.id}, '{self.name}')"
