import pytest
from main import BooksCollector

@pytest.fixture(autouse=True)
def setup():
    collector = BooksCollector()
    return collector
