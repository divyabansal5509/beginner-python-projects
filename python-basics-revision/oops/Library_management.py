class Book:
    def __init__(self,title,author,id):
        self.title = title
        self.author = author
        self.id =id
        self.is_available = True
        
    def __str__(self):
        return f"{self.title} by {self.author} having id = {self.id}, {self.is_available}"
    
class DigitalBook(Book):
    def __init__(self, title, author, id, file_size):
        super().__init__(title, author, id)
        self.file_size = file_size
    
    def __str__(self):
        return f"{self.title} by {self.author} having id = {self.id}, ({self.file_size}) {self.is_available}"
    
class Library():
     def __init__(self):
         self.lis=[]
         
     def add_book(self,book):
         self.lis.append(book)
         
     def display_books(self):
         for i in self.lis:
            print(i)
             
         
     def search_book(self,name):
         for i in self.lis:
            if i.title == name:
                print(i)
                
     def borrow_book(self,id):
         found = False
         for i in self.lis:
             if i.id == id:
                 found = True
                 if i.is_available == True:
                     i.is_available == False
                     print(f"Success! You Borrowed {i.title}")
                 else:
                     print("Sorry,this book is already borrowed")
         if found == False:
            print("Book not found")
                     
                  
     def return_book(self,id):
         found = False
         for i in self.lis:
             if i.id == id:
                 found = True
                 if i.is_available == False:
                     i.is_available == True
                     print(f"Success! '{i.title}' has been returned to the shelf")
                 else:
                     print(f"Error,'{i.title}' is already in the library catalog.")
         if found == False:
            print("Book not found")
         
    
book1 = Book("AI","Sam Dash","090")
book2 = Book("CS","Ram Mash","080")
book3 = DigitalBook("ACC","INK Rash","060","247 KB")
book4 = DigitalBook("French","Robin Mosby","070","502 KB")

Lib = Library()
Lib.add_book(book1)
Lib.add_book(book2)
Lib.add_book(book3)
Lib.add_book(book4)

print("----Display Books ----") 
Lib.display_books()
print("----Search Books ----")
Lib.search_book("ACC")
    
print("----Display Books ----") 
Lib.display_books()

print("--- Borrow Book---")
Lib.borrow_book("090")

print("--- return Book---")
Lib.return_book("080")

print("----Display Books ----") 
Lib.display_books()