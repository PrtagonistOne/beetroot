class Author:
    def __init__(self, name: str, country: str, birthday: str, books: list):
        self.name = name.lower()
        self.country = country.lower()
        self.birthday = birthday.lower()
        self.books = books

    def __str__(self):
        return f'Name: {self.name.title()}, {self.country.title()}, birthday: {self.birthday}, books: {self.books}\n'

    def __repr__(self):
        return self.__str__()


class Book:
    def __init__(self, name: str, year: int, author: Author):
        self.name = name.lower()
        self.year = year
        self.author = author

    def __str__(self):
        return f'name: {self.name.title()}, year: {self.year}, author: {self.author}'

    def __repr__(self):
        return self.__str__()


class Library:
    def __init__(self, name: str, books: list, authors: list):
        self.name = name.lower()
        self.books = books
        self.authors = authors

    def new_book(self, name: str, year: int, author: Author) -> Book:
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author_: Author) -> list:
        top = []
        bottom = []
        for i, book in enumerate(self.books):
            if book.author.name == author_.name:
                top.append(book)
            if book.author.name != author_.name:
                bottom.append(book)

        top.extend(bottom)
        return top

    def group_by_year(self, year: int) -> list:
        top = []
        bottom = []
        for i, book in enumerate(self.books):
            if book.year == year:
                top.append(book)
            if book.year != year:
                bottom.append(book)

        top.extend(bottom)
        return top


library = Library('Olga Kobilyanska Library', [], [])
author1 = Author('Lev Tolstoi', 'Tsar Russia', '09.09.1828', ['War and peace', 'A Confession', 'Childhood'])
author2 = Author('Mark Twain', 'Great Britain', '30.11.1835', ['Roughing it', 'Gilded Age', 'Life of the Mississippi'])

library.new_book('Family Happiness', 1859, author1)
library.new_book('Following the Equator', 1897, author2)

print(library.group_by_author(author1))
print(library.group_by_author(author2))
print()
print(library.group_by_year(1897))
print(library.group_by_year(1859))

