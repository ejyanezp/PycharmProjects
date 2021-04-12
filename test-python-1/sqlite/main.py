import sqlite.books_database


menu = """
a.- Add book                   b.- List books
c.- Mark book as read          d.- Delete book
q.- Quit 
Your choice: """


def add_book():
    name = input("Name: ")
    author = input("Author: ")
    sqlite.books_database.db_add_book(name, author)


def list_books():
    result_set = sqlite.books_database.db_list_books()
    for book in result_set:
        print(f"\t{book['name']} by {book['author']}, Read: {book['read']}")


# Type hint "-> str" (only useful in the IDE, the language does not use it)
# Tells this function returns a string object
def select_book() -> str:
    list_books()
    name = input("Enter the book name: ")
    return name


def mark_read():
    name = select_book()
    sqlite.books_database.db_mark_read(name)


def delete_book():
    name = select_book()
    sqlite.books_database.db_delete_book(name)


dispatcher = {'a': add_book, 'b': list_books, 'c': mark_read, 'd': delete_book}

while True:
    option = input(menu)
    if option == "q":
        break
    try:
        dispatcher[option]()
    except KeyError:
        print(f"{option} is not a valid option!")

print("Finished")
