class Book:
    def __init__(self, id_, name, pages):
        """
        Конструктор класса Book, который принимает id, название книги и количество страниц.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Метод возвращает красивую строку с информацией о книге.
        Формат вывода: Книга "название_книги"
        """
        return f"Книга \"{self.name}\""

    def __repr__(self):
        """
        Метод возвращает валидную строку, по которой можно воссоздать экземпляр класса.
        Формат вывода: Book(id_=..., name=..., pages=...)
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

# Данные для тестирования
BOOKS_DATABASE = [
    {"id": 1, "name": "test_name_1", "pages": 200},
    {"id": 2, "name": "test_name_2", "pages": 400}
]

if __name__ == '__main__':
    # Создаём список книг на основе базы данных
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])
        for book_dict in BOOKS_DATABASE
    ]

    # Проверяем метод __str__
    for book in list_books:
        print(book)

    # Проверяем метод __repr__
    print(list_books)

