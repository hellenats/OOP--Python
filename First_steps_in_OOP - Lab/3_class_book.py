class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


book1 = Book('Twisted Hate', 'Ana Huang', 222)
print(book1.name)
print(book1.author)
print(book1.pages)