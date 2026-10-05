class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class User:
    def __init__(self, name):
        self.name = name

    def get_limit(self):
        return 1

    def issue_book(self, book):
        if book.available:
            book.available = False
            print(self.name, "issued", book.title)
        else:
            print(book.title, "is already issued.")

    def return_book(self, book):
        book.available = True
        print(self.name, "returned", book.title)


class Student(User):
    def get_limit(self):
        return 2


class Teacher(User):
    def get_limit(self):
        return 5


class Guest(User):
    def get_limit(self):
        return 1


books = [
    Book("Python"),
    Book("Java"),
    Book("C++")
]

users = [
    Student("Arun"),
    Teacher("Meena"),
    Guest("Kumar")
]

for user in users:
    print(user.name, "can borrow", user.get_limit(), "book(s)")
