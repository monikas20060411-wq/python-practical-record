class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def borrow(self, book):
        if book.issue():
            print(self.name, "issued", book.title)
        else:
            print("Book is already issued.")

    def return_book(self, book):
        book.return_book()
        print(self.name, "returned", book.title)


class Student(User):
    pass


class Teacher(User):
    pass


books = [
    Book(1, "Python Programming", "Guido"),
    Book(2, "Java Programming", "James"),
    Book(3, "C Programming", "Dennis")
]

users = [
    Student(101, "Rahul"),
    Teacher(102, "Anita")
]


def display_books():
    print("\n--- Books ---")

    for book in books:
        status = "Available" if book.available else "Issued"

        print(
            book.book_id,
            book.title,
            "-",
            book.author,
            "-",
            status
        )


def find_book(book_id):
    for book in books:
        if book.book_id == book_id:
            return book

    return None


while True:

    print("\n===== LIBRARY MANAGEMENT =====")
    print("1. Display Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_books()

    elif choice == "2":
        user_id = int(input("Enter user ID: "))
        book_id = int(input("Enter book ID: "))

        user = next(
            (u for u in users if u.user_id == user_id),
            None
        )

        book = find_book(book_id)

        if user and book:
            user.borrow(book)
        else:
            print("Invalid user or book.")

    elif choice == "3":
        user_id = int(input("Enter user ID: "))
        book_id = int(input("Enter book ID: "))

        user = next(
            (u for u in users if u.user_id == user_id),
            None
        )

        book = find_book(book_id)

        if user and book:
            user.return_book(book)
        else:
            print("Invalid user or book.")

    elif choice == "4":
        print("Exiting Library System...")
        break

    else:
        print("Invalid choice.")
