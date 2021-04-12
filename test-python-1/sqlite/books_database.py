from database import Database
import sqlite3
from typing import List, Dict, Union


# Example of Python Context Managers to initialize and close connections
def db_add_book(name, author):
    try:
        with Database('data.db') as db:
            cursor = db.cursor()
            # Recommended form to avoid SQL Injection
            cursor.execute('INSERT INTO books VALUES (?, ?, 0)', (name, author))
    except sqlite3.IntegrityError as err:
        print(err)


# Type hint a "Book" is a dictionary.
# Key is a string and value is a string or integer
Book = Dict[str, Union[str, int]]


# Type hint "-> List[Dict[str, Union[str, int]]]"
# (only useful in the IDE, the language does not use it)
# Tells this function returns a list of Books
def db_list_books() -> List[Book]:
    with Database('data.db') as db:
        cursor = db.cursor()
        cursor.execute('SELECT name, author, read from books ORDER BY name')
        result_set = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    return result_set


# Type hint of the function parameter ": str"
# Python ignores it, but this helps the programmer in the IDE
def db_mark_read(name: str):
    with Database('data.db') as db:
        cursor = db.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))


def db_delete_book(name):
    with Database('data.db') as db:
        cursor = db.cursor()
        cursor.execute('DELETE FROM books WHERE name=?', (name,))


Database.create_book_table('data.db')
