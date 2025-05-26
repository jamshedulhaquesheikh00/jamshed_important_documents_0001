class Book:
    total_books = 0  # Class variable to keep track of total number of books

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  # Increment count when a new book is created

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Example usage
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("Pride and Prejudice", "Jane Austen")

print(f"Total books: {Book.total_books}")
