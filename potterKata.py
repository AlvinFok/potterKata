#%%


class PotterKata:
    
    def __init__(self):
        self.discount = [1, 0.95, 0.9, 0.8, 0.75]#If only buy same books then no discount
    
    def getPrice(self, books:list):
        key = range(len(books))
        books = dict(zip(key, books))#cost list to dict
        
        price = 0
        numberOfRemainingBook = self.__getNumbersOfBooks(books)
        while numberOfRemainingBook > 0:
            numberOfDistinctBooks = self.__getNumberOfDistinctBooks(books)
            numberOfRemainingBook = self.__getNumbersOfBooks(books)
            
            discount = self.__getDiscount(numberOfDistinctBooks-1)
            price += numberOfDistinctBooks * 8 * discount
            
            self.__removeOneOfEachBooks(books, numberOfDistinctBooks)
                    
        
        return price

    def __removeOneOfEachBooks(self, books, numberOfDistinctBooks):
        for key in books:
            if numberOfDistinctBooks == 0:
                break
            if books[key] > 0:
                books[key] -= 1
                numberOfDistinctBooks -=1
    
    
    def __getDiscount(self, index):
        return self.discount[index]
    
    def __getNumbersOfBooks(self, books:dict):
        return sum(list(books.values()))
    
    def __getNumberOfDistinctBooks(self, books:dict):
        return sum(i > 0 for i in books.values())
    


potterKata = PotterKata()
books = [1,0,0,0,0]
print(potterKata.getPrice(books))
# %%
