from library_system import Book, Library

def demo():
    library = Library()
    
    # Add books (requires Admin role)
    try:
        library.add_book(Book("Python Basics", "Author1", 200), user_role="User")  # Should fail
    except PermissionError as e:
        print(f"Permission error: {e}")
    
    library.add_book(Book("Python Basics", "Author1", 200), user_role="Admin")
    library.add_book(Book("Advanced Python", "Author2", 300), user_role="Admin")
    
    # Iterate over library
    for book in library:
        print(book)
    
    # Borrow and return with logging
    library.borrow_book("Python Basics")
    library.return_book("Python Basics")
    
    # Duck typing
    class FakeItem:
        title = "Fake Title"
    library.borrow_item(FakeItem())  # Works due to duck typing
    
    # Len and eq examples
    book1 = Book("Python Basics", "Author1", 200)
    book2 = Book("Python Basics", "Author1", 200)
    print(len(book1))  # 200
    print(book1 == book2)  # True

if __name__ == "__main__":
    demo()
