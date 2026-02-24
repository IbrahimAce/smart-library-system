class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                return book
        raise ValueError(f"Book '{title}' not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                return book
        raise ValueError(f"Book '{title}' not borrowed.")

    def borrow_item(self, item):
        # Duck typing: Works if item has .title (no type check)
        if hasattr(item, 'title'):
            print(f"Borrowing item: {item.title}")
        else:
            raise ValueError("Item must have a 'title' attribute.")

    def __getitem__(self, index):
        return self.books[index]

    def __len__(self):
        return len(self.books)
