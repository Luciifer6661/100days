# class Library:
#     def __init__(self):
#         self.books=[]
#         self.no_books=0
        
#     def showinfo(self):
#         print(f"The library has {self.no_books} books and the books are:")
#         for b in self.books:
#             print(b)
            
#     def add_books(self,book):
#         self.books.append(book)
#         # print(self.books)
#         self.no_books=len(self.books)
    
    
        
# l=Library()
# l.add_books("Do Epic Shit")
# l.add_books("Alchemist")
# l.add_books("Gita")

# l.showinfo()


#using getters and setters------------------------------------------------------------------------

class Library:
    def __init__(self):
        self.books=[]
        self.no_books=0
        
        
    @property
    def add_books(self):
        print(f"The library has {self.no_books} books and the books are:")
        for b in self.books:
            print(b)
    
    @add_books.setter
    def add_books(self,book):
        self.books.append(book)
        # print(self.books)
        self.no_books=len(self.books)
    
    
        

p=Library()
p.add_books="Make Epic Money"
p.add_books="Alchemist"
p.add_books="Gita"
p.add_books


