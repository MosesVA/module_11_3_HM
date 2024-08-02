import json


class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre


class Librarian:
    def __init__(self, name, librarian_id):
        self.name = name
        self.librarian_id = librarian_id


class Reader:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email


class AddBookCommand:
    def __init__(self, book, library):
        self.book = book
        self.library = library

    def execute(self):
        self.library.add_book(self.book)


class ReaderController:
    def __init__(self):
        self.readers = {}

    def add_reader(self, reader: object):
        self.readers[reader.get_name()] = reader.get_email()

    def to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.readers, file, ensure_ascii=False, indent=2)
            return f'Читатели записаны в файл {filename}.json'

    def from_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data


class LibraryController:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена в библиотеку.")


if __name__ == "__main__":
    reader1 = Reader('Вася', 'vasya@mail.ru')
    reader2 = Reader('Петя', 'petya@mail.ru')
    reader3 = Reader('Маша', 'masha@mail.ru')
    lib_controller = LibraryController()
    readers_controller = ReaderController()

    book1 = Book("Дюна", "Фрэнк Герберт", "Фантастика")
    book2 = Book("Незнайка на Луне", "Николай Носов", "Детская Сказка")

    add_book_cmd = AddBookCommand(book1, lib_controller)
    add_book_cmd.execute()

    add_book_cmd = AddBookCommand(book2, lib_controller)
    add_book_cmd.execute()

    readers_controller.add_reader(reader1)
    readers_controller.add_reader(reader2)
    readers_controller.add_reader(reader3)
    print(readers_controller.to_json('Читатели.json'))
    print(readers_controller.from_json('Читатели.json'))
