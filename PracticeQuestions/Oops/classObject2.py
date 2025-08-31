# Create a Library class which stores a list of Book objects and has methods to:
# Add a book.
# Remove a book by title.
# Display all books.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Price: ₹{self.price}"

class Library:
    def __init__(self):
        self.books = [] # create blank list as a books name 

    def add_book(self, title, author, price):
        book = Book(title, author, price) # create Book object using book name 
        self.books.append(book) #add books details in this list
        print(f"\n✅ Book '{title}' added to the library.") # display confirmaation massege 



    def remove_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"\n❌ Book '{title}' removed from the library.")
                return
        print(f"\n⚠️ Book '{title}' not found in the library.")

    def display_all_books(self):
        if not self.books:
            print("\n📚 The library is empty.")
        else:
            print("\n📖 Books in the Library:")
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book}")


# # 🔄 Sample usage:

library = Library()

# # Adding books
library.add_book("Python Basics", "John Doe", 299)
library.add_book("Data Science", "Jane Smith", 450)

# # Display books
library.display_all_books()

# # Remove a book
library.remove_book_by_title("Data Science")

# # Display again
library.display_all_books()
