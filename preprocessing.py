import pandas as pd
import sqlite3
from sqlite3 import Error
import logging
import numpy as np

class importData(object):

    def __init__(self):
        pass

    def sqliteConnect(self, db_file, query=None):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            logging.exception(e)
            return None
        c = conn.cursor()

        # Execution query
        df = pd.read_sql(query, conn)

        # Close connection
        conn.commit()
        conn.close()


    def loadCsv(self, uri, header=None):
        df = pd.read_csv(uri, header=header)

        print("data import successful\n")
        print(df.head())
