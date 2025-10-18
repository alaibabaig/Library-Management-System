from datetime import datetime, timedelta

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.borrowed_by = None
        self.due_date = None

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, title, author):
        book_id = len(self.books) + 1
        self.books.append(Book(book_id, title, author))
        print("Book added successfully.")

    def register_member(self, name):
        member_id = len(self.members) + 1
        self.members.append(Member(member_id, name))
        print("Member registered successfully.")

    def display_all_books(self):
        if not self.books:
            print("No books in library.")
            return
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{book.book_id}. {book.title} by {book.author} [{status}]")

    def display_available_books(self):
        available = [book for book in self.books if not book.is_borrowed]
        if not available:
            print("No available books.")
        for book in available:
            print(f"{book.book_id}. {book.title} by {book.author}")

    def display_all_members(self):
        if not self.members:
            print("No members registered.")
            return
        for member in self.members:
            print(f"{member.member_id}. {member.name}")

    def search_books(self, keyword):
        found = False
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                status = "Borrowed" if book.is_borrowed else "Available"
                print(f"{book.book_id}. {book.title} by {book.author} [{status}]")
                found = True
        if not found:
            print("No matching books found.")

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if member and book and not book.is_borrowed:
            book.is_borrowed = True
            book.borrowed_by = member
            book.due_date = datetime.now() + timedelta(days=14)
            member.borrowed_books.append(book)
            print(f"Book '{book.title}' borrowed by {member.name}. Due date is {book.due_date.date()}")
        else:
            print("Borrow operation failed! Book might already be borrowed or invalid member/book.")

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if member and book and book in member.borrowed_books:
            book.is_borrowed = False
            book.borrowed_by = None
            book.due_date = None
            member.borrowed_books.remove(book)
            print(f"Book '{book.title}' returned successfully.")
        else:
            print("Return operation failed.")

    def view_members_borrowed_books(self, member_id):
        member = self.find_member(member_id)
        if member:
            if member.borrowed_books:
                for book in member.borrowed_books:
                    print(f"{book.book_id}. {book.title} by {book.author} (Due: {book.due_date.date()})")
            else:
                print("No books borrowed.")
        else:
            print("Member not found.")

    def view_overdue_books(self):
        now = datetime.now()
        found = False
        for book in self.books:
            if book.is_borrowed and book.due_date and book.due_date < now:
                print(f"{book.book_id}. {book.title} by {book.author} (Borrowed by: {book.borrowed_by.name}, Due: {book.due_date.date()})")
                found = True
        if not found:
            print("No overdue books.")

    def library_report(self):
        total = len(self.books)
        borrowed = len([b for b in self.books if b.is_borrowed])
        available = total - borrowed
        print(f"Total books: {total}")
        print(f"Borrowed books: {borrowed}")
        print(f"Available books: {available}")
        print(f"Total members: {len(self.members)}")

    def find_book(self, book_id):
        return next((b for b in self.books if b.book_id == book_id), None)

    def find_member(self, member_id):
        return next((m for m in self.members if m.member_id == member_id), None

)

def menu():
    library = Library()
    # Sample data for testing
    library.add_book("Python Programming", "John Doe")
    library.add_book("Let Us C", "Yashavant Kanetkar")
    library.add_book("Clean Code", "Robert C. Martin")
    library.add_book("The Pragmatic Programmer", "Andrew Hunt")
    library.add_book("Introduction to Algorithms", "Thomas H. Cormen")
    library.add_book("Design Patterns", "Erich Gamma")
    library.register_member("Alaiba")
    library.register_member("Sara")
    library.register_member("Ahmed")
    library.register_member("Mona")
    library.register_member("Omar")

    while True:
        print("=" * 70)
        print("LIBRARY MANAGEMENT SYSTEM")
        print("=" * 70)
        print("1. Display All Books")
        print("2. Display Available Books")
        print("3. Display All Members")
        print("4. Search Books")
        print("5. Borrow a Book")
        print("6. Return a Book")
        print("7. View Member's Borrowed Books")
        print("8. View Overdue Books")
        print("9. Library Report")
        print("10. Add New Book")
        print("11. Register New Member")
        print("0. Exit")
        print("=" * 70)
        choice = input("Enter your choice (0-11): ")
        print()

        if choice == '1':
            library.display_all_books()
        elif choice == '2':
            library.display_available_books()
        elif choice == '3':
            library.display_all_members()
        elif choice == '4':
            keyword = input("Enter book title or author: ")
            library.search_books(keyword)
        elif choice == '5':
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            library.borrow_book(member_id, book_id)
        elif choice == '6':
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            library.return_book(member_id, book_id)
        elif choice == '7':
            member_id = int(input("Enter member ID: "))
            library.view_members_borrowed_books(member_id)
        elif choice == '8':
            library.view_overdue_books()
        elif choice == '9':
            library.library_report()
        elif choice == '10':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)
        elif choice == '11':
            name = input("Enter member name: ")
            library.register_member(name)
        elif choice == '0':
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 11.")

if __name__ == "__main__":
    menu()