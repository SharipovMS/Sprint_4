import pytest

class TestBooksCollector:
    def test_add_new_book_add_two_books(self, setup):
        setup.add_new_book('Гордость и предубеждение и зомби')
        setup.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(setup.get_books_genre()) == 2

    def test_books_genre_initialization_empty_dict(self, setup):
        assert setup.books_genre == {}

    def test_favorites_initialization_empty_list(self, setup):
        assert setup.favorites == []

    @pytest.mark.parametrize('books', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_genre_initialization_genre_age_rating(self, setup, books):
        assert books in setup.genre

    @pytest.mark.parametrize('books', ['Ужасы', 'Детективы'])
    def test_genre_age_rating_initialization_check_genre_age(self, setup, books):
        assert books in setup.genre_age_rating

    def test_add_new_book_name_book_name_added(self, setup):
        setup.add_new_book('Мощи святого Леопольда')
        assert 'Мощи святого Леопольда' in setup.get_books_genre()

    def test_set_book_genre_add_genre_genre_added_book(self, setup):
        setup.add_new_book('Мощи святого Леопольда')
        setup.set_book_genre('Мощи святого Леопольда', 'Фантастика')
        assert setup.get_book_genre('Мощи святого Леопольда') == 'Фантастика'

    def test_get_books_with_specific_genre_get_desired_genre(self, setup):
        setup.add_new_book('Смерть на Ниле')
        setup.set_book_genre('Смерть на Ниле', 'Детективы')
        setup.add_new_book('Незнайка')
        setup.set_book_genre('Незнайка', 'Мультфильмы')
        assert 'Смерть на Ниле' in setup.get_books_with_specific_genre('Детективы')

    @pytest.mark.parametrize("book", [{'Смерть на Ниле': 'Детективы', 'Незнайка': 'Мультфильмы', 'Винни пух': 'Мультфильмы'}])
    def test_get_books_genre_add_books_and_genre_list_books(self, setup, book):
        setup.add_new_book('Смерть на Ниле')
        setup.set_book_genre('Смерть на Ниле', 'Детективы')
        setup.add_new_book('Незнайка')
        setup.set_book_genre('Незнайка', 'Мультфильмы')
        setup.add_new_book('Винни пух')
        setup.set_book_genre('Винни пух', 'Мультфильмы')
        assert setup.get_books_genre() == book

    def test_get_books_for_children_add_children_genre_books_get_books(self, setup):
        setup.add_new_book('Незнайка')
        setup.set_book_genre('Незнайка', 'Мультфильмы')
        assert 'Незнайка' in setup.get_books_for_children()

    def test_add_book_in_favorites_add_books_books_in_favorites(self, setup):
        setup.add_new_book('Смерть на Ниле')
        setup.add_book_in_favorites('Смерть на Ниле')
        assert 'Смерть на Ниле' in setup.get_list_of_favorites_books()

    def test_delete_book_from_favorites_books_favorites_empty_list(self, setup):
        setup.add_new_book('Смерть на Ниле')
        setup.add_book_in_favorites('Смерть на Ниле')
        setup.delete_book_from_favorites('Смерть на Ниле')
        assert len(setup.get_list_of_favorites_books()) == 0
    def test_get_list_of_favorites_books_add_and_check_favorit_list(self, setup):
        setup.add_new_book('Смерть на Ниле')
        setup.add_book_in_favorites('Смерть на Ниле')
        assert 'Смерть на Ниле' in setup.get_list_of_favorites_books()
