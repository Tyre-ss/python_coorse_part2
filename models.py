import uuid


class Book:
    def __init__(self, book: str):
        self.book = book
        self.inn = uuid.uuid4().hex

    def __str__(self):
        return f"<Book {self.book} - {self.inn}>"


Harry_Potter = Book("Harry Potter")


class Readers:
    def __init__(self, reader: Book):
        self.reader = reader
        self.number_of_books = 0

    def unturned_books(self, unturned):
        self.number = unturned

    def returned_books(self, returned):
        self.number = returned

    def cost_of_book(self, cost):
        self.cost = cost

    def rental_duration(self, months):
        self.months = months

    def delay_duration(self, months):
        self.duration = months

    def transfer_of_book(self, Other, Self, number):
        self.number -= number
        self.number += number


class Library:
    def __init__(self, name: str):
        self.name = name
        self.readers: list[Readers] = []

    def open_reader_account(self, reader: Readers):
        new_reader = Readers(reader)
        self.readers.append(new_reader)

    @property
    def book_in_library(self):
        pas = 0
        for readers in self.readers:
            if readers.number_of_books > 0:
                pas += readers.number_of_books
