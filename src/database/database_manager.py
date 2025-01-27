# src/database/database_manager.py

import sqlite3

class DatabaseManager:
    """
    A class to manage interactions with the database.
    """
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """
        Establishes a connection to the database.
        """
        self.connection = sqlite3.connect(self.db_path)
        print("Connected to the database.")

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()
            print("Closed the database connection.")
