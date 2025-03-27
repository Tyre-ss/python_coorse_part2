import uuid


class Book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.inn = uuid.uuid4().hex
        self.author = author

    def __str__(self):
        return f"<Book {self.name} - {self.inn}>"

