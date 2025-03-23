class TestAuthor:
    def test_new_author(self, author):
        assert author.inn
        assert author.name

    def test_inn_in_author(self, author, another_author):
        assert author.inn != another_author.inn


class TestPerson2:
    def test_new_author(self, author):
        assert author.inn
        assert author.name

    def test_inn_in_author(self, author, another_author):
        assert author.inn != another_author.inn
