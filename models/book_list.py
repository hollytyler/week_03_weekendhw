from models.book import *

book1 = Book("Harry Potter and the Chamber of Secrets", "J.K. Rowling", "Fantasy", True)
book2 = Book("The Hobbit", "J.R.R. Tolken", "Fantasy", False)
book3 = Book("Storyteller", "Dave Grohl", "Autobiography", False)

books = [book1, book2, book3]

def add_new_book(book):
    books.append(book)

def delete_book(book_title):
    book_to_delete = None
    for book in books:
        if book.title == book_title:
            book_to_delete = book
            break

    books.remove(book_to_delete)
