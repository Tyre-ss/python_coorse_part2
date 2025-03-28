import pytest

from models import Book, Library


@pytest.fixture()
def book() -> Book:
    Harry_Potter = Book("Harry_Potter", "chtoto")
    return Harry_Potter


@pytest.fixture()
def another_book() -> Book:
    Widpochinok = Book("Harry_Potter", "im ai")
    return Widpochinok


@pytest.fixture()
def library():
    Lib = Library("I_dont_know")
    return Lib


@pytest.fixture()
def library2():
    Lib = Library("I_know")
    return Lib
