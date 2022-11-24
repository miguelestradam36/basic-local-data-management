class SqLiteManager():
    #module as attribute to facilitate imports
    sqlite3 = __import__('sqlite3') #sqlite3 module as attribute

    #normal attributes
    database_ = '' #database file location

    #------------------------
    # Methods
    #------------------------
    
    def __init__(self):
        """
        Function that initializes class
        ---
        Objective: Flags the start of process
        Params: No arguments/parameters
        """
        print('Starting SqLite services...')

    @property
    def database(self):
        """
        Getter method
        ---
        Objective: returns database path location.
        Params: No arguments/parameters
        """
        return self.database_

    @database.setter
    def database(self, db_path:str):
        """
        Setter method
        ---
        Objective: Called to define the connection to SqLite connection
        Params:
            param -> db_path: Location of database into which we are going to write/get our data.
            param -> db_path: string       
        """
        try:
            self.database_ = db_path
            print('connecting to database...')
            self.connection = self.sqlite3.connect(self.database)
            self.cursor = self.connection.cursor()
            print('connection to database started...')
        except Exception as error:
            print("\nERROR: {}\n".format(error))

    def run_query(self, from_file:bool=False, script:str="SELECT * FROM Invoices")->None:
        """
        Setter method
        ---
        Objective: Called to define the connection to SqLite connection
        Params:
            param -> db_path -> description: 
            param -> db_path -> type: string
            param -> db_path -> default: 'SHOW TABLES;'

            param -> db_path -> description: 
            param -> db_path -> type: bool
            param -> db_path -> default: False
        """
        try:
            if from_file:
                with open(script, 'r') as sql_file:
                    script = sql_file.read()
            self.cursor.execute(script)
            print('\n',self.cursor.fetchall(),'\n')
        except Exception as error:
            print("\nERROR: {}\n".format(error))
        finally:
            if self.save_changes():
                print('commited action...')

    def save_changes(self)->bool:
        """
        Class method
        ---
        Output: boolean value returned
        Params: No arguments/parameters
        Objective: Changes into SqLite database have to be commited in order to be saved.  
        """
        try:
            print('Automatically saving changes...')
            self.connection.commit()
            return True
        except Exception as error:
            print("\nERROR: {}\n".format(error))
        return False

    def __del__(self):
        """
        Deletion method, this is done automatically once all the tasks have been executed
        ---
        Params: No arguments/parameters
        Objective: In this case, the changes done to the database will be automatically commited and the connection closed.
        """

        self.save_changes()

        self.cursor.close()