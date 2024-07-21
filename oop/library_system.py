# Base Class - Book
class Book:
    """A class to represent a book."""

    def __init__(self, title, author):
        """Initialize the Book instance."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the Book instance."""
        return f"Book: {self.title} by {self.author}"

# Derived Class - EBook
class EBook(Book):
    """A class to represent an e-book."""

    def __init__(self, title, author, file_size):
        """Initialize the EBook instance."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the EBook instance."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived Class - PrintBook
class PrintBook(Book):
    """A class to represent a print book."""

    def __init__(self, title, author, page_count):
        """Initialize the PrintBook instance."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the PrintBook instance."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Composition - Library
class Library:
    """A class to represent a library."""

    def __init__(self):
        """Initialize the Library instance."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)
