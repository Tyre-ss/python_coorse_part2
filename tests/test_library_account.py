# Lib = Library


class TestLibAccount:
    def test_bank_account(self, lib_account, person):
        assert lib_account.quantity == 0
        assert lib_account.autor == person

    def test_deposit(self, lib_account, lib):
        lib_account.deposit(3000)
        assert lib_account.book_quantity == 3000
        assert lib_account.books_from_readers == 3000
        assert lib.pasive_book == 0

    def test_withdraw(self, lib_account2, lib):
        lib_account2.withdraw(2000)
        assert lib_account2.book_quantity == -2000
        assert lib.books_from_readers == 3000
        assert lib.pasive_book == -2000

    def test_transfer(self, lib_account, lib_account2):
        lib_account.transfer(lib_account2, 50)
        assert lib_account.quantity == 3000 - 50
        assert lib_account2.quantity == -2000 + 50
