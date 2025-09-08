from datetime import date
class Book:
    def __init__(self, title: str, author: str, year: int, status: bool = True):
        if not title:
            raise ValueError("Title cannot be none")
        self.title = title.lower()
        self.author = author.lower()
        self.year = year 
        self._status = status  # True for available and False for borrowed 
    
    # Getters and setters for the status 
    def getStatus(self):
        return self._status 
    def setStatus(self, status):
        self._status = status 



class Library:
    # Initalizes the books stored at the library. Possible exception: init already has duplicate books
    def __init__(self, books):
        self.books = {}
        for book in books:
            self.books[book.title] = book
        
    # For adding future books to the library 
    def addBook(self, book) -> bool:
        if self.books.get(book.title, None) != None:
            return False 

        self.books[book.title] = book 
        return True
    
    # For removing books from the library incase of damage?
    def removeBook(self, book_title) -> bool:
        if self.books.get(book_title, None) == None:
            return False 

        del self.books[book_title]
        return True

    # for users to borrow a book
    def borrowBook(self, book_title) -> bool:
        book = self.books.get(book_title, None)
        if not book or book.getStatus() == False:
            return False 

        book.setStatus(False)
        return True 
    
    # For users to return a book after borrowing it
    def returnBook(self, book_title) -> bool:
        book = self.books.get(book_title, None)
        if not book or book.getStatus() == True:
            return False 
        
        book.setStatus(True)
        return True 

    def filterBook(self, title: str = None, author: str = None, year: int = None) -> list[Book]:
        # I dont want to implement regex and make it complicated for now
        result = []
        for _, book in self.books.items():
            if book.getStatus() == True:
                if title == None or title.lower().strip() in book.title:
                    if author == None or author.lower() in book.author:
                        if year == None or year == book.year:
                            result.append(book)
        
        return result 
                            

                    





