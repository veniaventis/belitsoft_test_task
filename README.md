# Test Assignment: Database Management

This project is a test assignment for creating and testing a book library database using SQLite. The tasks include setting up the database, writing automated tests with pytest, and ensuring the functionality of various database operations. Below are the instructions and details regarding the implementation.


Scripts Overview

    create_db.py: A script to create and populate the database.
    test_database.py: A set of automated tests using pytest to verify various database operations.

Automated Tests

The tests will cover the following operations:

    Adding a book
    Retrieving a list of all books
    Retrieving book information by ID
    Updating book information by ID
    Deleting a book by ID
    Attempting to retrieve a non-existent book

The tests will use fixtures to create a test database and clean it up after each test.

**Running the Scripts and Tests:**

To run the scripts and tests, on GitHub Actions follow these steps:

How to Use GitHub Actions Workflow

    Trigger the workflow manually:
        Go to the "Actions" tab in this GitHub repository.
        Select the workflow named "Run Data Base Tests".
        Click on "Run workflow" and choose the desired deployment-target.

    Available Targets:
        database_test: Runs the pytest tests on the database.
        creation_data_base: Runs the database creation script and verifies the database setup.


To run the scripts and tests, local machine follow these steps:

1. Clone the repository:

        git clone <repository-url>
        cd <repository-directory>
2. Set up a virtual environment and install dependencies:
  
         python -m venv venv
         source venv/bin/activate  # On Windows use `venv\Scripts\activate`
         pip install -r requirements.txt

3. Install dependencies

         pip install -r requirements.txt

4. Create and populate the database:

         python3 create_db.py

5. Run the automated tests:

         pytest -v test_database.py


**How to Use GitHub Actions Workflow**

    Trigger the workflow manually:
        Go to the "Actions" tab in your GitHub repository.
        Select the workflow named "Run Data Base Tests".
        Click on "Run workflow" and choose the desired deployment-target.

    Available Targets:
        database_test: Runs the pytest tests on the database.
        creation_data_base: Runs the database creation script and verifies the database setup.