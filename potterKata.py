#%%


class PotterKata:
    
    def __init__(self):
        self.discount = [1, 0.95, 0.9, 0.8, 0.75]#If only buy same books then no discount
    
    def getPrice(self, books:list):
        if self.__isNoBook(books):#check isn't have book if no then return 0
            return 0
        discountIndex = -1
        for i in books:
            if i != 0:
                discountIndex += 1
                
        discount = self.__getDiscount(discountIndex)
        
        price = sum(books) * 8 * discount
        return price
        
    def __isNoBook(self, books:list):
        if sum(books) == 0:
            return True
        
        return False
    
    def __getDiscount(self, index):
        return self.discount[index]
    

if __name__ == 'main':
    potterKata = PotterKata()
    books = [1,0,0,0,0]
    print(potterKata.getPrice(books))
# %%
