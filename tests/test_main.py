from main import get_answer


class TestMain:
    def setup_method(self, method):
        print("\n%s - %s" % (type(self).__name__, method.__name__))

    def test_get_answer(self):
        assert get_answer() == 5