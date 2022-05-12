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
    
def test_multiSameBook(potterKata):
    books = [3,0,0,0,0]
    assert potterKata.getPrice(books) == 24
    
def test_twoDiffBook(potterKata):
    books = [1,1,0,0,0]
    assert potterKata.getPrice(books) == 15.2
    
def test_threeDiffBook(potterKata):
    books = [1,1,1,0,0]
    assert potterKata.getPrice(books) == 21.6
    
def test_fourDiffBook(potterKata):
    books = [1,1,1,1,0]
    assert potterKata.getPrice(books) == 25.6