class TestLibrary:
    def test_new_library(self, library):
        assert library.total == 5
        assert library.name
        assert library.passive == 0
        assert library.active == 5
        assert not library.readers
