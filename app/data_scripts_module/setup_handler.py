class SetUpManager():
    #modules as attributes to facilitate imports
    os = __import__('os')
    sys = __import__('sys')

    #Normal attributes
    requirements_location_ = ''

    #------------------------
    # Methods
    #------------------------

    @property
    def requirements_location(self):
        """
        Getter method, which is used to define the config file path.
        """
        return self.requirements_location_

    @requirements_location.setter
    def requirements_location(self, file_path:str):
        """
        Setter method, which can be compared to: 
            pip install -r requirements.txt

        param -> file_path: Location of requirements.txt file
        param -> file_path: string      
        """
        print('Checking system...')
        self.requirements_location_ = file_path

        with open(self.requirements_location, 'r') as file:
            modules = file.readlines()
        
        for module in modules:
            module = module.rstrip()
            self.check_module(module=module)

    def check_module(self, module:str)->bool:
        """
        Method to check python module into environment

        param -> module: module to be checked
        param -> module: string
        """
        try:
            __import__(module)
            print('Checking {} module into environment...'.format(module))
            print('module {} confirmed on environment'.format(module))
            return True
        except:
            print('Installing module {}...'.format(module))
            self.os.system('pip install {} --quiet'.format(module))
            return False
    
    def __del__(self):
        print("Finished setting up dependencies...\n")