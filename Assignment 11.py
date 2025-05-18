# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 11. Class Methods

# Assignment 11:

# Create a class Book with a class variable total_books.
# Add a class method increment_book_count() to increase the count when a new book is added.

# SOLUTION :

class Book:
    # 📚 Class variable to keep track of total number of books
    total_books = 0

    def __init__(self, title, author):
        self.title = title      # 📖 Title of the book
        self.author = author    # ✍️ Author of the book
        Book.increment_book_count()  # 🔢 Increment book count
        print(f"\n 🎉 New Book Added: '{self.title}' by {self.author}")

    @classmethod
    def increment_book_count(cls):
        """🧮 Increases the total number of books by 1"""
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        """📊 Returns the current total number of books"""
        return cls.total_books

# 🚀 Example usage
print("\n 📚 Welcome to the Library System!")

# 📘 Adding books
book1 = Book("Jannat Kay Pattay ", "Nimra Ahmed")
book2 = Book("Peer-e-Kamil (ﷺ) ", "Umera Ahmed")
book3 = Book("Aangan ", "Khadija Mastoor")

# 📈 Displaying total number of books
print("\n 🧾 Total books in the system:", Book.get_total_books())

# --------------- ASSIGNMENT 11 ENDS HERE ---------------

