class TestBook:
    def test_new_book(self, book):
        assert book.name
        assert book.inn
        assert book.author
