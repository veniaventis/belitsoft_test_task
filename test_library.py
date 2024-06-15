import pytest
from models.models import Book
from utils.db_manager import DBManager
from utils.data_generator import DataGenerator
from utils.get_data import TestDataGet

get_all_books_form_test_data = TestDataGet.get_test_data("books")
id_from_data_test = TestDataGet.get_test_data("test_id")
wrong_id_from_data_test = TestDataGet.get_test_data("wrong_id")


@pytest.fixture(scope="function")
def db_session():
    engine = DBManager.create_engine_memory()
    DBManager.create_tables(engine)
    session = DBManager.create_session(engine)
    books = DataGenerator.fill_books_from_test_data(TestDataGet.get_test_data("books"))
    session.add_all(books)

    yield session

    session.close()
    DBManager.drop_tables(engine)


def test_add_book(db_session):
    new_author = DataGenerator.generate_author()
    new_title = DataGenerator.generate_title()
    new_year = DataGenerator.generate_year()
    new_book = Book(title=new_title, author=new_author, year=new_year)

    db_session.add(new_book)
    db_session.commit()

    book = db_session.query(Book).filter_by(title=new_title).first()

    assert book.title == new_title
    assert book.author == new_author
    assert book.year == new_year


def test_get_all_books(db_session):
    books = db_session.query(Book).all()
    assert len(books) == len(get_all_books_form_test_data)


def test_get_book_by_id(db_session,):
    book = db_session.query(Book).filter_by(id=id_from_data_test).first()

    assert book.title == TestDataGet.get_data_from_books_object(id_from_data_test, "title")
    assert book.author == TestDataGet.get_data_from_books_object(id_from_data_test, "author")
    assert book.year == TestDataGet.get_data_from_books_object(id_from_data_test, "year")


def test_update_book_by_id(db_session):
    new_title = DataGenerator.generate_title()
    new_author = DataGenerator.generate_author()
    new_year = DataGenerator.generate_year()

    book = db_session.query(Book).filter_by(id=id_from_data_test).first()
    book.title = new_title
    book.author = new_author
    book.year = new_year
    db_session.commit()

    updated_book = db_session.query(Book).filter_by(id=id_from_data_test).first()

    assert updated_book.title == new_title
    assert updated_book.author == new_author
    assert updated_book.year == new_year


def test_delete_book_by_id(db_session):
    book = db_session.query(Book).filter_by(id=id_from_data_test).first()
    db_session.delete(book)
    db_session.commit()

    deleted_book = db_session.query(Book).filter_by(id=id_from_data_test).first()

    assert deleted_book is None


def test_get_nonexistent_book(db_session):
    book = db_session.query(Book).filter_by(id=wrong_id_from_data_test).first()

    assert book is None
