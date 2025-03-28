import uuid


class Book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.inn = uuid.uuid4().hex
        self.author = author

    def __str__(self):
        return f"<Book {self.name} - {self.inn}>"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.list_book: list[Book] = []

    def get_book(self, book_inn):
        for book in self.list_book:
            if book.inn == book_inn:
                self.list_book.append(book)

    def delete_book(self, book_inn):
        for book in self.list_book:
            if book.inn == book_inn:
                self.list_book.remove(book)
                break
