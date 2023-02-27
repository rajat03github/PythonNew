# Exercise - 6 Library Mangament System
class Library:

    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBooks(self, book):
        self.books.append(book)  #append is push
        self.noBooks = len(self.books)

    def shoInfo(self):
        print(f"The library has {self.noBooks} books . The books are ")
        for book in self.books:
            print(book)


l1 = Library()
l1.addBooks("Harry Potter")
l1.addBooks("Harry Potter 2")
l1.shoInfo()