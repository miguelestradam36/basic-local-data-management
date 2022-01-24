class DataManager():
    pd = __import__('pandas')

    @property
    def filename(self):
        return self.filename

    @property.setter
    def filename(self, filename:str):
        print('setting new data source...')
        self.filename = filename
        print('reading source...')
        try:
            self.xls = self.pd.ExcelFile(self.filename)
        except Exception as error:
            print("\nERROR: {}\n".format(error))

    def get_sheet(self, sheet_name:str):
        print('reading sheet...')
        try:
            df = self.pd.read_excel(self.xls, sheet_name)
            return df
        except Exception as error:
            print("\nERROR: {}\n".format(error))
        return None

    def __del__(self):
        print('finished reading and transforming data...')