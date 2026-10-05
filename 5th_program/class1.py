class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Available:", self.is_available)


class User:
    def __init__(self, name):
        self.name = name

    def issue_book(self, book):
        if book.is_available:
            book.is_available = False
            print(self.name, "issued", book.title)
        else:
            print(book.title, "is not available.")

    def return_book(self, book):
        if not book.is_available:
            book.is_available = True
            print(self.name, "returned", book.title)
        else:
            print(book.title, "was not issued.")


class Student(User):
    def issue_book(self, book):
        print("Student borrowing:")
        super().issue_book(book)


class Teacher(User):
    def issue_book(self, book):
        print("Teacher borrowing:")
        super().issue_book(book)


# Create books
book1 = Book("Python Programming", "John Smith")
book2 = Book("Data Structures", "Robert Brown")

# Create users
student = Student("Rahul")
teacher = Teacher("Priya")

# Issue book
student.issue_book(book1)

# Try to issue the same book
teacher.issue_book(book1)

# Return book
student.return_book(book1)

# Issue the book again
teacher.issue_book(book1)

# Display book details
print("\nBook Details:")
book1.display()