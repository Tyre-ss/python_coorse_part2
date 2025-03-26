class Test_readers:
    def test_readers(self, readers):
        assert readers.number == 0
        assert readers.client == readers

    def test_unreturned_book(self, readers, library, total):
        readers.unreturned_book(2)
        assert readers.number_of_books == 2
        assert library.number_of_books == 1
        assert total.number_of_books == 3

    def test_returned_books(self, readers, library, total):
        readers.returned_books(1)
        assert readers.number_of_books == 1
        assert library.number_of_books == 2
        assert total.number_of_books == 2

    def test_cost_of_book(self, book):
        book.cost(20)

    def test_rental_duration(self, months):
        months.number(2)

    def test_delay_duration(self, months):
        months.number(0.5)

    def test_transfer_of_book(self, book, readers, library, total):
        library.issued_books(1)
        readers.returned_books(0)
        assert library.numbers_of_book == 19
        assert readers.number_of_books == 6
        assert total.number_of_books == 25
