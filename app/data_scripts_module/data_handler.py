from .sqlite_handler import SqLiteManager

class DataManager(SqLiteManager):
    """
        
    """
    #module as attribute to facilitate imports
    pd = __import__('pandas')
    sys = __import__('sys')

    #normal attributes
    filename_ = ''

    #------------------------
    # Methods
    #------------------------

    def __init__(self):
        print('Starting data management services...')

    @property
    def filename(self):
        """
        
        """
        return self.filename_

    @filename.setter
    def filename(self, filename:str):
        """
        
        """
        print('setting new data source...')
        self.filename_ = filename
        print('reading source...')
        try:
            self.xls = self.pd.ExcelFile(self.filename)
        except Exception as error:
            print('Unable to read Excel file...')
            print("\nERROR: {}\n".format(error))
            self.sys.exit(-1)


    def excel_to_db(self)->None:
        try:
            assert self.filename != ''
            assert self.connection != ''
            print('transforming excel into SqLite Database')
            for sheet_name in self.xls.sheet_names:
                print('reading sheet {}...'.format(sheet_name))
                try:
                    df = self.pd.read_excel(self.xls, sheet_name=sheet_name)
                    df.to_sql(sheet_name, self.connection, if_exists="replace")
                except:
                    print('ERROR: Unable to read sheet {} from excel file...'.format(sheet_name))
        except Exception as error:
            print("\nERROR: {}\n".format(error))

    def __del__(self):
        """
        Deletion method, this is done automatically once all the tasks have been executed
        """
        print('finished reading and transforming data...')