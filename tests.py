import pytest
def test_add_new_book_add_two_books(setup):
    setup.add_new_book('Гордость и предубеждение и зомби')
    setup.add_new_book('Что делать, если ваш кот хочет вас убить')
    assert len(setup.get_books_genre()) == 2

def test_books_genre_initialization_empty_dict(setup):
    assert setup.books_genre == {}

def test_favorites_initialization_empty_list(setup):
    assert setup.favorites == []

def test_genre_initialization_check_genre(setup):
    for genre in setup.genre:
        assert genre in setup.genre

def test_genre_age_rating_initialization_check_genre_age(setup):
    for genre_age in setup.genre_age_rating:
        assert genre_age in setup.genre_age_rating

@pytest.mark.parametrize('book', ['Мощи святого Леопольда'])
def test_add_new_book_name_book_name_added(setup, book):
    setup.add_new_book('Мощи святого Леопольда')
    assert book in setup.books_genre

@pytest.mark.parametrize('genre', ['Фантастика'])
def test_set_book_genre_add_genre_genre_added_book(setup, genre):
    setup.add_new_book('Мощи святого Леопольда')
    setup.set_book_genre('Мощи святого Леопольда', 'Фантастика')
    assert setup.get_book_genre('Мощи святого Леопольда') == genre

@pytest.mark.parametrize('genre', ['Ужасы'])
def test_get_book_genre_check_genre_added_book(setup, genre):
    setup.add_new_book('Кладбище домашних животных')
    setup.set_book_genre('Кладбище домашних животных', 'Ужасы')
    assert setup.get_book_genre('Кладбище домашних животных') == genre

@pytest.mark.parametrize('book', ['Смерть на Ниле'])
def test_get_books_with_specific_genre_get_desired_genre(setup, book):
    setup.add_new_book('Смерть на Ниле')
    setup.set_book_genre('Смерть на Ниле', 'Детективы')
    setup.add_new_book('Незнайка')
    setup.set_book_genre('Незнайка', 'Мультфильмы')
    assert book in setup.get_books_with_specific_genre('Детективы')

@pytest.mark.parametrize("book", [{'Смерть на Ниле': 'Детективы', 'Незнайка': 'Мультфильмы', 'Винни пух': 'Мультфильмы'}])
def test_get_books_genre_add_books_and_genre_list_books(setup, book):
    setup.add_new_book('Смерть на Ниле')
    setup.set_book_genre('Смерть на Ниле', 'Детективы')
    setup.add_new_book('Незнайка')
    setup.set_book_genre('Незнайка', 'Мультфильмы')
    setup.add_new_book('Винни пух')
    setup.set_book_genre('Винни пух', 'Мультфильмы')
    assert setup.get_books_genre() == book

@pytest.mark.parametrize('book', ['Незнайка'])
def test_get_books_for_children_add_children_genre_books_get_books(setup, book):
    setup.add_new_book('Незнайка')
    setup.set_book_genre('Незнайка', 'Мультфильмы')
    setup.get_books_for_children()
    assert book in setup.get_books_for_children()

@pytest.mark.parametrize('book', ['Смерть на Ниле'])
def test_add_book_in_favorites_add_books_books_in_favorites(setup, book):
    setup.add_new_book('Смерть на Ниле')
    setup.set_book_genre('Смерть на Ниле', 'Детективы')
    setup.add_book_in_favorites('Смерть на Ниле')
    assert book in setup.favorites

def test_delete_book_from_favorites_books_favorites_empty_list(setup):
    setup.add_new_book('Смерть на Ниле')
    setup.set_book_genre('Смерть на Ниле', 'Детективы')
    setup.add_book_in_favorites('Смерть на Ниле')
    setup.delete_book_from_favorites('Смерть на Ниле')
    assert len(setup.favorites) == 0

@pytest.mark.parametrize('book', ['Смерть на Ниле'])
def test_get_list_of_favorites_books_add_and_check_favorit_list(setup, book):
    setup.add_new_book('Смерть на Ниле')
    setup.set_book_genre('Смерть на Ниле', 'Детективы')
    setup.add_book_in_favorites('Смерть на Ниле')
    setup.get_list_of_favorites_books()
    assert book in setup.get_list_of_favorites_books()
