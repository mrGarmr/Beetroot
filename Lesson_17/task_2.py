
# Task 2

# Library

# Write a class structure that implements a library. Classes:

# 1) Library - name, books = [], authors = []

# 2) Book - name, year, author (author must be an instance of Author class)

# 3) Author - name, country, birthday, books = []

# Library class

# Methods:

# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.

# - group_by_author(author: Author) - returns a list of all books grouped by the specified author

# - group_by_year(year: int) - returns a list of all the books grouped by the specified year

# All 3 classes must have a readable __repr__ and __str__ methods.

# Also, the book class should have a class variable which holds the amount of all existing books

# '''

# class Library:

#     pass

 

# class Book:

#     pass

 

# class Author:

#     pass

# '''


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author(name={self.name}, country={self.country}, birthday={self.birthday})"

    def __str__(self):
        return f"{self.name} ({self.country})"

class Book:
    book_count = 0  # Class variable to keep track of the total number of books

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

        # Adding the book to the author's list of books
        author.books.append(self)

        # Increment the global book count
        Book.book_count += 1

    def __repr__(self):
        return f"Book(name={self.name}, year={self.year}, author={self.author.name})"

    def __str__(self):
        return f"'{self.name}' by {self.author.name} ({self.year})"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __repr__(self):
        return f"Library(name={self.name}, books={len(self.books)}, authors={len(self.authors)})"

    def __str__(self):
        return f"{self.name} Library with {len(self.books)} books and {len(self.authors)} authors."

    def new_book(self, name, year, author):
        """Adds a new book to the library and to the author's book list."""
        book = Book(name, year, author)
        self.books.append(book)

        # Add author to the library's authors list if not already present
        if author not in self.authors:
            self.authors.append(author)
        
        return book

    def group_by_author(self, author):
        """Returns a list of all books grouped by the specified author."""
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        """Returns a list of all books grouped by the specified year."""
        return [book for book in self.books if book.year == year]

# Example Usage

if __name__ == "__main__":
    # Create some authors
    author1 = Author("George Orwell", "United Kingdom", "1903-06-25")
    author2 = Author("J.K. Rowling", "United Kingdom", "1965-07-31")

    # Create a library
    library = Library("City Library")

    # Add books to the library
    library.new_book("1984", 1949, author1)
    library.new_book("Animal Farm", 1945, author1)
    library.new_book("Harry Potter and the Philosopher's Stone", 1997, author2)
    library.new_book("Harry Potter and the Chamber of Secrets", 1998, author2)

    # Print the library
    print(library)

    # Print books grouped by author
    print("\nBooks by George Orwell:")
    for book in library.group_by_author(author1):
        print(book)

    # Print books grouped by year
    print("\nBooks published in 1997:")
    for book in library.group_by_year(1997):
        print(book)

    # Print total number of books in the system
    print(f"\nTotal number of books: {Book.book_count}")
