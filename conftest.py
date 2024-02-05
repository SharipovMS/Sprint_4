import pytest
from main import BooksCollector

@pytest.fixture()
def setup():
    collector = BooksCollector()
    return collector
