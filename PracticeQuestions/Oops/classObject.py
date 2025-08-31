'''
question✅ 1. Class & Object
Create a Book class with title, author, and price. Add a method to display book details.
Add a class variable to count how many Book objects have been created.
Create a Library class which stores a list of Book objects and has methods to:
Add a book.
Remove a book by title.
Display all books.
'''
'''
class Book :
    count_book = 0
    def Details(self,Title,auther,price):
        self.Title = Title
        self.auther = auther
        self.price = price

        Book.count_book +=1
        
        print(f"Details of Book{self.count_book}::\nBook title:{self.Title}\nauther Name of this book:{self.auther}\nand price Only :{self.price}\n")

    # def bookDetails(self):
    #     print(f"Details of Books::\nBook title:{self.Title}\nauther Name of this book:{self.auther}\nand price Only :{self.price}\n Total books is : {self.count_book}")
    @staticmethod
    def display_count_book():
        print(f"Numbers of books are:{Book.count_book}")

    
book = Book()
book.Details("Python","Guido van rossum", 499)
book.Details("Java","Jams gosline", 455)
book.Details("C","danis ritchi", 299)
book.Details("C++","Bjarne Stroustrup", 399)
book.display_count_book()

'''
'''
class  Library:
    count_book =0 
    def Enter_Book(self,Title,author,price):
        self.Title = Title
        self.author = author
        self.price = price 
         
        Library.count_book += 1


    def Display_Book(self):
        print(f"Details of Book{self.count_book}::\nBook title:{self.Title}\nauther Name of this book:{self.authr}\nand price Only :{self.price}\n")

obj = Library()
for i in range(1,5):
    value_store = obj.Enter_Book(input(f"Enter Book{Library.count_book+1} name:"),input("Enter Book  auther name:"),int(input("Enter price of this Book:")))
    print(value_store)
obj.Display_Book()
print(obj.count_book)
'''
# testing to add new concept

# class Library:
#     count_book = 0

#     def __init__(self, Title, author, price):
#         self.Title = Title
#         self.author = author
#         self.price = price
#         Library.count_book += 1

#     def Display_Book(self,count):
#         self.count = count
#         print(f"\nDetails of Book {count}:")
#         print(f"Book Title: {self.Title}")
#         print(f"Author Name: {self.author}")
#         print(f"Price: ₹{self.price}")

# # Create a list to store all book objects
# books = []

# for i in range(2):
#     title = input(f"Enter Book {i+1} name: ")
#     author = input("Enter Book author name: ")
#     price = int(input("Enter price of this Book: "))
#     book = Library(title, author, price)
#     books.append(book)

# # Display all books
# i = 1
# for book in books:
#     with open("classObjectData.txt") as f:
#         store_value = f.read()
#     with open("classObjectData.txt","w") as f:
#         store_value = book.Display_Book(i)
#         f.write(store_value)
#     i +=1
# print(store_value)
# print(f"\nTotal number of books entered: {Library.count_book}")


'''
class Library:
    count_book = 0

    def __init__(self, Title, author, price):
        self.Title = Title
        self.author = author
        self.price = price
        Library.count_book += 1

    def Display_Book(self, count):
        data = f"\nDetails of Book {count}:\n"
        data += f"Book Title: {self.Title}\n"
        data += f"Author Name: {self.author}\n"
        data += f"Price: ₹{self.price}\n"
        return data

# Create a list to store all book objects
books = []

for i in range(2):
    title = input(f"Enter Book {i+1} name: ")
    author = input("Enter Book author name: ")
    price = int(input("Enter price of this Book: "))
    book = Library(title, author, price)
    books.append(book)

# Gather all output in a string
output_data = ""
for i, book in enumerate(books, start=1):
    output_data += book.Display_Book(i)

# Write to file using utf-8 encoding
with open("classObjectData.txt", "w", encoding="utf-8") as f:
    f.write(output_data)

# Print to console
print(output_data)
print(f"\nTotal number of books entered: {Library.count_book}")

'''