# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 14:20:25 2024

@author: Göktuğ
"""

class Book:
    def __init__(self, name, author, release_date, page):
        self.name = name
        self.author = author
        self.release_date = release_date
        self.page = page

    def to_string(self):
        return f"{self.name},{self.author},{self.release_date},{self.page}"

    @staticmethod
    def from_string(book_string):
        name, author, release_date, page = book_string.strip().split(',')
        return Book(name, author, int(release_date), int(page))

class Library:
    def __init__(self):
        self.booklist = []
        
    def add_book(self, book):
        self.booklist.append(book)
     
    def list_books(self):
        if not self.booklist:
            print("No books found in the library.")
            return
        for index, book in enumerate(self.booklist, 1):
            print(f"Book {index}:")
            print("Name:", book.name)
            print("Author:", book.author)
            print("Release Date:", book.release_date)
            print("Page:", book.page)
            print("------------------------")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for book in self.booklist:
                file.write(book.to_string() + '\n')

    def load_from_file(self, filename):
        self.booklist = []
        with open(filename, 'r') as file:  # Open in read mode
            lines = file.read().splitlines()  # Read lines and split them
        for line in lines:
            self.booklist.append(Book.from_string(line))

    def remove_book(self, book_name):
        for book in self.booklist:
            if book.name.lower() == book_name.lower():
                self.booklist.remove(book)
                print(f"The book '{book_name}' has been removed from the library.")
                return
        print(f"The book '{book_name}' is not found in the library.")

    def find_book_by_name(self, book_name):
        for book in self.booklist:
            if book.name.lower() == book_name.lower():
                return book
        return None

# Function to get user input for a new book
def get_book_details_from_user():
    name = input("Enter the name of the book: ")
    author = input("Enter the author of the book: ")
    release_date = int(input("Enter the release date of the book: "))
    page = int(input("Enter the page count of the book: "))
    return Book(name, author, release_date, page)

# Create an instance of the Library class
library = Library()

# Load the library from the text file
library.load_from_file("library.txt")

# Menu loop
while True:
    print("\nMenu:")
    print("1. List Books")
    print("2. Add New Book")
    print("3. Remove a Book")
    print("4. Search for a Book")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        print("\nListing Books:")
        library.list_books()
    elif choice == '2':
        print("\nAdding New Book:")
        new_book = get_book_details_from_user()
        library.add_book(new_book)
        print("Book added successfully.")
    elif choice == '3':
        print("\nRemoving a Book:")
        book_to_remove = input("Enter the name of the book you want to remove: ")
        library.remove_book(book_to_remove)
    elif choice == '4':
        print("\nSearch for a Book:")
        book_name = input("Enter the name of the book you are searching for: ")
        found_book = library.find_book_by_name(book_name)
        if found_book:
            print("Book found:")
            print("Name:", found_book.name)
            print("Author:", found_book.author)
            print("Release Date:", found_book.release_date)
            print("Page:", found_book.page)
        else:
            print(f"The book '{book_name}' is not found in the library. Would you like to donate it for us ?")
            Donate=input()
            if Donate.lower() == "yes":
               print("\nAdding New Book:")
               new_book = get_book_details_from_user()
               library.add_book(new_book)
               print("Book added successfully.")
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

# Save the library to a text file before quitting
library.save_to_file("library.txt")