from utils.db_manager import DBManager
from utils.get_data import TestDataGet


def main():
    engine = DBManager.create_engine_file(TestDataGet.get_config_data('data_base_path'))
    DBManager.create_tables(engine)
    session = DBManager.create_session(engine)
    count_of_books = TestDataGet.get_test_data('count_of_books')

    DBManager.populate_db(session, num_books=count_of_books)

    print("Database created and populated with initial data.")


if __name__ == '__main__':
    main()
