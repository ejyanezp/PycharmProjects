from bookStore.utils.database import Book, BookStore

menu = """
a.- Add book                   b.- List books
c.- Mark book as read          d.- Delete book
e.- Save books to csv file     f.- Load books from csv file
g.- Save books to json file    h.- Load books from json file
q.- Quit 
Your choice: """

book_store = BookStore()


def add_book():
    name = input("Name: ")
    author = input("Author: ")
    book = Book(name, author)
    book_store.add_book(book)


def list_books():
    print(str(book_store))


def select_book():
    list_books()
    while True:
        index = input("Select the book by number: ")
        try:
            index = int(index)
            return index
        except ValueError:
            print(f"Not a valid input '{index}', please enter an integer")


def mark_read():
    index = select_book()
    try:
        book = book_store[index-1]
        book.mark_read()
    except IndexError:
        print(f"Book not found {index}")


def delete_book():
    index = select_book()
    try:
        book = book_store[index-1]
        book_store.delete_book(book)
    except IndexError:
        print(f"Book not found {index}")


def save_books():
    file_name = input("Specify file name: ")
    book_store.save(file_name)


def load_books():
    file_name = input("Specify file name: ")
    book_store.load(file_name)


def save_to_json():
    file_name = input("Specify file name: ")
    book_store.save_to_json(file_name)


def load_from_json():
    file_name = input("Specify file name: ")
    book_store.load_from_json(file_name)


dispatcher = {'a': add_book,     'b': list_books, 'c': mark_read,
              'd': delete_book,  'e': save_books, 'f': load_books,
              'g': save_to_json, 'h': load_from_json}

while True:
    option = input(menu)
    if option == "q":
        break
    else:
        try:
            dispatcher[option]()
        except KeyError:
            print(f"{option} is not a valid option!")

print("Finished")
