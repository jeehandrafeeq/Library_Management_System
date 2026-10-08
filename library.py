class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def issue_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    return "✅ Book Issued Successfully"
                else:
                    return "❌ Already Issued"
        return "Book Not Found"

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.is_available = True
                return "✅ Book Returned Successfully"
        return "Book Not Found"