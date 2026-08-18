class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author

class Member:

    def __init__(self, name):
        self.name=name

class Librarian:
    def __init__(self):
        self.Librarian=""

class Library:
    def __init__(self):
        self.books=[]
        self.borrowed=[]
        self.members=[]

    def add(self, book):
        self.books.append(book)
    
    def remove(self, book):
        self.books.remove(book)

    def search(self, title):
        found=False
        for b in self.books:
            if b.title == title:
                print("Book found")
                found=True
        if not found:
            print("Book not found")

    def borrow(self, title):
        found=False
        for b in self.books:
            if b.title == title:
                self.books.remove(b)
                self.borrowed.append(b)
                print("Borrowed")
                found=True
                break
        if not found:
            print("No book found")
    def revert(self, title):
        found=False
        for b in self.borrowed:
            if b.title == title:
                self.borrowed.remove(b)
                self.books.append(b)
                print("Reverted")
                found=True
                break
        if not found:
            print("No book found")

    def view(self):
        for b in self.books:
            print(b.title + " by "+ b.author)        

l=Library()

while True:
    choice=int(input("1. Member Login || 2. Librarian Login || 0. Exit"))

    if choice==1:
        mem=input("1. View available books || 2. Search: || 3. Borrow || 4. Revert: ")
        if mem=="1":
            l.view()
        if mem=="2":
            title=input("Enter title of the book to search: ")    
            l.search(title)
        if mem=="3":
            title=input("Enter the title of the book to borrow: ")
            l.borrow(title)
        if mem=="4":
            title=input("Enter the title of the book to revert: ")
            l.revert(title)
    if choice==2:
        lib=int(input("1. Add book, 2. Remove book: "))
        if lib==1:
            title=input("Enter the book title to add: ")
            author=input("Enter the author name to add: ")
            book=Book(title, author)
            l.add(book)
            print("Book Added")
        if lib==2:
            title=input("Enter the book title to remove: ")
            l.remove(book)
            print("Book Removed")
    if choice==0:
        print("Thank you")
        break