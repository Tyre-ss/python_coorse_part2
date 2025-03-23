class TestLib:
    def test_new_lib(self, lib):
        assert lib.name
        assert lib.passive == 0
        assert lib.active == 0
        assert not lib.accounts
