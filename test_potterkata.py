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
    
def test_fiveDiffBook(potterKata):
    books = [1,1,1,1,1]
    assert potterKata.getPrice(books) == 30
    
#test duplicated books' price
def twoBooksDuplicated(potterKata):
    books = [2,2,0,0,0]
    assert potterKata.getPrice(books) == 30.4
    
def threeBooksDuplicated(potterKata):
    books = [2,2,2,0,0]
    assert potterKata.getPrice(books) == 43.2
    
def fourBooksDuplicated(potterKata):
    books = [2,2,2,2,0]
    assert potterKata.getPrice(books) == 51.2
    
def fiveBooksDuplicated(potterKata):
    books = [2,2,2,2,2]
    assert potterKata.getPrice(books) == 60
    
def threeBooksWithOneDuplicated(potterKata):#5% discount
    books = [2,1,0,0,0]
    assert potterKata.getPrice(books) == 38.4
    
def threeBooksDuplicated(potterKafa):#10% discount
    books = [2,2,2,0,0]
    assert potterKafa.getPrice(books) == 43.2
    
def fiveBooksTwoDuplicated(potterKafa):#10% for three books, 5% for two books
    books = [2,2,1,0,0]
    assert potterKafa.getPrice(books) == 36.8
    
def sixBooksTwoDuplicated(potterKafa):#20% for four books, 5% for two books
    books = [2,2,1,1,0]
    assert potterKafa.getPrice(books) == 40.8
    
def allDiscountApplied(potterKafa):#
    books = [3,2,4,2,1]
    assert potterKafa.getPrice(books) == (30+25.6+15.2+8)