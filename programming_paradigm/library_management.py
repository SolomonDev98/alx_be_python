#!/usr/bin/env python3
"""
    Objective: Implementing a system that tracks books in a library, focusing on classes, object instantiation, and method invocation.
"""

class Book:
    def __init__(self, title, author, _is_checked_out=False):
        self.title = title
        self.author = author
        self.__is_checked_out = _is_checked_out

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False
    
    def is_available(self):
        return not self.__is_checked_out


class Library:
    def __init__(self):
        self._books = []
    

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"'{title}' was not checked out.")

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")