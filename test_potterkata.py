import pytest
from potterKata import PotterKata


@pytest.fixture()
def potterKata():
    return PotterKata()

def test_NoBook(potterKata):
    books = [0,0,0,0,0]
    assert potterKata.getPrice(books) == 0
    
def test_oneBook(potterKata):
    books = [1,0,0,0,0]
    assert potterKata.getPrice(books) == 8