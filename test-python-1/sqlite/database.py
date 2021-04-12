import sqlite3
import os.path


class Database:
    def __init__(self, db_name):
        self.conn = None
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not (exc_type or exc_val or exc_tb):
            self.conn.commit()
        self.conn.close()

    @classmethod
    def create_book_table(cls, name):
        create_table = True
        if os.path.isfile(name):
            create_table = False
        conn = sqlite3.connect(name)
        cursor = conn.cursor()
        if create_table:
            print("Creating App tables")
            cursor.execute('CREATE TABLE books (name text primary key, author text, read integer)')
        else:
            print("Using App Tables")
        conn.commit()
        conn.close()
