from abc import ABC, abstractmethod


class LibraryItem(ABC):

    def __init__(self, title):
        self.title = title
        self.available = True

    @abstractmethod
    def issue(self):
        pass

    @abstractmethod
    def return_item(self):
        pass


class Book(LibraryItem):

    def issue(self):
        if self.available:
            self.available = False
            print("Book issued:", self.title)
        else:
            print("Book is already issued.")

    def return_item(self):
        self.available = True
        print("Book returned:", self.title)


class Magazine(LibraryItem):

    def issue(self):
        if self.available:
            self.available = False
            print("Magazine issued:", self.title)
        else:
            print("Magazine is already issued.")

    def return_item(self):
        self.available = True
        print("Magazine returned:", self.title)


class User:
    def __init__(self, name):
        self.name = name

    def borrow_item(self, item):
        print(self.name, "is borrowing:")
        item.issue()

    def return_item(self, item):
        print(self.name, "is returning:")
        item.return_item()


book = Book("Python Programming")
magazine = Magazine("Technology Today")

user = User("Rahul")

user.borrow_item(book)
user.borrow_item(magazine)

user.return_item(book)
user.return_item(magazine)
