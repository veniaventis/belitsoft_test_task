from utils.db_manager import DBManager
from utils.get_data import TestDataGet


def main():
    engine = DBManager.create_engine_file(TestDataGet.get_config_data('data_base_path'))
    DBManager.create_tables(engine)
    session = DBManager.create_session(engine)

    DBManager.populate_db(session, num_books=10)

    print("Database created and populated with initial data.")


if __name__ == '__main__':
    main()
