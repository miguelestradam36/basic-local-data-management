from .sqlite_handler import SqLiteManager

class DataManager(SqLiteManager):
    """
        
    """
    #module as attribute to facilitate imports
    pd = __import__('pandas') #pandas module as attribute
    sys = __import__('sys') #sys module as attribute

    #normal attributes
    filename_ = '' #excel output filename

    #------------------------
    # Methods
    #------------------------

    def __init__(self):
        """
        Function that initializes class
        Objective: flag the start of Data Handling
        Params: No arguments/parameters
        """
        print('Starting data management services...')

    @property
    def filename(self):
        """
        Getter method
        ---
        Objective: retrieve excel filename
        Params: No arguments/parameters
        """
        return self.filename_

    @filename.setter
    def filename(self, filename:str):
        """
        Setter method
        ---
        Objective: Save data into filename provided
        Params: filename (string [Required])
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
        """
        Class method
        ---
        Params: No parameters/arguments
        Objective: Write database to excel sheet with tables as sheets.
        """
        try:
            assert self.filename != ''
            assert self.connection != ''
            print('transforming excel into SqLite Database')
            for sheet_name in self.xls.sheet_names:
                try:
                    df = self.pd.read_excel(self.xls, sheet_name=sheet_name)
                    df.to_sql(sheet_name, self.connection, if_exists="replace")
                    print('reading sheet {}...'.format(sheet_name))
                except:
                    print('ERROR: Unable to read sheet {} from excel file...'.format(sheet_name))
        except Exception as error:
            print("\nERROR: {}\n".format(error))

    def __del__(self):
        """
        Deletion method, this is done automatically once all the tasks have been executed
        Objective: Marks the end of processing.
        Params: No arguments/parameters
        """
        print('finished reading and transforming data...')