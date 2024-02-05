# qa_python - спринт 4 Ui тесты.
##Тесты находятся в файле tests.py##

Тест на добавление двух новых книг :: test_add_new_book_add_two_books

Тесты на инициализацию:

test_books_genre_initialization_empty_dict :: словарь books_genre пустой.
test_favorites_initialization_empty_list :: список favorites пустой.
test_genre_initialization_check_genre :: список genre содержит правильные значения.
test_genre_age_rating_initialization_check_genre_age :: список genre_age_rating содержит дефолтные значения.

test_add_new_book_name_book_name_added :: Этот тест проверяет, добавлено ли конкретное название книги в словарь books_genre при вызове метода add_new_book.

test_set_book_genre_add_genre_genre_added_book :: Этот тест проверяет, правильно ли определенный жанр добавлен в книгу в словаре books_genre при вызове метода set_book_genre.

test_get_book_genre_check_genre_added_book :: Этот тест проверяет, правильно ли получен жанр конкретной книги в словаре books_genre с использованием метода get_book_genre.

test_get_books_with_specific_genre_get_desired_genre :: Этот тест гарантирует, что конкретная книга с определенным жанром включена в список книг, возвращаемых методом get_books_with_specific_genre.

test_get_books_genre_add_books_and_genre_list_books :: Этот тест проверяет, возвращает ли метод get_books_genre правильный словарь книг и их жанров после добавления нескольких книг и жанров.

test_get_books_for_children_add_children_genre_books_get_books :: Этот тест проверяет, включена ли книга с жанром "Мультфильмы" (Дети) в список книг, возвращаемых методом get_books_for_children.

test_add_book_in_favorites_add_books_books_in_favorites :: Этот тест гарантирует, что конкретная книга будет добавлена в список избранного при вызове метода add_book_in_favorites.

test_delete_book_from_favorites_books_favorites_empty_list :: Этот тест проверяет, правильно ли метод delete_book_from_favorites удаляет книгу из списка избранного.

test_get_list_of_favorites_books_add_and_check_favorit_list :: Этот тест проверяет, включена ли конкретная книга в список книг, возвращаемый методом get_list_of_favorites_books после добавления ее в список избранных.

Для тестов используется конструкция @pytest.fixture, она инициализирует создание объекта класса BookCollector и находится в файле conftest.py

**Запуск тестов выполняется командой:**

<pytest -v tests.py>

**Оценка покрытия выполняется командой:**

<pytest --cov=main>

**Расширеная оценка покрытия: **

<pytest --cov=main --cov-report=html>



