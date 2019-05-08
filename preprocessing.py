import pandas as pd
import sqlite3
from sqlite3 import Error
import logging
import numpy as np

class importData(object):

    def __init__(self):
        pass

    def sqliteConnect(self, db_file, query=None):
        ''' create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        '''
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


    def loadCsv(self, uri, header=0):
        '''Load a CSV file into a pandas dataframe.
        
        Usage 
        -------
        uri = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv'
        data = importData()
        data.loadCsv(uri, header=0)
        
        Input
        ------
        uri : HTTP URL, or file location for CSV file.
        header : None if no column names in are in CSV file. header=0 if column 
                 names are to be inferred from the first line of the file
        
        Return
        -------
        pandas.core.frame.DataFrame
        '''
        self.df = pd.read_csv(uri, header=header)
        return self.df

        
    def selectData(self, df, colIndeces=None, colNames=None, rows=None):
        '''Select columns from an imported pandas dataframe'''
        #return df[colIndeces][rows]
        pass
        