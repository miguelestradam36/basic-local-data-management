class SqLiteManager():
    #module as attribute to facilitate imports
    sqlite3 = __import__('sqlite3')

    def __init__(self):
        print('Starting SqLite services...')

    @property
    def database(self):
        """
        
        """
        return self.database

    @property.setter
    def database(self, db_path:str):
        """
        
        """
        self.database = db_path
        try:
            print('connecting to database...')
            self.connection = self.sqlite3.connect(self.database)
            self.cursor = self.connection.cursor()
            print('connection to database started...')
        except Exception as error:
            print("\nERROR: {}\n".format(error))

    def load_data(self):
        """
        
        """
        print('Starting data load...')

    def __del__(self):
        """
        
        """
        try:
            print('Automatically saving changes...')
            self.connection.commit()
        except Exception as error:
            print("\nERROR: {}\n".format(error))
        finally:
            try:
                print('Closing connection...')
                self.cursor.close()
            except Exception as error:
                print("\nERROR: {}\n".format(error))