from mimesis import Person, Text, Datetime, Generic
from db_models.book_model import Book

text = Text()
person = Person()
datetime = Datetime()


class DataGenerator:
    @staticmethod
    def generate_title():
        return Generic().text.title()

    @staticmethod
    def generate_author():
        return Generic().person.full_name()

    @staticmethod
    def generate_year():
        return Generic().datetime.year()

    @staticmethod
    def generate_books(num_of_records):
        data = []

        for record in range(num_of_records):
            data.append(Book(title=DataGenerator().generate_title(), author=DataGenerator().generate_author(),
                             year=DataGenerator().generate_year()))
        return data

    @staticmethod
    def fill_books_from_test_data(test_data_of_books):
        book_data = []

        for book in test_data_of_books:
            book_data.append(Book(title=book["title"], author=book["author"], year=book["year"]))
        return book_data
