import unittest

#Library___________________________________________
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
    book_count = 0  

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

        author.books.append(self)

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

        if author not in self.authors:
            self.authors.append(author)
        
        return book

    def group_by_author(self, author):
        """Returns a list of all books grouped by the specified author."""
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        """Returns a list of all books grouped by the specified year."""
        return [book for book in self.books if book.year == year]
#___________________________________________________________________________

class TestLibraryUnitTest(unittest.TestCase):

    def setUp(self):
        """Set up the initial conditions for each test."""
        self.author1 = Author("T.G.Shevchenko", "Ukraine", "1814-03-09")
        self.author2 = Author("Lesia Ukrainka", "Ukraine", "1871-02-25")
        self.book1 = Book("Kobzar", 1840, self.author1)
        self.book2 = Book("Kateryna", 1842, self.author1)
        self.book3 = Book("Na krylah pisen", 1893, self.author2)
        self.library = Library("Kiev City Library")
        self.library.books.append(self.book1)
        self.library.books.append(self.book2)
        self.library.books.append(self.book3)


    def test_new_book_adding_to_library(self):
        """Test the new_book method of Library class."""
        book = self.library.new_book("Vidguky", 1902, self.author2)
        self.assertIn(book, self.library.books)
        self.assertIn(self.author2, self.library.authors)
        self.assertEqual(len(self.library.books), 4)  # Now there should be 4 books

    def test_library_group_by_author(self):
        """Test the group_by_author method of Library class."""
        self.library.new_book("Haidamaky", 1842, self.author1)
        books_by_author = self.library.group_by_author(self.author1)
        self.assertEqual(len(books_by_author), 3)  
        self.assertTrue(all(book.author == self.author1 for book in books_by_author))

    def test_library_group_by_year(self):
        """Test the group_by_year method of Library class."""
        self.library.new_book("Kasandra", 1901, self.author2)
        books_by_year = self.library.group_by_year(1901)
        self.assertEqual(len(books_by_year), 1)  # Only 1 book by year 1901
        print(books_by_year[0])
        self.assertEqual(books_by_year[0].year, 1901)

    def test_book_count_increment(self):
        """Test if the book count is correctly adding."""
        start_count = Book.book_count
        self.library.new_book("Bukvar", 1860, self.author1)
        self.assertEqual(Book.book_count, start_count + 1)

    def test_books_association_with_author(self):
        """Test if books are correctly associated with their authors."""
        self.assertIn(self.book1, self.author1.books)
        self.assertIn(self.book2, self.author1.books)
        self.assertNotIn(self.book3, self.author1.books)

    def test_author_books_after_adding_new_book(self):
        """Test if new books are added to the author's books list."""
        new_book = self.library.new_book("Boyarynia", 1913, self.author2)
        self.assertIn(new_book, self.author2.books)
        self.assertNotIn(new_book, self.author1.books)


if __name__ == "__main__":
    unittest.main()