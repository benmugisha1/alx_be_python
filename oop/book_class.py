class Book:
    """A class to represent a book."""

    def __init__(self, title, author, year):
        """Initialize the Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Print a message when the Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a string representation of the Book instance."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an official string representation of the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
