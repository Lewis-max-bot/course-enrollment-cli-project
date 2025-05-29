import sqlite3


CONN = sqlite3.connect("lib/database.db")
CURSOR = CONN.cursor()
