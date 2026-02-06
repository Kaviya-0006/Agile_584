books = []

def welcome():
    print("Welcome to the Library Management System")

def add_book(book_name):
    books.append(book_name)
    print(f"Book '{book_name}' added successfully")

def view_books():
    if not books:
        print("No books available in the library")
    else:
        print("Books available in the library:")
        for book in books:
            print("-", book)

welcome()
add_book("Python Programming")
add_book("Data Structures")
view_books()
