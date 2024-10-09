# library.py
import json
from book import Book
import os

class Library:
    def __init__(self, data_file="data/library_data.json"):
        self.data_file = data_file
        self.books = []
        self.borrowed_books = {}
        self.load_data()

    def create_empty_data_file(self):
        if not os.path.exists(self.data_file):
            initial_data = {
                "library": {
                    "books": [],
                    "borrowed_books": {}
                }
            }
            with open(self.data_file, 'w') as file:
                json.dump(initial_data, file)

    def load_data(self):
        self.create_empty_data_file()  # Ensure the file exists
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                self.books = [Book.from_dict(book) for book in data['library']['books']]
                self.borrowed_books = {user: Book.from_dict(book) for user, book in data['library']['borrowed_books'].items()}
        except FileNotFoundError:
            self.books = []
            self.borrowed_books = {}

    def save_data(self):
        data = {
            "library": {
                "books": [book.to_dict() for book in self.books],
                "borrowed_books": {user: book.to_dict() for user, book in self.borrowed_books.items()}
            }
        }
        with open(self.data_file, 'w') as file:
            json.dump(data, file)

    def add_book(self, book):
        self.books.append(book)
        self.save_data()

    def borrow_book(self, user, title):
        for book in self.books:
            if book.title == title and title not in self.borrowed_books:
                self.borrowed_books[user] = book
                self.books.remove(book)
                self.save_data()
                return
        print(f"Sorry, {title} is unavailable.")

    def return_book(self, user):
        if user in self.borrowed_books:
            returned_book = self.borrowed_books.pop(user)
            self.books.append(returned_book)
            self.save_data()
