from sqlite_handler import SqLiteManager

class DataManager(SqLiteManager):
    """
        
    """
    #module as attribute to facilitate imports
    pd = __import__('pandas')

    def __init__(self):
        print('Starting data management services...')

    @property
    def filename(self):
        """
        
        """
        return self.filename

    @property.setter
    def filename(self, filename:str):
        """
        
        """
        print('setting new data source...')
        self.filename = filename
        print('reading source...')
        try:
            self.xls = self.pd.ExcelFile(self.filename)
        except Exception as error:
            print("\nERROR: {}\n".format(error))

    def get_sheet(self, sheet_name:str):
        """
        
        """
        print('reading sheet...')
        try:
            df = self.pd.read_excel(self.xls, sheet_name)
            return df
        except Exception as error:
            print("\nERROR: {}\n".format(error))
        return None

    def excel_to_db(self)->None:
        try:
            print('transforming excel into SqLite Database')
        except Exception as error:
            print("\nERROR: {}\n".format(error))

    def __del__(self):
        """
        Deletion method, this is done automatically once all the tasks have been executed
        """
        print('finished reading and transforming data...')