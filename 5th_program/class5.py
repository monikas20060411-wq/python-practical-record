class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self._available = True

    def issue(self):
        if self._available:
            self._available = False
            return True
        return False

    def return_book(self):
        self._available = True

    def status(self):
        return "Available" if self._available else "Issued"


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrowing_limit(self):
        return 1

    def issue_book(self, book):
        if len(self.borrowed_books) >= self.borrowing_limit():
            print(self.name, "has reached the borrowing limit.")
            return

        if book.issue():
            self.borrowed_books.append(book)
            print(self.name, "issued", book.title)
        else:
            print(book.title, "is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(self.name, "returned", book.title)
        else:
            print("This book was not borrowed by", self.name)


class Student(User):

    def borrowing_limit(self):
        return 2


class Teacher(User):

    def borrowing_limit(self):
        return 5


class Librarian(User):

    def borrowing_limit(self):
        return 10


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def display_books(self):
        print("\n===== BOOKS =====")

        for book in self.books:
            print(
                book.book_id,
                "|",
                book.title,
                "|",
                book.author,
                "|",
                book.status()
            )


# Create library
library = Library()


# Add books
library.add_book(
    Book(1, "Python Programming", "John Smith")
)

library.add_book(
    Book(2, "Data Structures", "Robert Brown")
)

library.add_book(
    Book(3, "Database Systems", "James Wilson")
)


# Create users
student = Student(101, "Rahul")
teacher = Teacher(102, "Priya")
librarian = Librarian(103, "Kumar")


library.add_user(student)
library.add_user(teacher)
library.add_user(librarian)


# Issue books
student.issue_book(library.books[0])
teacher.issue_book(library.books[1])

# Try to issue an already issued book
librarian.issue_book(library.books[0])

# Display books
library.display_books()

# Return a book
student.return_book(library.books[0])

# Issue again
librarian.issue_book(library.books[0])

# Display final status
library.display_books()
