from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_models.book_model import Base
from utils.data_generator import DataGenerator


class DBManager:
    @staticmethod
    def create_engine_memory():
        return create_engine('sqlite:///:memory:')

    @staticmethod
    def create_engine_file(db_path):
        return create_engine(db_path)

    @staticmethod
    def create_tables(engine):
        Base.metadata.create_all(engine)

    @staticmethod
    def drop_tables(engine):
        Base.metadata.drop_all(engine)

    @staticmethod
    def create_session(engine):
        Session = sessionmaker(bind=engine)
        return Session()

    @staticmethod
    def populate_db(session, num_books=10):
        books = DataGenerator().generate_books(num_books)
        session.add_all(books)
        session.commit()
