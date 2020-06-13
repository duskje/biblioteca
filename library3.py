from datetime import date
import json


class Library:
    def __init__(self, books : list = None):
        if books is None:
            books = []

        self.books = list(books)

    def add_book(self, title: str, author: str = '', year: str = ''):
        self.books.append(Book(title, author, year))

    def remove_book(self, title: str):
        """Delete on first match"""
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break

    def lend_book(self, title: str):
        """Lend on first match"""
        for book in self.books:
            if book.title == title:
                book.date_lent = str(date.today())
                break

    def return_book(self, title: str):
        for book in self.books:
            if book.title == title:
                book.date_lent = None

    def load(self):
        with open('library.json', 'r') as file:
            books = json.load(file)

        self.books = [Book(**book) for book in books]

    def save(self):
        save_data = []

        for book in self.books:
            save_data.append({'title': book.title, 'author': book.author, 'year': book.year, 'date_lent': book.date_lent})

        with open('library.json', 'w') as file:
            json.dump(save_data, file)


class Book:
    def __init__(self, title: str, author: str = '', year: str = '', date_lent: date = None):
        self.title = title
        self.author = author
        self.year = year
        self.date_lent = date_lent

    # Is this even a good idea? I think not
    def __str__(self):
        return '{} by {}, published in {}.'.format(self.title, self.author, self.year)

    @property
    def is_here(self):
        return self.date_lent is None

