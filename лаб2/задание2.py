class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages


class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        """Возвращает следующий доступный ID для добавления новой книги."""
        if not self.books:
            return 1
        else:
            last_book = max(self.books, key=lambda x: x.id)
            return last_book.id + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги в списке по её уникальному ID.

        :param book_id: Целое число — уникальный идентификатор книги.
        :return: Индекс книги в списке, либо ошибка ValueError, если книга отсутствует.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


# Определение тестового набора данных
BOOKS_DATABASE = [
    {"id": 1, "name": "test_name_1", "pages": 200},
    {"id": 2, "name": "test_name_2", "pages": 400}
]

# Основная программа для проверки функционала классов
if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверка следующего ID для пустой библиотеки

    # Создаем список объектов-книг из предопределенной базы данных
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])
        for book_dict in BOOKS_DATABASE
    ]

    # Инициализация библиотеки с набором книг
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())  # проверка следующего ID для библиотеки с книгами

    # Проверка индекса книги с известным ID
    print(library_with_books.get_index_by_book_id(1))


