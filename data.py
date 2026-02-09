from DataProvider import DataProvider

class TestData:
    def __init__(self):
        self._config = None
        self._users = None
        self._selectors = None
        self._config = None
        self._products = None
        self._messages = None
        self._sort = None

    @property
    def users(self):
        if self._users is None:
            self._users = DataProvider("users.json")
        return self._users

    @property
    def config(self):
        if self._config is None:
            self._config = DataProvider("config.json")
        return self._config

    @property
    def messages(self):
        if self._messages is None:
            self._messages = DataProvider("messages.json")
        return self._messages

    @property
    def products(self):
        if self._products is None:
            self._products = DataProvider("products.json")
        return self._products

    @property
    def selectors(self):
        if self._selectors is None:
            self._selectors = DataProvider("selectors.json")
        return self._selectors

    @property
    def sort(self):
        if self._sort is None:
            self._sort = DataProvider("sort.json")
        return self._sort