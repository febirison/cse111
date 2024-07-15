import pytest
import datetime

from library_management_system import (
    load_books, save_books, add_book, update_book, checkout_book,
    return_book, search_books, validate_book_info, calculate_due_date
)

def test_add_book():
    books = []
    new_book = {
        'id': '1',
        'title': 'Test Book',
        'author': 'Test Author',
        'genre': 'Test Genre',
        'checked_out': 'False',
        'due_date': '',
        'patron': ''
    }
    add_book(books, new_book)
    assert books[0] == new_book

def test_update_book():
    books = [{
        'id': '1',
        'title': 'Old Title',
        'author': 'Old Author',
        'genre': 'Old Genre',
        'checked_out': 'False',
        'due_date': '',
        'patron': ''
    }]
    updated_info = {'title': 'New Title', 'author': 'New Author', 'genre': 'New Genre'}
    assert update_book(books, '1', updated_info)
    assert books[0]['title'] == 'New Title'
    assert books[0]['author'] == 'New Author'
    assert books[0]['genre'] == 'New Genre'

def test_checkout_book():
    books = [{
        'id': '1',
        'title': 'Test Book',
        'author': 'Test Author',
        'genre': 'Test Genre',
        'checked_out': 'False',
        'due_date': '',
        'patron': ''
    }]
    patron = 'Test Patron'
    assert checkout_book(books, '1', patron)
    assert books[0]['checked_out'] == 'True'
    assert books[0]['patron'] == patron

def test_return_book():
    books = [{
        'id': '1',
        'title': 'Test Book',
        'author': 'Test Author',
        'genre': 'Test Genre',
        'checked_out': 'True',
        'due_date': '2024-07-23',
        'patron': 'Test Patron'
    }]
    assert return_book(books, '1')
    assert books[0]['checked_out'] == 'False'
    assert books[0]['due_date'] == ''
    assert books[0]['patron'] == ''

def test_search_books():
    books = [{
        'id': '1',
        'title': 'Test Book',
        'author': 'Test Author',
        'genre': 'Test Genre',
        'checked_out': 'False',
        'due_date': '',
        'patron': ''
    }]
    search_criteria = {'title': 'Test Book'}
    results = search_books(books, search_criteria)
    assert len(results) == 1
    assert results[0]['title'] == 'Test Book'

def test_validate_book_info():
    valid_book_info = {'id': '1', 'title': 'Test Book', 'author': 'Test Author', 'genre': 'Test Genre'}
    invalid_book_info = {'id': '', 'title': 'Test Book', 'author': 'Test Author', 'genre': 'Test Genre'}
    assert validate_book_info(valid_book_info)
    assert not validate_book_info(invalid_book_info)

def test_calculate_due_date():
    current_date = datetime.datetime(2024, 7, 9)
    due_date = calculate_due_date(current_date)
    assert due_date == '2024-07-23'

if __name__ == "__main__":
    pytest.main()
