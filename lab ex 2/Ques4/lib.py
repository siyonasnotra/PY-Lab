class LibraryManager:
    def __init__(self):
        # Dictionary to store books, where ISBN is the key
        self.books = {}

    def add_book(self, title, author, publisher, volume, year, isbn):
        """Add a book to the library."""
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
        else:
            self.books[isbn] = {
                'title': title,
                'author': author,
                'publisher': publisher,
                'volume': volume,
                'year': year
            }
            print(f"Book with ISBN {isbn} added.")

    def remove_book(self, isbn):
        """Remove a book from the library by its ISBN."""
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN {isbn} removed.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def retrieve_book(self, isbn):
        """Retrieve and display the details of a book using its ISBN."""
        book = self.books.get(isbn)
        if book:
            return book
        else:
            print(f"Book with ISBN {isbn} not found.")
            return None

    def search_books(self, query):
        """Search for books by title or author."""
        results = []
        for book in self.books.values():
            if query.lower() in book['title'].lower() or query.lower() in book['author'].lower():
                results.append(book)
        return results

    def list_books(self):
        """List all books currently in the library."""
        return list(self.books.values())

    def update_book(self, isbn, title=None, author=None, publisher=None, volume=None, year=None):
        """Update the details of an existing book."""
        book = self.books.get(isbn)
        if book:
            if title:
                book['title'] = title
            if author:
                book['author'] = author
            if publisher:
                book['publisher'] = publisher
            if volume:
                book['volume'] = volume
            if year:
                book['year'] = year
            print(f"Book with ISBN {isbn} updated.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def check_availability(self, isbn):
        """Check if a book is available in the library by its ISBN."""
        return isbn in self.books

# Example usage
if __name__ == "__main__":
    manager = LibraryManager()
    
    # Adding sample books
    manager.add_book("Python Machine Learning", "John Doe", "Tech Press", "1st", 2023, "978-3-16-148410-0")
    manager.add_book("Introduction to Data Structures", "Jane Smith", "Learn More", "2nd", 2021, "978-1-23-456789-7")
    
    # Retrieving a book
    print(manager.retrieve_book("978-3-16-148410-0"))
    
    # Searching for books
    print(manager.search_books("Data Structures"))
    
    # Listing all books
    print(manager.list_books())
    
    # Updating a book
    manager.update_book("978-1-23-456789-7", year=2022)
    
    # Checking availability
    print(manager.check_availability("978-3-16-148410-0"))
    
    # Removing a book
    manager.remove_book("978-1-23-456789-7")
    
    # Listing all books after removal
    print(manager.list_books())
