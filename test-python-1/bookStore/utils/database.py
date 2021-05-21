import csv
import json


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.read = False

    def __str__(self):
        return f"Title: {self.name}, Author: {self.author}, Status: {self.read}"

    def __repr__(self):
        return f"{self.name},{self.author},{self.read}"

    def mark_read(self):
        self.read = True


class BookStore:
    def __init__(self):
        self.bookList = []

    def __str__(self):
        result = "Book List:\n"
        index = 1
        for elem in self.bookList:
            result += f"\t{str(index)} - {str(elem)}\n"
            index += 1
        return result

    def __getitem__(self, item):
        return self.bookList[item]

    def add_book(self, new_elem):
        self.bookList.append(new_elem)

    def delete_book(self, book):
        self.bookList.remove(book)

    def save(self, file):
        csv_output = open(file, 'w', newline='\n')
        writer = csv.writer(csv_output)
        # writerows method in the line 47
        # requires a list of lists for writing CSV format
        list_seq = [[book.name, book.author, book.read] for book in self.bookList]
        writer.writerows(list_seq)
        csv_output.close()

    def load(self, file):
        try:
            csv_input = open(file, 'r')
            reader = csv.reader(csv_input)
            list_seq = list(reader)
            csv_input.close()
            # Convert the list of lists to our classes
            for my_list in list_seq:
                book = Book(my_list[0], my_list[1])
                book.read = True if my_list[2] == "True" else False
                self.add_book(book)
        except FileNotFoundError:
            print(f"'{file}' file was not found.")

    def save_to_json(self, file):
        json_output = open(file, 'w')
        list_dict = [{'name': book.name, 'author': book.author, 'read': book.read} for book in self.bookList]
        json.dump(list_dict, json_output)
        json_output.close()

    def load_from_json(self, file):
        try:
            input_file = open(file, 'r')
            list_dict = json.load(input_file)
            for obj in list_dict:
                book = Book(obj['name'], obj['author'])
                book.read = obj['read']
                self.add_book(book)
        except FileNotFoundError:
            print(f"'{file}' file was not found.")
        except json.decoder.JSONDecodeError as ex:
            print(ex)
