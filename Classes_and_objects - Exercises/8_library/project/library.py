from typing import List, Dict

from project.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str: list] = {}    # {'author': [book1, book2]}
        self.rented_books: Dict[str: Dict[str]] = {}       # {usernames: {book names: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in self.books_available:
            if book_name in self.books_available[author]:
                user.books.append(book_name)
                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {}
                self.rented_books[user.username][book_name] = days_to_return
                self.books_available[author].remove(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"

            find_return_days = next((days for books in self.rented_books.values()
                              for book, days in books.items() if book == book_name), None)
            if find_return_days is not None:
                return f'The book "{book_name}" is already rented and will be available in {find_return_days} days!'

    def return_book(self, author:str, book_name:str, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        user.books.remove(book_name)
        self.books_available[author].append(book_name)
        del self.rented_books[user.username][book_name]
